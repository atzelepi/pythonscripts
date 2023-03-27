import ipaddress
ip_list=["192.168.0.0", "192.168.0.2", "192.168.0.3","192.168.0.4","192.168.0.5","192.168.0.7"]
ip_list.sort()
print("sorted bin list is: ", ip_list)

ip_objects =[ipaddress.IPv4Address(ip) for ip in ip_list]
print("ip objects",ip_objects)
binary_list  = ['{:#b}'.format(ipaddress.IPv4Address(ip)) for ip in ip_list]

print("sorted bin list is: ", binary_list)

binary_representation_list = []
for ip in binary_list:
    binary_representation = ip[2:]
    binary_representation_list.append(binary_representation)
    print("binary respresentation of the list is: ", binary_representation_list)
# Find the largest prefix length that will accommodate all the IP addresses
result = int(binary_representation_list[-1], 2) ^ int(binary_representation_list[0], 2)
result_binary = bin(result)[2:]
prefix_len=32-len(result_binary)
print("XOR result in binary: ", result_binary)
subnet = ipaddress.IPv4Network(str(ip_objects[0]) + '/' + str(prefix_len))
print(subnet)
