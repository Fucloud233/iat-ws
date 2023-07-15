# -*- coding = utf-8 -*-
# @Time : 2023/07/15 15:42
# @Autor : Fucloud
# @FIle : main.py
# @Software : PyCharm

from text_transcription import transcript
from json_paser import parse
from text_save import TextClass
from utils import get_name


def main():
    # 1. 转写语音
    file_path = "output\\sound\\2.wav"
    json_text = transcript(file_path)

    # 如果返回空则失败
    if json_text == "":
        return

    # 2. 解析转写结果
    result_text = parse(json_text)

    # 3. 保存解析结果
    file_name = get_name(file_path)
    text_class = TextClass(file_name)
    text_class.write(result_text)


if __name__ == "__main__":
    main()
