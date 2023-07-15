# -*- coding = utf-8 -*-
# @Time : 2023/07/15 14:32
# @Autor : Fucloud
# @FIle : json_paser.py
# @Software : PyCharm

import json


def read_json(path: str):
    with open(path) as f:
        lines = f.readlines(-1)

    text = ""
    for line in lines:
        text += line + '\n'

    return json.loads(text)


def get_main_json(json_text: str) -> list:
    lattice_list = json.loads(json_text)["lattice"]
    # print(json.dumps(result_json, indent=2))

    words = []
    for lattice in lattice_list:
        words.append(json.loads(lattice["json_1best"])["st"]["rt"][0])

    return words


def get_result_text(words: list):
    text = ""
    # result_json = json.loads(result_json)["st"]["rt"]
    for word in words:
        for w in word["ws"]:
            text += w["cw"][0]["w"]

    return text


# 解析转写结果中的文本
def parse(json_text: str):
    print("[info] parse start!")
    # 1. 获取JSON中保存转写结果中的重要文本
    result_json = get_main_json(json_text)

    # 2. 获得转写结果中的结果文本
    result_text = get_result_text(result_json)
    print("[info] parse success!")

    return result_text


# if __name__ == "__main__":
#     json_str = read("output/result2.json")
#     result_json = get_json(json_str)
#     result_text = get_result_text(result_json)
#
#     text_class = TextClass("2.txt")
#     text_class.write(result_text)
#     # print("Result:", result_text)
