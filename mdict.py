# 此文件调用 writemdict 库产生 MDict 格式的文件
# writemdict 库是 MdxBuilder 的一个开源实现，并不包含 mdx 的全部技术细节，也
# 不能生成新版 mdx 词典，不过这不重要。

from lib.writemdict.writemdict import MDictWriter

# 我们的 mdict 词典将采用的词条格式为：英文名<br>中文名<br>描述
# 这些词条将以 Python 字典的格式传递给 writemdict 库
# 此函数的 dictionary 由 fetch.py 的函数生成
def generateSourceDictionary(dictionary, nodescription):
    result = {}
    if (nodescription):
        for entry in dictionary.keys():
            result[entry] = dictionary[entry]["name"]
    else:
        for entry in dictionary.keys():
            if (dictionary[entry]["links"]==""):
                result[entry] = dictionary[entry]["name"] + "<br>" + dictionary[entry]["intro"]
            else:
                result[entry] = dictionary[entry]["name"] + "<br>" + dictionary[entry]["intro"] + "<br>" + dictionary[entry]["links"]
    return result

# 此函数调用 writemdict 库并向传来的文件对象写入数据，其中 dictionary 参数由
# fetch.py 的函数生成，file 为被写入的文件对象，必须拥有写入权限且必须以二进制
# 格式打开
def writeMdxFile(title, description, dictionary, nodescription, outfile):
    source_dictionary = generateSourceDictionary(dictionary, nodescription)
    writer = MDictWriter(source_dictionary, title=title, description=description)
    writer.write(outfile)