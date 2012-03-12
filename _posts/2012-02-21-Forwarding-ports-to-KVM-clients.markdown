---
layout: post
title: Forwarding ports to KVM clients
---
If you create a VM under Ubuntu 11.10 using virt-manager the default is for it to use [Usermode Networking](https://help.ubuntu.com/community/KVM/Networking#usermodenetworking). This doesn't require any setup, however the VM gets an IP address on a new subnet (10.0.2.1/24) that isn't available from the outside world - or even from the host!

You can move to [bridged networking](https://help.ubuntu.com/community/KVM/Networking#bridgednetworking) but this requires a fair amount of system configuration work. Another, less well documented, way is to use the redirect functionality built into QEMU.

The [QEMU man page](http://pwet.fr/man/linux/commandes/qemu) specifies -redir as follows:
    -redir [tcp|udp]:host-port:[guest-host]:guest-port
    When using the user mode network stack, redirect incoming TCP or UDP connections to the host port host-port to the guest guest-host on guest port guest-port. If guest-host is not specified, its value is 10.0.2.15 (default address given by the built-in DHCP server). For example, to redirect host X11 connection from screen 1 to guest screen 0, use the following:
    
            # on the host
            qemu -redir tcp:6001::6000 [...]
            # this host xterm should open in the guest X11 server
            xterm -display :1
    
    To redirect telnet connections from host port 5555 to telnet port on the guest, use the following:
    
            # on the host
            qemu -redir tcp:5555::23 [...]
            telnet localhost 5555
    
    Then when you use on the host CWtelnet localhost 5555, you connect to the guest telnet server.

To use this with a virt-manager created virtual machine you need to manually edit the VM Config (I'm using QEMU usermode to manage my VMs so I have to specify a special connection string):
    virsh --connect qemu:///session edit Windows

You then have to specify that this domain will use extra commands from a special namespace, so change the top <domain> attribute from:
    <domain type='kvm'>
to:
    <domain type='kvm' xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0'>

Then add a some override parameters to be passed straight through to the QEMU command line. Here I'm forwarding port 1234 on the host to port 3389 on the VM (make this block immediately under the <domain> node):
    <qemu:commandline>
        <qemu:arg value='-redir'/>
        <qemu:arg value='tcp:1234::3389'/>
    </qemu:commandline>

Save these changes, exit the editor and then start up the VM. You should be able to connect to localhost:1234 and be plumbed through to port 3389 on the VM.
