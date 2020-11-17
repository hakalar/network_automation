from __future__ import print_function
from netmiko import ConnectHandler
import pandas as pd

# This gives an output of BGP neighbor if it is down:
# example:
# Neighbor 10.0.11.101 is down
# Neighbor 10.0.10.103 is down


import sys
import time
import select
import paramiko
import re
status = open(r'E:\\Python-Scripts\\bgp-status.txt','w')
old_stdout = sys.stdout
sys.stdout = status
host = '10.0.10.100'
platform = 'cisco_ios'
username = 'javed'
password = 'cisco'
device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
output = device.send_command('terminal length 0')
output = device.send_command('enable')
bgp_status = device.send_command('show ip bgp summary | be N')


for neighbor_status in bgp_status.split('\n'):
    if 'down' in neighbor_status:
        print(f"{neighbor_status} is down")
    else:
        print('All neighbors are up')
        break
status.close()


# data = pd.read_csv('E:\\Python-Scripts\\bgp-status.txt', delim_whitespace=True , header=None)
# # for index, row in data.iterrows():
# #     if row[8] == 'Down':
# #         print (f"Neighbor {row[0]} is down")
# #     else:
# #         pass

# 'Neigbour: '+df['Neighbor']+' is '+df['Up/Down'].replace('.*\\d:.*','Up',regex=True)