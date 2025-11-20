import socket

def scan_ports(target_ip, start_port, end_port):
    open_ports = []
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    open_ports.append(port)
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    return open_ports