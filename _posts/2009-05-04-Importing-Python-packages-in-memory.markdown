---
layout: post
title: Importing Python packages in-memory
---
<p><a href="http://www.studentrobotics.org">Student Robotics</a> needs to import python packages written by the students into a simulator. Currently the simulator downloads a ZIP of the python package to the temp directory, then uses the inherent ability of python to transparently treat a zip file as a package to import the code. This has caused us problems, mainly as some schools <b>don't allow students to write to %TEMP%!!!</b></p><p>We are now planning to run the simulator as a web service - Students will save their code in an online IDE and then request a simulation to be run. A physics engine will be plugged in, and some nifty Javascript used to draw a little virtual robot driving around a virtual arena. This means that we (Student Robotics) are running untrusted code on our servers <em>by design</em>. In order to carefully manage our sanity we will be running the students code in its own process as a severely crippled user. This includes banning writing to disk.</p><p>We can't use the standard python zip imports as the zipfile module only supports opening files directly off disk. I have implemented some <a href="http://www.python.org/dev/peps/pep-0302/">import hooks</a> to add the ability to import files from a zip file held in memory. Exceptions aren't handled, that's up to the caller.</p><p>EDIT: Compile before exec so I can set the filename of the code object correctly.</p><pre>
import zipfile, StringIO, imp, sys, os.path

f = StringIO.StringIO()
f.write(open("robot.zip", "rb").read())

zip = zipfile.ZipFile(f)

modules = dict([(os.path.splitext(z.filename)[0], zip.open(z.filename).read())
                    for z in zip. infolist() \
                    if os.path.splitext(z.filename)[1] == ".py"])

class Loader:
    def __init__(self, fullname, contents):
        self.fullname = fullname
        self.contents = contents

    def load_module(self, fullname):
        if fullname in sys.modules:
            return sys.modules[fullname]

        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = "<%s>" % fullname
        mod.__loader__ = self

        code = compile(self.contents, mod.__file__, "exec")

        exec code in mod.__dict__
        return mod

class Finder:
    def __init__(self, modules):
        self.modules = modules

    def find_module(self, fullname, path=None):
        if (fullname in self.modules) and (path == None):
            return Loader(fullname, self.modules[fullname])

        return None

sys.meta_path.append(Finder(modules))

def trace(frame, event, arg):
    if event == "call":
        print frame.f_code.co_filename
    return None

sys.settrace(trace)

print "**************************"

import robot

f = robot.Face()
f.cheese()
f.bee()
</pre><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/6550447907550133610-673288436435250856?l=www.secomputing.co.uk' alt='' /></div>