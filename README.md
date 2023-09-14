# EhDatabase2Dictionary
Convert the achivement of EhTagTranslation project to different kinds of dictionaries

将 EhTagTranslation 项目的成果转换为各种格式的词典

This project is only in Chinese and i18n would be a super long shot.

## 最新消息
记录本项目完工之前的最新进展与思路。此章节在项目完工后会删除。

+ 日期（由新到旧排序） 消息内容

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