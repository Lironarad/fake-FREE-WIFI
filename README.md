# free fake AP

This project demonstrate a fake free wifi access point.
the user how connect to this AP in ip 10.0.0.1 will get a login page that ask for an email and password.
the program will catch the emails adrass and passwords that the users fill in and print them to terminal in the end of the running.

### Prerequisites

To run this progam you will need:
1. kali linux os
2. python
3. 2 wifi adapters

to clone the project to your local machine:
```
git clone https://github.com/Lironarad/fake_FREE-WIFI.git
```

### Installing an running the program
IMPORTENT!!!
before running the program you masr enter your wireless interface name in some configuration files.
you can find it using the command
```
iwconfig
```
write your wirless interface name in the following files:

in the conf directory:
1. dnsmasq.conf - line 1.
2. hostapd.conf - line 1.

in the src directory:
fakeAP.py - line 29.

From the project directory on your local machine, write the following command in the terminal:

```
sudo python main.py
```
The firstline in the program will ask you if you want to install First Time Wizard Install, in the first runinng session you must answer 'Y' to get the AP up and running.

```
Do you want to do First Time Wizard Install? [Y/n]
```
the program then install some tools to  cuild the fake AP, we will give a short brif about this tools here:

1. apache2:
	Apache is the most commonly used Web server on Linux systems. Web servers are used to serve Web pages requested by client computers.
	(from: https://help.ubuntu.com/lts/serverguide/httpd.html)

2. hostapd:
	hostapd is a user space daemon for access point and authentication servers. It implements IEEE 802.11 access point management, IEEE 802.1X/WPA/WPA2/EAP Authenticators, RADIUS client, EAP server, and RADIUS authentication server.
(from: https://w1.fi/hostapd/)

3. dnsmasq:
	Dnsmasq provides network infrastructure for small networks: DNS, DHCP, router advertisement and network boot.
	(from: http://www.thekelleys.org.uk/dnsmasq/doc.html)

when the program is running you shold see a screen such:

```
reportfilename: ./report.xml
tcpflow: listening on any

Killing these processes:

  PID Name
11057 wpa_supplicant

hostapd: no process found
You choice wlan1
net.ipv4.ip_forward = 1

press 'CTRL + C'  twice to stop

Configuration file: conf/hostapd.conf
Using interface wlan1 with hwaddr 5a:61:e5:0a:31:cb and ssid "FREE-WIFI"
wlan1: interface state UNINITIALIZED->ENABLED
wlan1: AP-ENABLED 
^Ctcpflow: terminating orderly
wlan1: interface state ENABLED->DISABLED
wlan1: AP-DISABLED 
wlan1: CTRL-EVENT-TERMINATING 
nl80211: deinit ifname=wlan1 disabled_11b_rates=0
```
when clients connect to the AP you will see details about the connection:

```
wlan1: STA 76:df:fb:3f:2e:d8 IEEE 802.11: authenticated
wlan1: STA 76:df:fb:3f:2e:d8 IEEE 802.11: associated (aid 1)
wlan1: AP-STA-CONNECTED 76:df:fb:3f:2e:d8
wlan1: STA 76:df:fb:3f:2e:d8 RADIUS: starting accounting session A3B6FF4C5CEDFCAD
```
To stop the program press 'CTRL + C'  twice.
when the program finished all the email adresses and passwords will print out to the terminal.

```

stoping...



*************** passwords captured: ***************

mail=user%40gmail.co&password=user_password
```






