# -*- coding = utf-8 -*-
# @Time : 2023/07/15 16:13
# @Autor : Fucloud
# @FIle : utils.py
# @Software : PyCharm

# 获取文件名中的真实名字
def get_name(file_path: str):
    files = file_path.split("\\")

    if len(files) < 1:
        return ""

    names = files.pop().split('.')
    if len(names) < 1:
        return ""

    return names[0]
