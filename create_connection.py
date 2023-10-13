# Can be used for port scans and banner grabbing
# Definition: A socket is one endpoint of a two-way communication link between two programs running on the network. A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to. An endpoint is a combination of an IP address and a port number
import socket 

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Socket.AF_INET used for IPv4 communication, socket.SOCK_STREAM used for a realiable, connection oriented communication method.(TCP)
    host = '127.0.0.1'
    port = 8000
    result = s.connect_ex((host, port)) #Gives error code to confirm connection
    print('Result is {}'.format(result))
    s.close()


if __name__ == '__main__':
    main()