# 此文件存储配置性质的全局变量。
# 警告：不要注释下述任何变量。本项目其他部分没有针对它们设置默认值。

# 本项目使用 GitHub Rest API 获取最新数据，因此数据源需为 GitHub 仓库。repository 变量指定所使用的 GitHub 仓库，格式为“所有者/仓库名”。
repository = "EhTagTranslation/Database"

# output_name 变量指定输出词典的文件名前缀。最终输出的词典将以“前缀_后缀”的格式命名，其中前缀在这里指定，而后缀将为词典的格式
output_name = "EhTagTranslation"

# title 变量指定词典名称。
title = "EhTagTranslation"

# description 变量为词典的描述
description = "EhTagTranslation 项目的翻译数据。"

# dictionary 变量指定输出的词典类型，all 代表输出全部词典
dictionary = "all"

# nodescription 变量指定是否使输出的词典不包含词条描述，若指定为 True，则最终词典只包含英文词条的中文翻译
nodescription = False