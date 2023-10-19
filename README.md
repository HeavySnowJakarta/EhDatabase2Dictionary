# EhDatabase2Dictionary
Convert the achivement of EhTagTranslation project to different kinds of dictionaries

将 EhTagTranslation 项目的成果转换为各种格式的词典

This project is only in Chinese and i18n would be a super long shot.

## 本项目特性

目前已经实现 MDict 格式词典的生成，目前计划支持 Babylon、星际译王、Lingvo、欧陆、Mac、Kindle、dictd 和 epwing 格式的词典，如您希望支持更多格式，欢迎提出 issue。

要获知当前分支的最新消息，参见 [CHANGELOG.md](doc/CHANGELOG.md)。要获取目前尚不稳定的开发中代码，请尝试切换至 dev 分支。要获知本项目计划支持的词典格式，参见 [TODO.md](doc/TODO.md)。

开发指南？[main.py](main.py) 这个文件本身恰巧就是本项目开发指南的序言！

## 如何使用本仓库

### 直接下载现成的词典（正在开发）

本仓库应用 GitHub Action 技术每天发布 GitHub Release，您可直接前往 GitHub Releases 页面下载所需格式的词典。本项目词典的命名采用 `EhTagTranslation_词典格式` 的格式，例如要下载 MDict 格式的文件，只需下载 `EhTagTranslation_MDict.mdx` 即可。

### 自行获取并构建词典

需要 Python 3 及以上环境，建议使用最新版本的 Python。在构建项目之前，请确保机器上已经安装 `requests` 和 `tqdm`：

```
pip3 install requests tqdm
```

克隆本仓库并运行 `main.py`，可根据喜好在 `configure.py` 中自行配置。比如，可以修改输出的词典文件名，也可以控制是否使输出的词典包含描述。

```
git clone https://github.com/HeavySnowJakarta/EhDatabase2Dictionary.git
cd EhDatabase2Dictionary
python3 main.py
```

如果程序顺利运行，您将能在 output 文件夹下找到生成的词典文件。

### 如何高效利用本项目生成的词典

目前要使用本项目生成的词典，用户应当使用支持用户自行导入词典的词典软件。目前本项目支持 MDict、欧陆词典和 Golden Dict 三款软件，更多的软件将在今后得到支持。

未来，本项目还将能够生成 Mac 和 Kindle 格式的词典，届时您只需要将本项目生成的词典导入 Mac 和 Kindle 自带的词典软件，即可在这两类设备实现随时随地对您需♂要的词汇划词翻译。更多种类的设备与系统也将在未来纳入研究。

## 已知问题

由于使用的上游纯文本数据库的问题，本项目生成的词典不含超链接。可能的解决方法是改用富文本数据库。目前不再在词典中使用超链接。

## 许可与致谢

本项目所用代码以 GPL 协议发布，本项目生成的词典数据如上游数据库一样以署名-非商业性使用-相同方式共享 3.0 中国大陆协议发布。

[EhTagTranslation](https://github.com/EhTagTranslation/Database) 项目直接启发了本项目的灵感，没有无数贡献者向该项目贡献的宝贵数据，本项目将成为一场无米之炊。

本项目操作 MDict 格式词典所使用的轮子由 [mdict-utils](https://github.com/liuyug/mdict-utils) 提供。感谢项目贡献者提供的操作实现。