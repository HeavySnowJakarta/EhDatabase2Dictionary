# 此文件利用 GitHub Rest API 从 api.github.com 自动从上游获取最新数据。

def fetch(repository):
    url = "https://api.github.com/repos/" + repository + "/releases/latest"