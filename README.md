# EhDatabase2Dictionary
Convert the achivement of EhTagTranslation project to different kinds of dictionaries

将 EhTagTranslation 项目的成果转换为各种格式的词典

This project is only in Chinese and i18n would be a super long shot.

## 最新消息
记录本项目完工之前的最新进展与思路。此章节在项目完工后会删除。

+ 日期（由新到旧排序） 消息内容

+ 9-23 阅读了 MDict txt 格式的初步制作方法。mdx 格式词典的生成要用到 MdxBuilder，这是仅使用于 Windows 下的 GUI 闭源软件，如果要用 MdxBuilder，我必须考虑：

    + 要不要把 Github Actions 容器换成 Windows 虚拟机？
    + 要不要想办法自动化操作 GUI 程序？
    + 要不要在开源项目里引入闭源代码？

我的想法是最好使用开源实现，这样生成的词典或许是不完美的，或许对不同的软件兼容性不好，但是开源实现能极好地解决上述几个问题。

参考资料：
    + [writemdict.py](https://github.com/zhansliu/writemdict)
    + [一些讨论](https://forum.freemdict.com/t/topic/774)

+ 9-23 完成了获取 Python 字典格式的数据的部分，接下来基于这一部分生成词典。

+ 9-23 用脚本测试了一下 male 与 female 标签之间的差异。某版本数据库中这两个标签共存在 61 处差异，现摘录部分如下：

```
DIFFERENT:  fairy
    M   NAME:  仙子🧚‍♂️
        INTRO:  有翅膀的人或其他生物，往往体型很小。
        LINKS:
    F   NAME:  仙女🧚‍♀️
        INTRO:  有翅膀的人或其他生物，往往体型很小。
        LINKS:

DIFFERENT:  dinosaur
    M   NAME:  恐龙🦖
        INTRO:  任何恐龙进化枝的动物。
        LINKS:
    F   NAME:  恐龙🦕
        INTRO:  任何恐龙进化枝的动物。
        LINKS:

DIFFERENT:  magical girl
    M   NAME:  魔法少女
        INTRO:  一种服装，包括裙子和褶边制服。需要异性装(crossdressing)标签。
        LINKS:
    F   NAME:  魔法少女
        INTRO:  一种服装，包括裙子和褶边制服。
        LINKS:

DIFFERENT:  growth
    M   NAME:  巨大化
        INTRO:  变高，有可能成为巨人(giant)
        LINKS:
    F   NAME:  巨大化
        INTRO:  变高，有可能成为女巨人(giantess)。
        LINKS:

DIFFERENT:  unusual pupils
    M   NAME:  异瞳
        INTRO:  瞳孔是或包含奇怪的形状，如心形、星形。除非是意想不到的形状，否则不应该用于动物/怪物(monster)的眼睛。
        LINKS:
    F   NAME:  异瞳
        INTRO:  瞳孔是或包含奇怪的形状，如心形、星形。除非是意想不到的形状，否则不应该用于动物/恶魔的眼睛。
        LINKS:
```

绝大多数词条是完全重合的。鉴于本词典的性质，针对 f 与 m 标签英文词条重合而中文词条不重合的部分，我认为只保留 f 词条而不保留 m 词条较为合适。

+ 9-19 目前我认为有图词典实用价值非常小，不再设计输出有图词典的功能。目前 noimage 变量等已经设计好的部分将会保留以供有需要时使用。

+ 9-19 实现了用 Rest API 获取数据的部分（fetch.py），但是 db.text.json 和 db.ast.json 有没有大的区别，才准备读。

+ 9-19 目前打算利用 Rest API 获取 EhDatabase 的最新 release，此部分将用 Python 实现，就不使用 Shell 代码了。正在阅读 Rest API 文档。

+ 9-18 今天准备研究 db.text.json 和 db.ast.json 有没有大的区别。抓取数据部分输出的内容将采用类似 db.ast.json 的 JSON 代码树。另外可以准备着手阅读各大词典格式了。

+ 9-17 从文档得知需要 db.ast.json 和 db.text.json 两个文件，其中 db.ast.json 用于生成有图词典，db.text.json 用于生成无图词典。接下来研究 db.ast.json 所使用的 JSON 语法树。

+ 9-17 OpportunityLiu 君提醒我 github release 有解析好的 JSON 格式的文件，这样只需要从 github 抓取最新的 release 就好，不需要克隆整个仓库了，此外亦不须手动用正则表达式之流，不需要数据清洗。这两天在看发布的 JSON 数据结构。

+ 9-14 看了一下存储数据的 markdown 文件，大体格式为：每行一个词条，词条格式为：`|英文名|中文名|描述|外部链接`，初步打算用正则表达式匹配此般数据，同时还需要进行数据清洗。

+ 9-14 目前计划使用 Python 脚本实现。EhDatabase 使用 markdown 存储数据，可能使用正则表达式匹配数据并将其转换为 Python 字典列表。需要从特定目录抓取所有 markdown 文件整合为同一个列表并按字母顺序排序。目前的难点有两个，一个是部分标签使用过分冗长的词组，实际查询时用到的意义不大；另一个是 male 和 female 这两个 markdown 文件包含的标签高度重合。E 站的策略是在这高度重合的标签前加入“m:”或“f:”标记，但是我怀疑某些词典全字匹配的策略对此十分不利。

## TODO
- [ ] mdict_mdx mdd
- [ ] lingoes_ld2
- [ ] babylon_bgl
- [ ] stardict_dict dict.dz idx
- [ ] abbyy lingvo_dsl->lsd lud
- [ ] mac dictionary_dictionary
- [ ] kindle dictionary_mobi
- [ ] dictd database (maybe also public server?)_dictd index
- [ ] epwing oneswing