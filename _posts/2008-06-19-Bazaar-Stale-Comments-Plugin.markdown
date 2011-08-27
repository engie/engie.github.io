---
layout: post
title: Bazaar Stale Comments Plugin
---
<p>I find myself regularly coming across comments on code, that I have written, that are cripplingly misleading and this is almost always due to them becoming stale over time. Comments become stale if the code they are describing is changed without the comment being updated, something I am often guilty of.</p><p>To try and reduce the impact of this I have started implementing a plugin for the <a href="http://bazaar-vcs.org/">Bazaar</a> version control system that runs when I try to make a commit. The goal is to have it look through changed files for comments and docstrings, and if these comments are marked as valid for an old revision check to see if the code they relate to has changed - if it has fail the commit.</p><p>The current version is pretty limited and can only cope with docstrings of the form:
<pre>
def greeting():
    """RevNo: 12
    Say hi to everyone.
    """
    print "Hello World"
</pre></p>
<p>If there is a change to that function in a revision later than 12 the plugin will fail the commit.
</p><p>I am having a go with hosting the code on <a href="http://launchpad.net">launchpad</a> under the name <a href="https://launchpad.net/bzr-stale-comments">Stale Comments Plugin</a></p><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/6550447907550133610-163392878270416876?l=www.secomputing.co.uk' alt='' /></div>