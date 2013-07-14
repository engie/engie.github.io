---
layout: post
title: Escalator
---
At [Navetas](http://www.navetas.com) we're enjoying great success using the new features in [C++11](https://en.wikipedia.org/wiki/C%2B%2B11). Lambda's are probably the office favourite but range based loops, initializer lists, auto and the rest are being brought to bear to write high performance C++ that reads like Scala.

We do a lot of data processing, crunching through data structures filled with electrical measurements, and we've found that the [Scala Collections API](http://docs.scala-lang.org/overviews/core/architecture-of-scala-collections.html) leads to beautiful, elegant code. We want the same but faster, so we have put together and released the [Escalator](https://github.com/Navetas/Escalator) library to bring the spirit of the Scala Collections API to C++.

It's early days yet but we're already using the Escalator library in our main product codebase to great effect. Here's an example:

<script src="https://gist.github.com/engie/5994390.js"></script>

You can also lift mutable collections, infinite streams and collections of non-copyables. The API isn't fixed yet but we're definitely open to pull requests!

It's been great fun, and a real learning experience, working on this with [Alex Wilson](https://github.com/d40cht/). Thanks Alex!
