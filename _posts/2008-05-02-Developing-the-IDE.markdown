---
layout: post
title: Developing the IDE
---
The IDE needs work. It's currently based on <a href="http://turbogears.org/">Turbogears</a> and it uses <a href="http://pysvn.tigris.org/">pysvn</a> to store the code. <a href="http://www.cdolivet.net/editarea/">Editarea</a> does the honors of syntax highlighting the Python code and the bulk of the Javascript is based on the <a href="http://mochikit.com/">Mochikit</a> library.

Currently the backend code is... OK.  We need to move from pysvn to the standard svn bindings as pysvn is full of memory leaks/kills the garbage collector/leaves us in a world of pain. That's a pretty major change, but it shouldn't be too bad.

On the frontend we need to increase reliability by having sensible failure modes (away from the current "Please Refresh and Lose Your Work" error message thrown up by any failure) and the edit area component needs upgrading to show the indentation levels better. Also the latest editarea supports tabbing which may be better than the current home grown one.

Overall, not too bad - the excitement is going to be integrating the simulator :D<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/6550447907550133610-6600401513746835294?l=www.secomputing.co.uk' alt='' /></div>