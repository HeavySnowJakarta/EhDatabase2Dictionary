# 主 Python 文件

version = 0

# 欢迎 hack 本项目！本项目将使用翔实的注释让您理解它简单的工作原理。
# 您打开本文件可能是受到了 README.md 的指引。本文件本身就是开发指南的概述部分。
# 在 import 部分，我将为你展示本项目的大致结构。

# = 导入模块 =
# 首先是 confugure.py。configure.py 存储了本项目所使用的配置性变量。
import configure

# fetch.py 的作用是从上游数据库，也即 EhDataBase，获取制作词典所需的源数据。
# fetch.py 共有两个函数，我们在这里使用 getDictionaryData() 函数从 GitHub
# 获取 json 格式的数据并将其转换为 Python 字典。
from fetch import getDictionaryData

# 接下来是制作词典的部分。对于每种词典（虽然现在只有一种 QwQ），本项目使用一个
# 单独的 Python 文件存储其源代码。

# mdict.py，顾名思义，生成 MDict 格式的词典。writeMdxFile() 函数为其主心骨。
from mdict import writeMdxFile

# 以上是本项目根目录的主要文件。此外：
#   doc 目录，存储除 README.md 以外的文档
#   lib 目录，存储本项目引用的子模块。目前本项目引用的子模块有：
#     mdict-utils，生成与转换 MDict 格式词典的基建
#   temp 目录，存储本项目所需生成的中间文件，例如制作 MDict 格式词典所需的 txt
#             格式的词典
#   output 目录，存储本项目最终生成的词典文件
#   .github 目录，存储配置 GitHub Action 用的数据
# 从文件结构就可以看出，本项目技术含量不高，到目前为止用的轮子全是别人实现好的。

# = 函数定义 =
# 同样地，对于每类即将生成的词典，本文件也为它们分别写一个函数。
# genMdict() 函数，顾名思义，就是生成 MDict 格式词典的函数咯。
def genMdict(dictionary, title, description="", nodescription=0):
    writeMdxFile(title, dictionary, description, nodescription)

# main.py 主要干的事情无非两个：
# - 调用 fetch.py 获取上游数据库的源内容
# - 调用各生成词典的子文件在 output 目录下生成词典
# 知道了本项目的大体结构，您可以到各个子文件查看对应功能的实现。
if __name__ == "__main__":
    dictionary = getDictionaryData(configure.repository, 1)
    genMdict(dictionary, configure.title, configure.description, configure.nodescription)