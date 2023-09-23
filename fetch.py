# 此文件利用 GitHub Rest API 从 api.github.com 自动从上游获取最新数据。

import json
import requests

# 首先讲一下 noimage 变量的意义。本项目创立初期我（Heavysnowjakarta）曾尝试设计
# 根据需求输出有图和无图词典的功能，后因我认为此功能作用不大而放弃。与之相关的已经
# 设计好的部分将会保留以供有需要时复用。

# 此函数利用 Rest API 基于所提供的仓库获取数据源实际地址
def getdataurl(repository, noimage):
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
def getjsondata(repository, noimage):
    url = getdataurl(repository, noimage)
    stringresult = requests.get(url).text
    jsonresult = json.loads(stringresult)
    # TODO: 根据 db.ast.json 返回字典