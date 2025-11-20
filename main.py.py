from port_scanner import scan_ports
from brute_forcer import brute_force_login
from utils import load_passwords

def main():
    print("Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute-force Login")
    choice = input("Choose module (1/2): ")

    if choice == "1":
        ip = input("Enter target IP: ")
        start = int(input("Start port: "))
        end = int(input("End port: "))
        open_ports = scan_ports(ip, start, end)
        print(f"Open ports: {open_ports}")

    elif choice == "2":
        url = input("Enter login URL: ")
        username = input("Enter username: ")
        pwd_file = input("Enter password list file: ")
        passwords = load_passwords(pwd_file)
        brute_force_login(url, username, passwords)

if __name__ == "__main__":
    main()