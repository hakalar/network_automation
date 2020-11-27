from netmiko import ConnectHandler

cisco_csr1kv = {
    'device_type': 'cisco_ios',
    'host':   '192.168.57.3',
    'username': 'cisco',
    'password': 'cisco',
    'port' : 22,          # optional, defaults to 22
    'secret': 'cisco',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco_csr1kv)

# configure commands (will automatically enter into config mode)

config_commands = [ 'logging buffered 20000',
                    'logging buffered 20010',
                    'no logging console' ]
output = net_connect.send_config_set(config_commands)
print(output)