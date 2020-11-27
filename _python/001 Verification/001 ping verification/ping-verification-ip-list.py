import os

ip_list = ["8.8.8.8", "192.168.57.3"]
for ip in ip_list:
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        print({ip}, 'is up!')
    else:
        print({ip}, 'is down!')
