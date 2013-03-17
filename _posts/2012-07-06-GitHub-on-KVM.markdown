---
layout: post
title: GitHub on KVM
---
[GitHub Enterprise](https://enterprise.github.com) is a version of GitHub that you can run locally on a company network. It comes as a virtual machine image in [Open Virtualization Format](http://en.wikipedia.org/wiki/Open_Virtualization_Format) and GitHub support it running on the VirtualBox and VMWare hypervisors. At [Navetas](http://www.navetas.com) we use the [KVM](http://www.linux-kvm.org) hypervisor so I have recently been looking at how to convert the GitHub Enterprise VM image to run under KVM.

1. [Download](https://enterprise.github.com/download) the GitHub Enterprise VM Image in Open Virtualization Archive (.ova) format.
1. Extract the contents of the archive with:
        tar -xf github-enterprise-11.10.270-i386.ova
    This will give you a set of files:
    * github-enterprise-11.10.270-i386-disk1.vmdk - The disk image
    * github-enterprise-11.10.270-i386.ovf - An XML description of the virtual machine
    * github-enterprise-11.10.270-i386.mf - Hashes of the other two files
1. Install [VMWare Workstation](http://www.vmware.com/products/workstation/overview.html) to get the vmware-vdiskmanager tool.
1. Convert the GitHub disk image to use a preallocated virtual disk (watch out - this file will be 10GB!):
        vmware-vdiskmanager -r github-enterprise-11.10.270-i386-disk1.vmdk -t 2 github-enterprise-11.10.270-i386-disk1-preallocated.vmdk
1. Convert the preallocated VMWare disk image to qcow2 format with qemu-img:
        qemu-img convert -O qcow2 github-enterprise-11.10.270-i386-disk1-preallocated-flat.vmdk github-enterprise-11.10.270-i386-disk1-preallocated-flat.qcow2
1. You can now create a KVM virtual machine using the generated qcow2 disk image as a boot disk!

It's worth noting that GitHub *do not* support running GitHub Enterprise under the KVM hypervisor.

### Expanding Disk Image (added 2012/07/20)
The disk image can also be converted to RAW format with qemu-img, and then written directly to an LVM volume (using dd), then the virtual machine can boot off that. If more space is required in the GitHub machine then you can:

1. Copy the 10GB RAW image into a Volume Group that is bigger - say 100GB
1. Boot up GitHub & log in with SSH
1. Run ghe-grow-root -d /dev/vda6

This should make GitHub all the available disk space.
