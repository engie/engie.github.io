---
layout: post
title: Stephen's First Parser!
---
<p>Basic parsing of generic HDL statements implemented for beginnings of developing a behavioural synthesis tool for Digital Systems Synthesis coursework.
<pre>
stephen@frank:~/work/dss$ cat input.txt
a <= 1 + 2; #Simple assignment
a <= 2 * 3;
a <= 2 * (3 + 4);
a <= 2 * 3 + 2 * 3 + 4; #Compound assignment
a <= 2 * a;
a <= 3 * a;
a <= a + b * 2;
stephen@frank:~/work/dss$ python parse.py input.txt
Register: a <= (1 + 2)
Register: a <= (2 * 3)
Register: a <= (2 * (3 + 4))
Register: a <= ((2 * 3) + ((2 * 3) + 4))
Register: a <= (2 * Register: a)
Register: a <= (3 * Register: a)
Register: a <= (Register: a + (Register: b * 2))
Symbol list:  {'a': Register: a, 'b': Register: b}</pre></p><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/6550447907550133610-4273817263540000844?l=www.secomputing.co.uk' alt='' /></div>