from netmiko import ConnectHandler

from device_info import cisco_csr1kv_1 as devices # noqa

cisco_csr1kv_1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.57.3',
    'username': 'cisco',
    'password': password, # get password from user input from cli
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

# iteration through list of devices defined in this script
for device in (cisco_csr1kv_1, cisco_csr1kv_2):
    net_connect = ConnectHandler(**device)
    # another way how to get the hostname into the output
    print(net_connect.find_prompt())