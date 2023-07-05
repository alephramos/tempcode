import ipaddress
import os


def get_extension_file(filename):
    name, extension = os.path.splitext(filename)
    return extension


def cidr_list_hosts(cidr: ipaddress.ip_network):
    ip_list = []
    for ip in ipaddress.IPv4Network(cidr).hosts():
        ip_list.append(str(ip))
    return ip_list


def subnet_belong_vpc(subnet: ipaddress.IPv4Network, vpc: ipaddress.IPv4Network):
    f_ip, l_ip = subnet[0], subnet[-1]
    if ip_belong_cidr(vpc, f_ip) and ip_belong_cidr(vpc, l_ip):
        return True
    else:
        return False


def ip_belong_cidr(cidr: ipaddress.IPv4Network, ip: ipaddress.IPv4Address):
    return ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(cidr)
