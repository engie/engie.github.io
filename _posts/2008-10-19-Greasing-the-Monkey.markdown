---
layout: post
title: Greasing the Monkey
---
Just wrote my first <a href="https://addons.mozilla.org/en-US/firefox/addon/748">Greasemonkey</a> script to help out an old friend. The script (<a href="http://userscripts.org/scripts/show/35685">http://userscripts.org/scripts/show/35685</a>) adds links to BBC Radio schedules (e.g. <a href="http://www.bbc.co.uk/radio7/programmes/schedules">http://www.bbc.co.uk/radio7/programmes/schedules</a>) where you can download the Realplayer version of a show that's on IPlayer.

<a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="http://2.bp.blogspot.com/_BamEf6W6pns/SPr1ueqsQ7I/AAAAAAAAAFQ/Q56X-BtwOwE/s1600-h/UserScript.png"><img style="display:block; margin:0px auto 10px; text-align:center;cursor:pointer; cursor:hand;" src="http://2.bp.blogspot.com/_BamEf6W6pns/SPr1ueqsQ7I/AAAAAAAAAFQ/Q56X-BtwOwE/s320/UserScript.png" border="0" alt=""id="BLOGGER_PHOTO_ID_5258785693763388338" /></a>

I was quite impressed by how easy putting together a Greasemonkey script was. Unfortunately there seems to be a limit to how many GM_xmlhttpRequest functions you can fire off (seems to be about 5). As I need to hit a second page to find each RealPlayer link, this limit  means I can't get the links for all shows on a schedule when the page loads.<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/6550447907550133610-1461254638625416808?l=www.secomputing.co.uk' alt='' /></div>