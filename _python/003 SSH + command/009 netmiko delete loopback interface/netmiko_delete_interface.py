#! /usr/bin/env python

# Import libraries
from netmiko import ConnectHandler

from device_info import cisco_csr1kv_1 as device

# New Loopback Details
loopback = {"int_name": "Loopback1"}

# Create a CLI configuration
interface_config = [
    "no interface {}".format(loopback["int_name"])
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