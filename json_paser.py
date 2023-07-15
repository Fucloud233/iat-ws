# -*- coding = utf-8 -*-
# @Time : 2023/07/15 14:32
# @Autor : Fucloud
# @FIle : json_paser.py
# @Software : PyCharm

import json
from text_save import TextClass

def read(path: str):
    with open(path) as f:
        lines = f.readlines(-1)

    text = ""
    for line in lines:
        text += line + '\n'

    return text


def get_json(json_text: str) -> list:
    result_json = json.loads(json_text)["content"]["orderResult"]
    lattice_list = json.loads(result_json)["lattice"]
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


def parse(text: str):
    result_json = get_json(text)
    result_text = get_result_text(result_json)

    return result_text


# if __name__ == "__main__":
#     json_str = read("output/result2.json")
#     result_json = get_json(json_str)
#     result_text = get_result_text(result_json)
#
#     text_class = TextClass("2.txt")
#     text_class.write(result_text)
#     # print("Result:", result_text)

