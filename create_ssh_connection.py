import paramiko #Paramiko is a python library that makes a connection with a remote device through SSH.
# Makes a secure connection between two devices

# Secure Shell is used to connect to servers, make changes, perform uploads and exit

def main():
    ip = '192.168.1.153'
    username = 'itguys'
    password = "Rocky"
    timeout = 5
    client_policy = paramiko.AutoAddPolicy()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(client_policy)
    client.connect(ip, username=username, password=password, timeout=timeout)
    print(client)





if __name__ == '__main__':
    main()