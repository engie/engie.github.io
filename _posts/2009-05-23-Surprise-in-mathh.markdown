---
layout: post
title: Surprise in math.h
---
<p>Quick Quiz: What does the following code output:</p><pre>
#include &lt;math.h&gt;
#include &lt;stdint.h&gt;
#include &lt;stdio.h&gt;

int main(int argc, char **argv)
{
    int i = INT32_MIN;
    printf("i is: %d\n", i);
    printf("abs(i) is: %d\n", abs(i));
}
</pre><p>Select the following to see the result...</p><pre style="color: blue; background-color: blue;">stephen@frank:/tmp$ gcc test.c -o test
stephen@frank:/tmp$ ./test 
i is: -2147483648
abs(i) is: -2147483648
</pre><p>Woah! This comes from the 2s complement representation of INT32_MIN. It's 1 followed by all zeros. When abs() does the standard invert-all-bits-then-add-one technique for turning a negative into a positive it turns INT32_MIN into... INT32_MIN!</p><p>Thanks to <a href="http://www.youtube.com/watch?v=wDN_EYUvUq0">http://www.youtube.com/watch?v=wDN_EYUvUq0</a></p><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/6550447907550133610-1735034187236469942?l=www.secomputing.co.uk' alt='' /></div>