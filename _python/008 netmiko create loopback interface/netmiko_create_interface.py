#! /usr/bin/env python

from netmiko import ConnectHandler
from device_info import cisco_csr1kv_1 as device

# New Loopback Details
loopback = {"int_name": "Loopback1",
            "description": "Demo interface by CLI and netmiko",
            "ip": "192.168.103.1",
            "netmask": "255.255.255.0"}

# Create a CLI configuration
interface_config = [
    "interface {}".format(loopback["int_name"]),
    "description {}".format(loopback["description"]),
    "ip address {} {}".format(loopback["ip"], loopback["netmask"]),
    "no shut"
]

# Open CLI connection to device
with ConnectHandler(ip = device["host"],
                    port = device["port"],
                    username = device["username"],
                    password = device["password"],
                    device_type = device["device_type"]) as ch:

    # Send configuration to device
    output = ch.send_config_set(interface_config)

    # Print the raw command output to the screen
    print("The following configuration was sent: ")
    print(output)