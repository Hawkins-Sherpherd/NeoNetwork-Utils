'''
用于寻找空闲网络资源的，直接面向终端用户的交互式脚本。
如果您想要写非交互式的程序，可以考虑调用该项目提供的 neonetwork_utils 库。

作者：Hawkins Sherpherd
'''
import sys
sys.path.append("..")

from lib import neonetwork_utils

REGISTRY_PATH = neonetwork_utils.get_registry_path("config.json")
ASN_PATH = neonetwork_utils.get_sub_path(REGISTRY_PATH,"asn")
ROUTE_PATH = neonetwork_utils.get_sub_path(REGISTRY_PATH,"route")
ROUTE_FILE_PATHS = neonetwork_utils.get_file_list_path(ROUTE_PATH)

ASN_LIST = neonetwork_utils.get_asn_list(ASN_PATH)
ROUTE_DICT = neonetwork_utils.get_route_dict(ROUTE_FILE_PATHS)
ROUTE4 = ROUTE_DICT["ipv4"]
ROUTE6 = ROUTE_DICT["ipv6"]

POS_INPUT = ["y","Y","yes","Yes","YES"]
NEG_INPUT = ["n","N","no","No","NO"]
ASN_INPUT = ["asn","ASN","aSN","AsN","ASn","asN","Asn","aSn"]
IPV4_INPUT = ["ipv4","IPV4","Ipv4","iPv4","ipV4","IPv4","iPV4"]
IPV6_INPUT = ["ipv6","IPV6","Ipv6","iPv6","ipV6","IPv6","iPV6"]

print("欢迎使用 NeoNetwork 空闲网络资源查找脚本，请问您要查找什么网络资源类型呢？")
print("温馨提示：使用前请记得更新您的本地 NeoNetwork 注册数据。")
print("\n可接受的选项：asn，ipv4，ipv6，exit（退出脚本）")
while True:
    print("您的选项是：")
    user_input = input()
    if user_input == "exit":
        exit()
    if user_input in ASN_INPUT:
        while True:
            print("这是为您找到的10个空闲 asn：")
            asn_list = neonetwork_utils.get_no_collide_resource(neonetwork_utils.get_random_neo_asn,ASN_LIST,10)
            for i in asn_list:
                print(i)
            while True:
                print("再试一次吗？（y/n）")
                user_input = input()
                if user_input in NEG_INPUT:
                    exit()
                if user_input in POS_INPUT:
                    break
                else:
                    print("无效输入，请重新输入。")
                    continue
    if user_input in IPV4_INPUT:
        while True:
            print("您要找多大的空闲网段呢？（前缀大小范围：20-29）")
            user_input = input()
            if int(user_input) not in range(20,30):
                print("无效输入，请重新输入。")
                continue
            if int(user_input) in range(20,30):
                if int(user_input) < 24:
                    print("在申请如此大的网段之前，您真的要认真考虑是不是真的需要这么多 IPv4 地址，毕竟 NeoNetwork 的整个地址空间装不下太多这样的网段呢！")
                print("这是为您找到的10个空闲的大小为/"+user_input+"的网段：")
                ip4_list = neonetwork_utils.format_output(neonetwork_utils.get_no_collide_resource(neonetwork_utils.get_random_neo_ipv4,ROUTE4,10,prefix_len=int(user_input)))
                for i in ip4_list:
                    print(i)
                while True:
                    print("再试一次吗？（y/n）")
                    user_input = input()
                    if user_input in NEG_INPUT:
                        exit()
                    if user_input in POS_INPUT:
                        break
                    else:
                        print("无效输入，请重新输入。")
                        continue
    if user_input in IPV6_INPUT:
        while True:
            print("您要找多大的空闲网段呢？（前缀大小范围：48-64）")
            user_input = input()
            if int(user_input) not in range(48,65):
                print("无效输入，请重新输入。")
                continue
            if int(user_input) in range(48,65):
                print("这是为您找到的10个空闲的大小为/"+user_input+"的网段：")
                ip6_list = neonetwork_utils.format_output(neonetwork_utils.get_no_collide_resource(neonetwork_utils.get_random_neo_ipv6,ROUTE6,10,prefix_len=int(user_input)))
                for i in ip6_list:
                    print(i)
                while True:
                    print("再试一次吗？（y/n）")
                    user_input = input()
                    if user_input in NEG_INPUT:
                        exit()
                    if user_input in POS_INPUT:
                        break
                    else:
                        print("无效输入，请重新输入。")
                        continue
    else:
        print("无效输入，请重新输入。")
        continue