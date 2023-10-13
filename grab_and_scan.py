from port_scanner import Scanner
from banner_reading import Grabber
from utils import timefunc

@timefunc
def main():
    ip = '192.168.1.153'
    portrange = (1, 151)
    scanner = Scanner(ip)
    scanner.scan(*portrange)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip, port)
            print(grabber.read())
            grabber.close()
        except Exception as e:
            print("Error", e)


if __name__ == '__main__':
    main()