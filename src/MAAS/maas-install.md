Title:MAAS Install

### Navigation

  * [index](http://maas.ubuntu.com/docs/genindex.html)
  * [modules](http://maas.ubuntu.com/docs/py-modindex.html) |
  * [next](http://maas.ubuntu.com/docs/configure.html) |
  * [previous](http://maas.ubuntu.com/docs/changelog.html) |
  * [MAAS 1.5 documentation](http://maas.ubuntu.com/docs/index.html) »

# Installing MAAS

There are two main ways to install MAAS:

* From Ubuntu’s package archive on an existing Ubuntu install.
* As a fresh install from Ubuntu Server install media.
    
If you are interested in testing the latest development version you can also
check out the very latest source and build MAAS yourself.

## Installing MAAS from the archive

Installing MAAS from packages is thankfully straightforward. There are
actually several packages that go into making up a working MAAS install, but
for convenience, many of these have been gathered into a virtual package
called ‘maas’ which will install the necessary components for a ‘seed cloud’,
that is a single server that will directly control a group of nodes. The main
packages are:

* `maas` - seed cloud setup, which includes both the region controller and
the cluster controller below.

* `maas-region-controller` - includes the web UI, API and database.

* `maas-cluster-controller` - controls a group (“cluster”) of nodes
including DHCP management.

* `maas-dhcp`/`maas-dns` - required when managing dhcp/dns.

If you need to separate these services or want to deploy an additional cluster
controller, you should install the corresponding packages individually (see
[_the description of a typical
setup_](http://maas.ubuntu.com/docs/orientation.html#setup) for more
background on how a typical hardware setup might be arranged).

There are two suggested additional packages ‘maas-dhcp’ and ‘maas-dns’. These
set up MAAS-controlled DHCP and DNS services which greatly simplify deployment
if you are running a typical setup where the MAAS controller can run the
network (Note: These **must** be installed if you later set the options in the
web interface to have MAAS manage DHCP/DNS). If you need to integrate your
MAAS setup under an existing DHCP setup, see [_Manual DHCP
configuration_](http://maas.ubuntu.com/docs/configure.html#manual-dhcp)

Note

A more up-to-date MAAS is available for the most recent Ubuntu LTS release in
the Canonical cloud archive. You can activate the archive with `sudo add-apt-
repository cloud-archive:tools`. Using packages from this archive is
recommended as it contains important fixes and new features that are not
always available in the Ubuntu archive.

### Install packages[¶](http://maas.ubuntu.com/docs/install.html#install-
packages)

At the command-line, type:

    
    $ sudo apt-get install maas maas-dhcp maas-dns
    

You will see a list of packages and a confirmation message to proceed. The
exact list will obviously depend on what you already have installed on your
server, but expect to add about 200MB of files.

The configuration for the MAAS controller will automatically run and pop up
this config screen:

![_images/install_cluster-config.png](./Installing MAAS — MAAS 1.5
documentation_files/install_cluster-config.png)

Here you will need to enter the hostname for where the region controller can
be contacted. In many scenarios, you may be running the region controller
(i.e. the web and API interface) from a different network address, for example
where a server has several network interfaces.

Once the configuration scripts have run you should see this message telling
you that the system is ready to use:

![_images/install_controller-config.png](./Installing MAAS — MAAS 1.5
documentation_files/install_controller-config.png)

The web server is started last, so you have to accept this message before the
service is run and you can access the Web interface. Then there are just a few
more setup steps [_Post-Install
tasks_](http://maas.ubuntu.com/docs/install.html#post-install)

## Installing MAAS from Ubuntu Server boot
media[¶](http://maas.ubuntu.com/docs/install.html#installing-maas-from-ubuntu-
server-boot-media)

If you are installing MAAS as part of a fresh install it is easiest to choose
the “Multiple Server install with MAAS” option from the installer and have
pretty much everything set up for you. Boot from the Ubuntu Server media and
you will be greeted with the usual language selection screen:

![_images/install_01.png](./Installing MAAS — MAAS 1.5
documentation_files/install_01.png)

On the next screen, you will see there is an entry in the menu called
“Multiple server install with MAAS”. Use the cursor keys to select this and
then press Enter.

![_images/install_02.png](./Installing MAAS — MAAS 1.5
documentation_files/install_02.png)

The installer then runs through the usual language and keyboard options. Make
your selections using Tab/Cursor keys/Enter to proceed through the install.
The installer will then load various drivers, which may take a moment or two.

![_images/install_03.png](./Installing MAAS — MAAS 1.5
documentation_files/install_03.png)

The next screen asks for the hostname for this server. Choose something
appropriate for your network.

![_images/install_04.png](./Installing MAAS — MAAS 1.5
documentation_files/install_04.png)

Finally we get to the MAAS part! Here there are just two options. We want to
“Create a new MAAS on this server” so go ahead and choose that one.

![_images/install_05.png](./Installing MAAS — MAAS 1.5
documentation_files/install_05.png)

The install now continues as usual. Next you will be prompted to enter a
username. This will be the admin user for the actual server that MAAS will be
running on (not the same as the MAAS admin user!)

![_images/install_06.png](./Installing MAAS — MAAS 1.5
documentation_files/install_06.png)

As usual you will have the chance to encrypt your home directory. Continue to
make selections based on whatever settings suit your usage.

![_images/install_07.png](./Installing MAAS — MAAS 1.5
documentation_files/install_07.png)

After making selections and partitioning storage, the system software will
start to be installed. This part should only take a few minutes.

![_images/install_09.png](./Installing MAAS — MAAS 1.5
documentation_files/install_09.png)

Various packages will now be configured, including the package manager and
update manager. It is important to set these up appropriately so you will
receive timely updates of the MAAS server software, as well as other essential
services that may run on this server.

![_images/install_10.png](./Installing MAAS — MAAS 1.5
documentation_files/install_10.png)

The configuration for MAAS will ask you to configure the host address of the
server. This should be the IP address you will use to connect to the server
(you may have additional interfaces e.g. to run node subnets)

![_images/install_cluster-config.png](./Installing MAAS — MAAS 1.5
documentation_files/install_cluster-config.png)

The next screen will confirm the web address that will be used to the web
interface.

![_images/install_controller-config.png](./Installing MAAS — MAAS 1.5
documentation_files/install_controller-config.png)

After configuring any other packages the installer will finally come to and
end. At this point you should eject the boot media.

![_images/install_14.png](./Installing MAAS — MAAS 1.5
documentation_files/install_14.png)

After restarting, you should be able to login to the new server with the
information you supplied during the install. The MAAS software will run
automatically.

![_images/install_15.png](./Installing MAAS — MAAS 1.5
documentation_files/install_15.png)

**NOTE:** The maas-dhcp and maas-dns packages should be installed by default, but on older releases of MAAS they won’t be. If you want to have MAAS run DHCP and DNS services, you should install these packages. Check whether they are installed with:
    
    $ dpkg -l maas-dhcp maas-dns
    

If they are missing, then:

    
    $ sudo apt-get install maas-dhcp maas-dns
    

And then proceed to the post-install setup below.

# Post-Install tasks[¶](http://maas.ubuntu.com/docs/install.html#post-install-
tasks)

If you now use a web browser to connect to the region controller, you should
see that MAAS is running, but there will also be some errors on the screen:

![_images/install_web-init.png](./Installing MAAS — MAAS 1.5
documentation_files/install_web-init.png)

The on screen messages will tell you that there are no boot images present,
and that you can’t login because there is no admin user.

## Create a superuser
account[¶](http://maas.ubuntu.com/docs/install.html#create-a-superuser-
account)

Once MAAS is installed, you’ll need to create an administrator account:

    
    $ sudo maas createadmin --username=root --email=MYEMAIL@EXAMPLE.COM
    

Substitute your own email address for [MYEMAIL@EXAMPLE.COM](https://mail.googl
e.com/mail/?view=cm&amp;fs=1&amp;tf=1&amp;to=MYEMAIL%40EXAMPLE.COM). You may also use a
different username for your administrator account, but “root” is a common
convention and easy to remember. The command will prompt for a password to
assign to the new user.

You can run this command again for any further administrator accounts you may
wish to create, but you need at least one.

## Import the boot images[¶](http://maas.ubuntu.com/docs/install.html#import-
the-boot-images)

MAAS will check for and download new Ubuntu images once a week. However,
you’ll need to download them manually the first time. To do this you will need
to connect to the MAAS API using the “maas” command-line client. (see
[_Logging in_](http://maas.ubuntu.com/docs/maascli.html#api-key) for details).
Then you need to run the command:

    
    $ maas my-maas-session node-groups import-boot-images
    

(substitute in a different profile name for ‘maas’ if you have called yours
something else) This will initiate downloading the required image files. Note
that this may take some time depending on your network connection.

Note

This API command is only available in MAAS versions 1.3 and above. For lower
versions, you need to run `sudo maas-import-pxe-files` once on each cluster
controller.

## Login to the server[¶](http://maas.ubuntu.com/docs/install.html#login-to-
the-server)

To check that everything is working properly, you should try and login to the
server now. Both the error messages should have gone (it can take a few
minutes for the boot image files to register) and you can see that there are
currently 0 nodes attached to this controller.

![_images/install-login.png](./Installing MAAS — MAAS 1.5 documentation_files
/install-login.png)

## Configure DHCP[¶](http://maas.ubuntu.com/docs/install.html#configure-dhcp)

If you want MAAS to control DHCP, you can either:

  1. Follow the instructions at [_Cluster Configuration_](http://maas.ubuntu.com/docs/cluster-configuration.html) to use the web UI to set up your cluster controller.
  2. Use the command line interface maas by first [_logging in to the API_](http://maas.ubuntu.com/docs/maascli.html#api-key) and then [_following this procedure_](http://maas.ubuntu.com/docs/maascli.html#cli-dhcp)

If you are manually configuring a DHCP server, you should take a look at
[_Manual DHCP configuration_](http://maas.ubuntu.com/docs/configure.html
#manual-dhcp)

## Configure switches on the network[¶](http://maas.ubuntu.com/docs/install.html#configure-switches-on-the-
network)

Some switches use Spanning-Tree Protocol (STP) to negotiate a loop-free path
through a root bridge. While scanning, it can make each port wait up to 50
seconds before data is allowed to be sent on the port. This delay in turn can
cause problems with some applications/protocols such as PXE, DHCP and DNS, of
which MAAS makes extensive use.

To alleviate this problem, you should enable [Portfast](https://www.symantec.c
om/business/support/index?page=content&amp;id=HOWTO6019) for Cisco switches or its
equivalent on other vendor equipment, which enables the ports to come up
almost immediately.

Once everything is set up and running, you are ready to [_start enlisting
nodes_](http://maas.ubuntu.com/docs/nodes.html)

[![MAAS logo](./Installing MAAS — MAAS 1.5 documentation_files/maas-
logo-200.png)](http://maas.ubuntu.com/docs/index.html)



