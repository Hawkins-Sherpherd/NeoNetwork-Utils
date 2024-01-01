# NeoNetwork-Utils
一个致力于为 NeoNetwork 注册数据查询提供便利的 Python 库和开箱即用工具组合。

## 项目文件结构
* lib
  * neonetwork_utils.py
* Tool_FreeResourceFinder.py
* config.json

### neonetwork_utils.py
neonetwork_utils 库的本体，它提供如下函数：
* get_registry_path(config_file)：从提供的 config_file 路径所指的 json 文件中获取 NeoNetwork 注册数据所在的路径。
* get_sub_path(registry_path,schema)：从提供的 NeoNetwork 注册数据文件夹路径和数据子类名称获取 NeoNetwork 注册数据子类的路径
* get_asn_list(asn_path)：获取 ASN 列表。
* get_route_dict(route_path)：通过提供的 route 数据文件夹路径从其中的注册数据文件获取路由注册数据，返回一个结构为 {"ipv4":[（一连串的 IPv4Network 对象）],"ipv6":[（一连串的 IPv6Network 对象）]} 的字典。
* get_file_list_path(sub_path)：获取目录下所有文件的路径。
* get_random_neo_asn()：生成随机的 NeoNetwork ASN。
* get_random_neo_ipv4(prefix_len)：生成随机的 NeoNetwork IPv4 网段。
* get_random_neo_ipv6(prefix_len)：生成随机的 NeoNetwork IPv6 网段。
* get_no_collide_resource(generate_func,entity_list,count,**kwargs)：生成无冲突的指定生成函数及其函数以及生成数量的 NeoNetwork 网络资源。
* format_output(input)：主要用于格式化类型为 ipaddress.IPv4Network 和 ipaddress.IPv6Network 的数据为字符串，input 应为一个列表。

### Tool_FreeResourceFinder.py
用于寻找空闲网络资源的，直接面向终端用户的交互式脚本。

### config.json
该项目内的脚本的默认配置文件。
内有如下配置选项：
* registry_path：NeoNetwork 注册数据的路径，默认为"../NeoNetwork"，使用前请修改为您的 NeoNetwork 注册数据所在的路径。