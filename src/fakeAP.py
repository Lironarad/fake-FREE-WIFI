import os
import signal
import time


dnsmasq_conf = "conf/dnsmasq.conf"
hostapd_conf = "conf/hostapd.conf"
website_files = "html" #The folder of website


ap_iface = ""
stop = ""

def start_apache():
	os.system("cp " + website_files + "/* /var/www/html/")
	os.system("service apache2 restart")
	os.system("service apache2 start")

def airmon_check_kill():
	os.system("airmon-ng check kill")

def kill_dnsmasq_and_hostapd():
	os.system("killall dnsmasq hostapd")

def start_dnsmasq():
	os.system("dnsmasq -C " + dnsmasq_conf)
def set_ip():
	global ap_iface
	ap_iface = "wlan1"
	print "You choice " + ap_iface
def ip_table():
	os.system("iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE")
	os.system("iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT")
	os.system("iptables -A FORWARD -i " + ap_iface + " -o eth0 -j ACCEPT")
	os.system("sysctl -w net.ipv4.ip_forward=1")


def restart_network():
	os.system("service network-manager restart")	

def start():
	print("\npress 'CTRL + C'  twice to stop\n")
	while True:
        	try:
               		time.sleep(1)
			os.system("hostapd " + hostapd_conf)
		except KeyboardInterrupt:
			break
	print "\n\nstoping...\n"
	restart_network()

#*****************************************************************************************************************#
start_apache()
airmon_check_kill()
kill_dnsmasq_and_hostapd()
start_dnsmasq()
set_ip()
ip_table()
start()

