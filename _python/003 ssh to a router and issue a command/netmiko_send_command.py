from netmiko import ConnectHandler
from getpass import getpass
import logging

cisco_csr1kv_1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.57.3',
    'username': 'cisco',
    'password': 'cisco', # get password from user input from cli
    'port' : 22,          # optional, defaults to 22
    'secret': 'cisco',     # optional, defaults to ''
}

cisco_csr1kv_2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.57.4',
    'username': 'cisco',
    'password': 'cisco',  # static ssh password
    'port' : 22,          # optional, defaults to 22
    'secret': 'cisco',     # optional, defaults to ''
}

command1 = "show ip int brief"

# iteration through list of devices defined in this script
for device in (cisco_csr1kv_1, cisco_csr1kv_2):
    net_connect = ConnectHandler(**device)
    # another way how to get the hostname into the output
    print(net_connect.find_prompt())
    # passing command as string parameter to the function
    output = net_connect.send_command('show run | inc hostname')
    print(output)
    # passing variable containing command to the send_command function
    output = net_connect.send_command(command1)
    print(output)