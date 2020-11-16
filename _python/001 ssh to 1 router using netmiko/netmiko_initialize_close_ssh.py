#!/usr/bin/env python
from netmiko import Netmiko

device = {
    "host": "192.168.57.5",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
}

net_connect = Netmiko(**device)
command = "show ip int brief"

print()
print(net_connect.find_prompt())
output = net_connect.send_command(command)
net_connect.disconnect()
print(output)
print()