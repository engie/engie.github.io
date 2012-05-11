---
layout: post
title: Using more of the CPU
---
At [Navetas](http://www.navetas.com) we are trying to help people understand where the electricity they pay for is going. We measure the electricity where it flows into the building and analyse these signals to work out what each bit of energy is going to be used for. This is hard enough at home with TVs, fridges, lights, etc but in a factory it gets even more tricky. Factory equipment can draw significant amounts of power and tends to be in constant use, although the amount of power used can jump around second by second.

To understand this twitchy data we have developed some new algorithms that take a more detailed look at the electricity being consumed, millisecond by millisecond. These are giving tremendously accurate results at the expense of needing far more computer power to run. We recently put together a system for a real world trial in a customer factory but a week before we had to ship it looked like it just wasn't going to be fast enough. Our system runs in real time so it has to be able to process at least one second of data per second!

First things first when trying to speed up a program that has to ship next week: we brought the fastest, most expensive laptop we could find. It sounds like a [chinook](http://www.youtube.com/watch?v=1BTBrJb3P9o) in full flight and only fits on the lap of the seriously obese. After a fun few days in which we found that Dell laptops don't run at full pelt without a special super power supply, and that occasionally Dell forget and ship you the normal weedy power supply, we found that even our thermo-nuclear laptop wasn't enough.

Next we fired up the profiler. We used [callgrind](http://valgrind.org/docs/manual/cl-manual.html) and found that our app spent almost all its time calculating one distance metric. We looked at the algorithms to try and see if we could be smarter about this but no - all those sums had to be done to get the results we required. It's worth noting that callgrind showed that we were working pretty much entirely from cache, so there wasn't much mileage in reducing the amount of data in the working set.

[Alex](http://uk.linkedin.com/pub/alex-wilson/0/684/825) then played with compiler options to try and persuade the optimiser to generate a faster executable and also tried the Visual Studio and Intel compilers that are famed for producing the fastest output.

We even gave the computer a stern talking to.

In parallel with the compiler tweaking I had a more detailed look at exactly what the system was doing when it was calculating this distance metric. The system was spending all its time doing a simple matrix vector product, gazillions of times a second. The product:

![Matrix Vector Equation](/images/matvecmult.png)

So each row in the result vector is the result of a sum. You take a row from the input matrix and multiply each entry by the matching entry in the input vector, summing the results. My challenge was to speed this up.

First I needed a way to measure how any changes affected the speed of this bit of the program. It ran pretty quickly so I needed a particularly accurate timing mechanism. The [time stamp counter](http://en.wikipedia.org/wiki/Time_Stamp_Counter) in x86 CPUs counts the number of cycles since the CPU was last reset, giving sub-nanosecond accuracy. It's worth noting that modern CPUs can dynamically alter their frequency leading to confusing results. I ran the code 100,000 times and calculated the variance and the mean of the cycle count from these runs to get a handle on the performance.

We use the [Boost uBLAS](http://www.boost.org/doc/libs/1_49_0/libs/numeric/ublas/doc/index.htm) library to manage and perform operations on our data. First I benchmarked [prod](http://www.boost.org/doc/libs/1_49_0/libs/numeric/ublas/doc/matrix_expression.htm#matrix_vector_operations) from uBLAS, it took *47k cycles*.

To get a handle on the problem I tried an initial hand rolled implementation:

<script src="https://gist.github.com/2439238.js?file=gistfile1.cpp"></script>

This ran in *65k cycles* - considerably slower than the uBLAS implementation. Moving to pointer munging:

<script src="https://gist.github.com/2439256.js?file=gistfile1.cpp"></script>

This ran in *47k cycles*, the same as the uBLAS implementation. I imagine pulling out the core data pointers gave the compiler more information than the operator() function calls (although I can't imagine why).

[SSE](http://en.wikipedia.org/wiki/Streaming_SIMD_Extensions) is an extension to the basic x86 instruction set that has been in Pentiums for as long as I've been paying attention. It contains a [range of instructions](http://softpixel.com/~cwright/programming/simd/sse2.php) for doing [DSP](http://en.wikipedia.org/wiki/Digital_signal_processing) type work where the same maths has to be applied again and again across a large set of data. All x86-64 CPUs implement at least SSE2 so I consider it universal. I tried forcing [gcc](http://gcc.gnu.org/) to use SSE2 with the -msse2 flag, but it didn't make much difference. A quick eyeball of the [asm](http://en.wikipedia.org/wiki/Assembly_language) showed that it was now using the XMM registers but it didn't seem to notice that the data could be worked on in parallel.

GCC supports using SSE instructions as function calls called [intrinsics](http://gcc.gnu.org/onlinedocs/gcc-3.1/gcc/Vector-Extensions.html). I tried reimplementing the pointer implementation using these to sum alternate pairs into two different accumulators. At the end of the loop I then added these accumulators to get the result:

<script src="https://gist.github.com/2439312.js?file=gistfile1.cpp"></script>

This ran in *30k cycles*! That's a serious improvement on the uBLAS implementation.

With the help of the website of the fantastic [Eric Bainville](http://www.bealto.com/mp-dot_sse.html) I thought it was worth doing a hand crafted assembly version to squeeze out any last bits of performance. Eric's page shows the general idea but I tidied up the bits he left as an exercise for the reader and embedded it using the fantastic [GCC Inline Assembly](http://ibiblio.org/gferg/ldp/GCC-Inline-Assembly-HOWTO.html).

<script src="https://gist.github.com/2439337.js?file=gistfile1.cpp"></script>

This ran in *29k* cycles. Not much in it. Here I have started to get lazy and hardcode the number of rows (400). I guess extracting that is a further exercise for the reader!

My last throw of the dice was to unroll the loop to try and use more of the SSE machinery. By summing into 4 accumulators and using 4 SSE registers I hope to use more memory bandwidth and make sure the CPU is always fed with data. This remains the most advanced x86 asm I've attempted and I would appreciate any hints on how to improve it. 

<script src="https://gist.github.com/2439378.js?file=gistfile1.cpp"></script>

This ran in *26k cycles*. This is 43% faster than the original uBLAS prod() call. Using this last version in our electricity disaggregation algorithm gave a 23% overall speed boost. Nothing revolutionary, but worth having!

Things to do next:

* Try the unrolled loop with intrinsics. It'll probably be just as fast as my hand crafted version.
* Try using new [AVX](http://en.wikipedia.org/wiki/Advanced_Vector_Extensions) instructions that have 256bit registers, allowing operations on 4 doubles! Unfortunately not all of our hardware supports this so it would have to be switched in depending on the CPU type.
* Link against an optimised blas library such as the [Intel Math Kernel Library](http://software.intel.com/en-us/articles/intel-mkl/). Libraries like this have implemented highly optimised code for every mathematical operation you can think of and I'm sure their matrix vector product code is pretty much optimal.
* Look again at the algorithm to try and find excuses not to actually do these sums!

Overall this work hasn't made a big difference to Navetas software, but I had a fun weekend. For the product release Alex managed to achieve the necessary performance with judicious tweaking of compiler optimisations, but perhaps in the future this experience will prove useful.

Navetas is hiring software engineers and research scientists to solve hard problems with novel maths and intelligent software. Please get in touch with careers@navetas.com if you're interested in getting involved.
