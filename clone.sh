#!/usr/bin/env bash
# 此脚本从上游数据库克隆 Git 仓库。

# 此变量指定上游数据库位置
Repositorypath = "https://github.com/EhTagTranslation/Database.git"

######
git clone $Repositorypath ./temp/database/