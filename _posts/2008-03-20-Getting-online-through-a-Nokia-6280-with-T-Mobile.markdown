---
layout: post
title: Getting online through a Nokia 6280 with T-Mobile
---
Some settings I use:
<pre>
cat /etc/chatscripts/ppp0
TIMEOUT 60 
ABORT ERROR 
ABORT BUSY 
ABORT VOICE 
ABORT "NO CARRIER" 
ABORT "NO DIALTONE" 
ABORT "NO DIAL TONE" 
ABORT "NO ANSWER" 
"" "ATZ" 
"OK" "ATQ0L3 V1 E1 S0=0 &C1 &D2 +FCLASS=0" 
OK-AT-OK "ATM1L3DT*99#" 
TIMEOUT 75 
CONNECT

stephen@sam:~$ cat /etc/ppp/peers/ppp0 
connect "/usr/sbin/chat -v -f /etc/chatscripts/ppp0"
usepeerdns

/dev/rfcomm0
115200
user "user"
defaultroute

persist

stephen@sam:~$ cat /etc/ppp/peers/provider 
# example configuration for a dialup connection authenticated with PAP or CHAP
#
# This is the default configuration used by pon(1) and poff(1).
# See the manual page pppd(8) for information on all the options.

# MUST CHANGE: replace myusername@realm with the PPP login name given to
# your by your provider.
# There should be a matching entry with the password in /etc/ppp/pap-secrets
# and/or /etc/ppp/chap-secrets.
user "myusername@realm"

# MUST CHANGE: replace ******** with the phone number of your provider.
# The /etc/chatscripts/pap chat script may be modified to change the
# modem initialization string.
connect "/usr/sbin/chat -v -f /etc/chatscripts/pap -T ********"

# Serial device to which the modem is connected.
/dev/modem

# Speed of the serial line.
115200

# Assumes that your IP address is allocated dynamically by the ISP.
noipdefault
# Try to get the name server addresses from the ISP.
usepeerdns
# Use this connection as the default route.
defaultroute

# Makes pppd "dial again" when the connection is lost.
persist

# Do not ask the remote to authenticate.
noauth

#
# RFCOMM configuration file.
#

rfcomm0 {
#       # Automatically bind the device at startup
        bind yes;
#
#       # Bluetooth address of the device
        device 00:17:4B:6E:9C:A5;
#
#       # RFCOMM channel for the connection
        channel 1;
#
#       # Description of the connection
        comment "Nokia";
}
</pre>

I think that's it!<div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/6550447907550133610-6123009818208735929?l=www.secomputing.co.uk' alt='' /></div>