import paramiko
import socket
import getpass

#get user/password/substring (for search)
myuser = input("Enter Username For Process: ")
mypass = getpass.getpass()
mysearch = input("Please enter string to search: ")

#get a list of devices from devices.txt - one per line
qbfile = open("devices.txt", "r")

# loop through devices in qbfile
# ssh to each device and do a sho ver
# on-match print "device" has + current line
# exit


for aline in qbfile:
    myhost = aline.rstrip()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(myhost, username=myuser, password=mypass, timeout=15, auth_timeout=20)
        channel = ssh.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')
        stdin.write('''
        terminal length 0
        show version
        exit
        ''')
        showver = stdout.read()
        for verline in showver.splitlines():
            if mysearch in verline:
                print (myhost + " has " + verline)
                ssh.close()
                exit()
        ssh.close()
    except paramiko.AuthenticationException, e:
        print ("Could not authentication to " + myhost)
    except (paramiko.SSHException, socket.error), e:
        print ("SSH Error connecting to " + myhost)

qbfile.close()