---
layout: post
title: Getting xinerama screen size info with Python
---
Looking at <a href="http://elisa.fluendo.com/">elisa</a> - amazing stuff, but it doesn't behave too nicely on my dual head machine.  Have developed some Python to find xinerama screen sizes based on the work done by <a href="http://code.google.com/p/pyglet/">pyglet</a>.

Next step is integrating this into elisa.

From PyGlet, under the <a href="http://www.opensource.org/licenses/bsd-license.php">new BSD license</a>.

<pre>
from ctypes import *
from ctypes import util
import sys

path = util.find_library('X11')
if not path:
    raise ImportError("Could not load xlib")

xlib = cdll.LoadLibrary(path)

Display = c_void_p
xlib.XOpenDisplay.argtypes = [c_char_p]
xlib.XOpenDisplay.restype = POINTER(Display)

path = util.find_library('Xinerama')
if not path:
    raise ImportError("Could not load xinerama")

xinerama = cdll.LoadLibrary(path)

class XineramaScreenInfo(Structure):
    _fields_ = [
    ('screen_number', c_int),
    ('x_org', c_short),
    ('y_org', c_short),
    ('width', c_short),
    ('height', c_short)
    ]
xinerama.XineramaQueryScreens.restype = POINTER(XineramaScreenInfo)

if len(sys.argv) > 1 and type(sys.argv[1]) in (str, unicode):
    d = xlib.XOpenDisplay(sys.argv[1])
else:
    d = xlib.XOpenDisplay("")

if not d:
    raise Exception("Could not open display")

if not xinerama.XineramaIsActive(d):
    raise Exception("Xinerama not active")

number = c_int()
infos = xinerama.XineramaQueryScreens(d, byref(number))
infos = cast(infos, POINTER(XineramaScreenInfo * number.value)).contents

for info in infos:
    print "Screen %d - pos=%d,%d size=%d,%d" % (
                                info.screen_number,
                                info.x_org,
                                info.y_org,
                                info.width,
                                info.height)
                                

xlib.XFree(infos)
</pre><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/6550447907550133610-4767707656408424047?l=www.secomputing.co.uk' alt='' /></div>