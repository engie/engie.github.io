---
layout: post
title: How should I share my key?
---
<p>What's the best way of sharing my gpg public key? A public key can be used to send &amp; receive encrypted and signed email, but it's only useful if your friends have a copy. If you know it has a keyid of B7200FD3, then you can search for it on the global key directories (for example in the <a href="https://keyserver2.pgp.com/vkd/DownloadKey.event?keyid=0x0A047B7DB7200FD3">PGP Global Directory</a>) and download it from there. Or, you could get it here:</p><pre>-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.10 (GNU/Linux)

mQGiBEYUNRQRBADqhl/h9sZ7x0Ms7dWnTHy4sGROzh3wPMdzQNiHQ7bCPdMkhAcL
XOMpt40s4jKsrVS5RA9laQONkbhbRs/A7ENzbVCVv49D7TP0y8em2SzOrb6uefEt
iztH1vhWS5tngNA6t/CHyk9ulaX3FMjZkMo/sQVHx5vLlNMPnTpfnThtswCg5ZdO
n0gTp3Mg2h5PAWWBrv0s0oMEAOjBeENBcqAC2eLElH4u7DBsbTIboodfEbUb3F1h
3Vj+ca3YbOu0dvzFhM3spXMxsCTXcWqyWAamGog0xE5yjGX6EufPZnyR3OfV7Dgs
lkKuw4Xl43Kr77LvEpfSxcJYAlmj0qTwlhKBJ9bBAld8BqGRLxzQdOuZtGOwwa57
ddOKA/4yBJSQEDOGdZN+ZUdnBm3ptpy22nTJhrb3XO8imrXZU5vP007+tudeSrSC
SqBcERcXrme4qLxcDZ3hbG/X6/xQHbe1Au+9IrRFTgBfzQplGHJlEk+CoNVqhHbQ
BME0Dkcb7WttwU9cs2WLspIiBlwx9D4695CcJPlR4VMwXh9Nr7QpU3RlcGhlbiBF
bmdsaXNoIDxzdGV2ZUBzZWNvbXB1dGluZy5jby51az6IYAQTEQIAIAUCRhQ1FAIb
IwYLCQgHAwIEFQIIAwQWAgMBAh4BAheAAAoJEAoEe323IA/TwwQAoNV7BXqqfKVT
37F1ftFd5IB+C66zAKCQB7VqngfN9KwPN2Cn4iD/uernRrkCDQRGFDUZEAgA4ByL
jOWVs8IhmFtd7rUQDF2vW3QjNtgZ5zMm/iPG9pQS76bqAtdGaN7bwd9hkqlo7c4B
fXjbB0LyU35lKJVJcsbKOZB568Z2OJn57jSSEtxnq7PE3MTDxy6UpKxfacV5mpDp
sZEQU6z36y02rHj/uEVICOQ5jr5WiRd6ZK++6igyJ7RLtO4MnizNRD9/L9hmrtit
NTPZxj1lDxYyGRaoLCVqUA2rZY5uZLIEygxtQwjCpY2FYRoxdJ+BHT9X9JzBVQ04
J/UKqBR4OonTNqXQSXaey2h6WwDiGWqDpDaIwa06ja0G4vQvo/Kg6SwAekT8a6tq
bEnkUJ7KGMLLkm+rvwADBQgApmvYw0ReNZoY/5lRLKQdH0gJJMehhV1lMiKZgjqD
sRzL2TYvvAiFdlfSVyMa0Gjrvg2BesMaZD943zpGvuB4kVcJJ6SNAPUWNLNRH1gN
7FAEb1Z+u1CTEjjPXPtbE+h+OWHhzRgsgWMvy5GzEWtRb21w/PTq5AA8UbnsM8me
GKXTleP3qMDEVkmbBHYsBd4EGAC3RfrHJS/8QXDwDgsHco/GxmasMg7Gef8s97/r
Dm3ZM+5KDAnQScNFZCbhGakT67abswJk4Urs7bldJeWkV04FvM1Bj8j10VxQKH3/
TCLzAQjZB0ZZnqyDuBLbKnCo4d2+Zel2nkZZ1A3JrbKdxYhJBBgRAgAJBQJGFDUZ
AhsMAAoJEAoEe323IA/TDjsAn1g4JLc73Jiug9NzIVZKICWRoT2eAJ4lPDScIdGZ
OmwKFEZVMVg+J8DmGg==
=HxzW
-----END PGP PUBLIC KEY BLOCK-----</pre>
<p>Both the keyId and the full key are a bit of a pain to share, too much text that has to be entered perfectly - this is something a computer should do for us. How about encoding the data in an image?</p><p>I've hacked up the qrencode utility (https://github.com/engie/libqrencode-patches) to allow it to generate QR Codes, 2D barcodes, for binary blobs and the result is a rather large image:</p><p><img style="display:block; margin:0px auto 10px; text-align:center;cursor:pointer; cursor:hand;width: 320px; height: 320px;" src="http://3.bp.blogspot.com/_BamEf6W6pns/TTtmEgFvg-I/AAAAAAAAAR8/9kJWTq3psu8/s320/out-l.png" border="0" alt="" id="BLOGGER_PHOTO_ID_5565153992065909730" /></p><p>I can <i>just about</i> read this using the Barcode Scanner app on my phone (not that it knows what to do with it) but it's rather unwieldy, and I'm not convinced it'll look any good on a TShirt. The KeyID is far more suitable for encoding in an image, but it lacks context. How about encoding a URL to the key? The MIT keyserver can be accessed at URLs like <a href="http://pgp.mit.edu:11371/pks/lookup?search=0xB7200FD3">http://pgp.mit.edu:11371/pks/lookup?search=0xB7200FD3</a> which is a start. How about something sexier? http://gpgkey.org/B7200FD3:</p><p><img style="display:block; margin:0px auto 10px; text-align:center;cursor:pointer; cursor:hand;width: 120px; height: 120px;" src="http://chart.apis.google.com/chart?cht=qr&amp;chs=120x120&amp;chl=http%3A%2F%2Fgpgkey.org%2FB7200FD3" border="0" alt="" /></p><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/6550447907550133610-1686162077869645128?l=www.secomputing.co.uk' alt='' /></div>