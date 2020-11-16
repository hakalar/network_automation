#! /usr/bin/env python

cisco_csr1kv_1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.57.5',
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