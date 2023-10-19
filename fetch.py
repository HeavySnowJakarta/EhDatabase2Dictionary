# 此文件利用 GitHub Rest API 从 api.github.com 自动从上游获取最新数据。

import json
import requests

# 首先讲一下 noimage 变量的意义。本项目创立初期尝试根据需求设计输出有图和无
# 图词典的功能，后因此功能可能作用不大而放弃。与之相关的已经设计好的部分将会保
# 留以供有需要时复用。

# fetch.py 由两个函数构成，其中 getDictionaryData() 为其主要部分。

# 此函数利用 Rest API 基于所提供的仓库获取数据源实际地址
# https://api.github.com/repos/repository/releases/latest 本身是一个 json
# 文件，在这个文件中“藏”着数据源的实际地址。这个函数的作用正是从这一地址获取数据库的
# 实际下载地址。
def getDataUrl(repository, noimage):
    url = "https://api.github.com/repos/" + repository + "/releases/latest"
    stringresult = requests.get(url).text
    jsonresult = json.loads(stringresult)
    if noimage:
        for i in jsonresult["assets"]:
            if i["name"] == "db.text.json":
                return i["browser_download_url"]
    else:
        for i in jsonresult["assets"]:
            if i["name"] == "db.ast.json":
                return i["browser_download_url"]

# 此函数为 fetch.py 的主体，从数据源实际地址解析 JSON 格式的数据并返回 Python 字典            
def getDictionaryData(repository, noimage):
    # 从 URL 获取 JSON 格式的字典
    url = getDataUrl(repository, noimage)
    stringresult = requests.get(url).text
    jsonresult = json.loads(stringresult)
    # 上述代码返回的字典是有层级结构的，我们接下来去除这些层级结构
    result = {}
    for category in jsonresult["data"]:
        for enname in category["data"].keys():
            result[enname] = category["data"][enname]
    # 当 female 与 male 标签的词条同时存在时，取 female 标签的词条
    # 为了确保这一点，我们在这里牺牲一些效率把这些相同的词条再一次换为 female 的
    # 接下来的四行代码虽然能实现业务，但是很烂，求大佬提供更好的实现方式
    for category in jsonresult["data"]:
        if category["namespace"] == "female":
            for enname in category["data"].keys():
                result[enname] = category["data"][enname]
    return result