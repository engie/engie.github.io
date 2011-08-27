---
layout: post
title: DigiKey Price Parser
---
<p>Needed to hit DigiKey to look up a load of prices, sooo...
<pre>
#!/usr/bin/env python
import urllib2
from BeautifulSoup import BeautifulSoup
import sys

id = sys.argv[1]
if len(sys.argv) > 2:
    need = int(sys.argv[2])
else:
    need = 1
    
page = urllib2.urlopen( \
"http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail?name=" + id)

soup = BeautifulSoup(page)

pricetable = soup.find('table', frame='void')
prices = pricetable.findChildren('tr')[1:]
for price in prices:
    quantity = price.first('td')
    if int(quantity.contents[0]) > need:
        cost = quantity.nextSibling
        print cost.contents[0]
        break
</pre></p><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/6550447907550133610-3989096668561326537?l=www.secomputing.co.uk' alt='' /></div>