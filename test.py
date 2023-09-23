# 本程序旨在测试 male 与 female 标签有无不同之处。

import json

f = open("test.json", "r", encoding="utf-8")
dictionary = json.loads(f.read())

for i in dictionary["data"]:
    if i["namespace"] == "male":
        male = i["data"]
    if i["namespace"] == "female":
        female = i["data"]

num = 0

for i in male.keys():
    if i in female.keys():
        if male[i]["name"] != female[i]["name"] or male[i]["intro"] != female[i]["intro"] or male[i]["links"] != female[i]["links"]:
            print("DIFFERENT: ", i)
            print("    M   NAME: ", male[i]["name"])
            print("        INTRO: ", male[i]["intro"])
            print("        LINKS: ", male[i]["links"])
            print("    F   NAME: ", female[i]["name"])
            print("        INTRO: ", female[i]["intro"])
            print("        LINKS: ", female[i]["links"])
            print(" ")
            num = num + 1


print("共", num, "条结果。")