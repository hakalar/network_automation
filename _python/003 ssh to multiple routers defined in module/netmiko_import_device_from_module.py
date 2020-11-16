from netmiko import ConnectHandler

from device_info import cisco_csr1kv_1 as device

# iteration through list of devices defined in device_info.py
net_connect = ConnectHandler(**device)
output = net_connect.send_command('show run | inc hostname')
print(output)
print(net_connect.find_prompt())

