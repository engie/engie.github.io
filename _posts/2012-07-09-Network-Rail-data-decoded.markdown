---
layout: post
title: Network Rail data decoded
---
Network Rail have recently released [a set of data feeds](https://datafeeds.networkrail.co.uk). These give free access to:

 * Train movements - Where the trains are
 * Train describer - The Return Of The Train Locations
 * VSTP - Very Short Term Planning - Short term schedule updates
 * RTPPM - Public Performance Measure - How the trains are meeting up with their deadlines
 * TSR - Temporary Speed Restrictions - Current speed restrictions in place
 * SCHEDULE - The train schedule

These are free to use for open source and commercial applications. I'm looking at the movement information with the goal of building up an understanding of where all the trains are, right now.

Updates are streamed from the server at a decent rate but it's not that well documented. I'm trying to collate information on the contents of the fields here as I understand it. Please feel free to [fork this page on GitHub](https://github.com/engie/engie.github.com/fork_select) to add information, or email information to steve@secomputing.co.uk and I'll add it.
