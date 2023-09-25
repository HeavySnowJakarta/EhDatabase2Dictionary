# 主 Python 文件

version = 0

import configure
from fetch import getDictionaryData
from mdict import writeMdxFile

def genMdict(dictionary, title, description, nodescription):
    f = open("./output/"+configure.output_name+"_mdict.mdx", 'wb')
    writeMdxFile(title, description, dictionary, nodescription, f)
    f.close()

def main():
    dictionary = getDictionaryData(configure.repository, 1)
    genMdict(dictionary, configure.title, configure.description, configure.nodescription)