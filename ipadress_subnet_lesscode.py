import ipaddress

ip_list=["192.168.0.0", "192.168.0.2", "192.168.0.3","192.168.0.4","192.168.0.5","192.168.0.7"]

binary_list = [f'{int(ipaddress.IPv4Address(ip)):032b}' for ip in ip_list]

prefix_len = 32 - len(bin(int(binary_list[-1], 2) ^ int(binary_list[0], 2))[2:])

subnet = ipaddress.IPv4Network(f'{ip_list[0]}/{prefix_len}')

print(f"Subnet: {subnet}")