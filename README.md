# EhDatabase2Dictionary
Convert the achivement of EhTagTranslation project to different kinds of dictionaries

将 EhTagTranslation 项目的成果转换为各种格式的词典

This project is only in Chinese and i18n would be a super long shot.

## 最新消息
记录本项目完工之前的最新进展与思路。此章节在项目完工后会删除。

+ 日期（由新到旧排序） 消息内容

+ 9-19 实现了用 Rest API 获取数据的部分（fetch.py），但是 db.text.json 和 db.ast.json 有没有大的区别，才准备读。

+ 9-19 目前打算利用 Rest API 获取 EhDatabase 的最新 release，此部分将用 Python 实现，就不使用 Shell 代码了。正在阅读 Rest API 文档。

+ 9-18 今天准备研究 db.text.json 和 db.ast.json 有没有大的区别。抓取数据部分输出的内容将采用类似 db.ast.json 的 JSON 代码树。另外可以准备着手阅读各大词典格式了。

+ 9-17 从文档得知需要 db.ast.json 和 db.text.json 两个文件，其中 db.ast.json 用于生成有图词典，db.text.json 用于生成无图词典。接下来研究 db.ast.json 所使用的 JSON 语法树。

+ 9-17 OpportunityLiu 君提醒我 github release 有解析好的 JSON 格式的文件，这样只需要从 github 抓取最新的 release 就好，不需要克隆整个仓库了，此外亦不须手动用正则表达式之流，不需要数据清洗。这两天在看发布的 JSON 数据结构。

+ 9-14 看了一下存储数据的 markdown 文件，大体格式为：每行一个词条，词条格式为：`|英文名|中文名|描述|外部链接`，初步打算用正则表达式匹配此般数据，同时还需要进行数据清洗。

+ 9-14 目前计划使用 Python 脚本实现。EhDatabase 使用 markdown 存储数据，可能使用正则表达式匹配数据并将其转换为 Python 字典列表。需要从特定目录抓取所有 markdown 文件整合为同一个列表并按字母顺序排序。目前的难点有两个，一个是部分标签使用过分冗长的词组，实际查询时用到的意义不大；另一个是 male 和 female 这两个 markdown 文件包含的标签高度重合。E 站的策略是在这高度重合的标签前加入“m:”或“f:”标记，但是我怀疑某些词典全字匹配的策略对此十分不利。

## TODO
- [ ] mdict
- [ ] lingoes
- [ ] babylon
- [ ] stardict
- [ ] abbyy lingvo
- [ ] mac dictionary
- [ ] kindle dictionary
- [ ] dictd database (maybe also public server?)