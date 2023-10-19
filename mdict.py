# 此文件调用 mdict_utils 库来生成 mdict 格式的词典

# 我们需要用到 mdict_utils 库中的 writer.py 中的 pack() 方法和
# pack_mdx_txt() 方法
from lib.mdict_utils.mdict_utils import writer
# from lib.writemdict.writemdict import MDictWriter

# generateSourceDictionary() 函数生成制作 MDict 词典所需的 txt 格式的文本
# 文件，该文件将保存为 `output/<configure.py 定义的 name>_mdict.txt`。
# name 和 nodescription 参数当由 configure.py 定义，dictionary 参数由 
# fetch.py 下的 getDictionaryData() 函数生成
def generateSourceDictionary(name, dictionary, nodescription=0):
    f = open("temp/"+name+"_mdict.txt", "w", encoding="utf-8")
    if nodescription:
        for enname in dictionary.keys():
            f.write(enname+"\n"+dictionary[enname]["name"]+"\n</>\n")
    else:
        for enname in dictionary.keys():
            if dictionary[enname]["links"]=="":
                f.write(enname+"\n"+"<b>"+dictionary[enname]["name"]+"</b>"+"\n"+dictionary[enname]["intro"]+"\n</>\n")
            else:
                f.write(enname+"\n"+"<b>"+dictionary[enname]["name"]+"</b>"+"\n"+dictionary[enname]["intro"]+"\n"+dictionary[enname]["links"]+"\n</>\n")
    f.close()

# 此函数调用 mdict_utils 库并根据指定的 txt 文件路径写入词典。title、
# description、nodescription 参数当由 confugure.py 定义，dictionary 参
# 数由 fetch.py 下的 getDictionaryData() 函数生成
# TODO: 继续完成对 mdict_utils 库下两个函数的调用
def writeMdxFile(title, dictionary, description="", nodescription=0):
    # 首先生成 pack_mdx_txt() 函数所需要的 txt 中间文件
    generateSourceDictionary(name=title, dictionary=dictionary, nodescription=nodescription)
    # 调用 writer.pack_mdx_txt() 函数解析前面生成的 txt 文件生成 Python 词典数据
    dic = writer.pack_mdx_txt(source="temp/"+title+"_mdict.txt")
    # 调用 writer.pack() 函数生成最终 mdx 文件
    writer.pack(target="output/"+title+"_MDict.mdx", dictionary=dic, title=title, description=description)