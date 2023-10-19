# 主 Python 文件

version = 0

import configure
from fetch import getDictionaryData
from mdict import writeMdxFile

def genMdict(dictionary, title, description="", nodescription=0):
    writeMdxFile(title, dictionary, description, nodescription)

if __name__ == "__main__":
    dictionary = getDictionaryData(configure.repository, 1)
    genMdict(dictionary, configure.title, configure.description, configure.nodescription)