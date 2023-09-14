# 此文件存储配置性质的全局变量。

# repository 变量指定被抓取的数据所在的 Git 仓库
repository = "https://github.com/EhTagTranslation/Database"

# directory 变量指定 markdown 文件所在的目录，项目将读取该目录所有 markdown 文件
directory = "database"

# output_name 变量指定输出词典的文件名前缀。最终输出的词典将以“前缀_后缀”的格式命名，其中前缀在这里指定，而后缀将为词典的格式
output_name = "EhTagTranslation"

# dictionary 变量指定输出的词典类型，all 代表输出全部词典
dictionary = "all"

# noimage 变量指定是否使图片输出到词典，True 代表不输出图片
noimage = False

# nodescription 变量指定是否使输出的词典不包含词条描述，若指定为 True，则最终词典只包含英文词条的中文翻译
nodescription = False