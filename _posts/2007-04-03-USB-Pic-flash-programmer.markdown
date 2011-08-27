---
layout: post
title: USB Pic flash programmer
---
<h2>The Goal</h2>
<p>To program a 15bit parrallel address and data flash chip over USB for use in my third year project.</p>
<h2>The Solution</h2>
<p>Use a Microchip Pic 18F4550 for USB access and control and hook it into a Am29F010B flash chip which has internal charge pumps to make the electrical supply side really easy - and that's it!  To make it easy to use with standard PC software the PIC appears as a CDC serial device (based on the Microchip MCHPUSB firmware) and you transfer files to it using XModem.</p>
<a href="http://www.flickr.com/photos/stephenenglish/444910656/" title="Photo Sharing"><img src="http://farm1.static.flickr.com/192/444910656_c06f0c0732.jpg" width="500" height="446" alt="18F4550 Flash programmer schematic" /></a>
<a href="http://www.flickr.com/photos/stephenenglish/444908293/" title="Photo Sharing"><img src="http://farm1.static.flickr.com/179/444908293_d9f21b9f1e.jpg" width="500" height="375" alt="USB Pic flash programmer" /></a>
<h2>Download</h2>
<p>The code which is running on the PIC is available <a href="http://stephen.english.googlepages.com/flashpic.tar.gz">here.</a>  To use it, assemble the circuit then compile that code with the Microchip C18 compiler. Download the code into the PIC then plug the USB from the PIC into a PC.  If the PC runs windows use the MCHPUSB drivers available from Microchip. For linux it is very important to prevent the cdc-acm driver from loading as it bombs out constantly (add blacklist cdc-acm to /etc/modprobe.d/blacklist). Instead, load the usbserial driver with:<pre>modprobe usbserial vendor=0x04d8 product=0x000a</pre> (as root).

EDIT: This appears no longer necessary with Ubuntu 7.10

Then connect to the device with Hyperterminal, Minicom, Kermit etc.</p>
<p>Once connected to the device with a serial link, characters sent to the PIC will be passed on out of the Rx/Tx serial port of the PIC (this is to provide a terminal connection to the embedded computer in my third year project.) To initiate a file transfer to the pic, type DL then start an XModem transfer. To receive data from the PIC, type DS then start an XModem receive. When receiving data, you will always get a complete dump of the RAM (64K) - if necessary, the data will be padded with 0xFF. If nothing works, adding <pre>#define FLASH_DEBUG</pre> to user.c will cause many debug messages to be put out of the PICs normal serial port - use a MAX233 or similiar to level shift this data up to PC serial port compatible levels.</p>
<h2>Thanks</h2>
<p>I would like to thank:<ul><li><a href="http://www.microchip.com">Microchip</a> for sending me the PIC on sample.</li><li><a href="http://www.electronicfr.com/usb.html">electronicfr.com</a> for a great schematic for basic 18F4550 PIC operation.</li><li><a href="http://www.warrantyvoidifremoved.com/">Jeff</a> for lending me his PIC programmer when mine died!</li></ul></p><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/6550447907550133610-2183986005324196575?l=www.secomputing.co.uk' alt='' /></div>