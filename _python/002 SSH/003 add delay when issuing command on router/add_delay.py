#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# Netmiko is the same as ConnectHandler
from netmiko import Netmiko

device = {
    "host": "192.168.57.3",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
    # Increase (essentially) all sleeps by a factor of 2
    "global_delay_factor": 2,
}

net_connect = Netmiko(**device)
# Increase the sleeps for just send_command by a factor of 2
output = net_connect.send_command("show ip int brief", delay_factor=2)
print(output)
net_connect.disconnect()