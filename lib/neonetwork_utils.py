'''
一个为对查询 NeoNetwork 注册数据提供便利而生的 Python 库

作者：Hawkins Sherpherd
'''

import json
import toml
import os
import ipaddress
import random
import re

NEO_ASN_RANGE_MIN = 4201270000
NEO_ASN_RANGE_MAX = 4201279999
NEO_IP_MIN = int(ipaddress.IPv4Address("10.127.0.0"))
NEO_IP_MAX = int(ipaddress.IPv4Address("10.127.255.255"))
NEO_IP6_MIN = int(ipaddress.IPv6Address("fd10:127::"))
NEO_IP6_MAX = int(ipaddress.IPv6Address("fd10:127:ffff:ffff:ffff:ffff:ffff:ffff"))
ASN_FILE_STRIP_LIST = ["AS",".toml"]
IP4_REGEX = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(/(3[0-2]|2[0-9]|1[0-9]|[0-9]))?$" # 来自 https://gist.github.com/khanzf/27996c1660317a4a2988
IP6_REGEX = r"^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))(\/((1(1[0-9]|2[0-8]))|([0-9][0-9])|([0-9])))?$" # 来自 https://gist.github.com/khanzf/27996c1660317a4a2988

def get_registry_path(config_file):
    with open("config.json","r") as config_file:
        return json.load(config_file)["registry_path"]
    
def get_sub_path(registry_path,schema):
    return registry_path + "/" + schema + "/"

def get_asn_list(asn_path):
    asn_list = os.listdir(asn_path)
    for i in range(len(asn_list)):
        for j in ASN_FILE_STRIP_LIST:
            asn_list[i] = asn_list[i].strip(j)
    return asn_list

def get_route_dict(route_path):
    route_dict = {"ipv4":[],"ipv6":[]}
    for i in range(len(route_path)):
        with open(route_path[i],"r") as route_file:
            routes = toml.load(route_file)
            routes = list(routes.keys())
            for j in routes:
                if re.search(IP4_REGEX,j):
                    route_dict["ipv4"].append(ipaddress.IPv4Network(j))
                if re.search(IP6_REGEX,j):
                    route_dict["ipv6"].append(ipaddress.IPv6Network(j))
        route_file.close()
    route_dict["ipv4"] = list(set(route_dict["ipv4"]))
    route_dict["ipv6"] = list(set(route_dict["ipv6"]))
    return route_dict

def get_file_list_path(sub_path):
    file_list = os.listdir(sub_path)
    for i in range (len(file_list)):
        file_list[i] = sub_path + file_list[i]
    return file_list

def get_random_neo_asn():
    return random.randint(NEO_ASN_RANGE_MIN,NEO_ASN_RANGE_MAX)

def get_random_neo_ipv4(prefix_len):
    return ipaddress.IPv4Network(str(ipaddress.IPv4Address(random.randrange(NEO_IP_MIN,NEO_IP_MAX,2**(32-prefix_len))))+"/"+str(prefix_len))

def get_random_neo_ipv6(prefix_len):
    return ipaddress.IPv6Network(str(ipaddress.IPv6Address(random.randrange(NEO_IP6_MIN,NEO_IP6_MAX,2**(128-prefix_len))))+"/"+str(prefix_len))

def get_no_collide_resource(generate_func,entity_list,count,**kwargs): # 生成无冲突的随机网络资源
    generate_result = []
    for i in range(count):
        j = generate_func(**kwargs)
        if j not in entity_list:
            generate_result.append(j)
    return generate_result

def format_output(input): # 格式化类型为 ipaddress.IPv4Network 和 ipaddress.IPv6Network 的数据为字符串，input 应为一个列表
    output = []
    for i in input:
        output.append(str(i))
    return output