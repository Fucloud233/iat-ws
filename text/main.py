# -*- coding = utf-8 -*-
# @Time : 2023/07/15 15:42
# @Autor : Fucloud
# @FIle : main.py
# @Software : PyCharm

from pathlib import Path
from text.text_transcription import transcript
from text.json_paser import parse
from text.text_save import TextClass


def main(input_dir: str, max_num: int = 3):
    count = 0
    for f in Path(input_dir).iterdir():
        if f.is_dir():
            continue

        # 设置最多读取3个文件
        if count >= max_num:
            break

        input_file_path = str(f)
        output_file_path = Path.joinpath(Path("../output"), "", Path(input_dir).stem)

        # 三只松鼠. 转写语音
        # file_path = "output/sound/example/三只松鼠.wav"
        json_text = transcript(input_file_path)

        # 如果返回空则失败
        if json_text == "":
            return

        # 2. 解析转写结果
        result_text = parse(json_text)

        # 3. 保存解析结果
        file_name = Path(input_file_path).stem
        text_class = TextClass(output_file_path, file_name)
        text_class.write(result_text)

        count += 1


if __name__ == "__main__":
    file_dir = Path("../output/sound")
    file_name_list = [
        "八马茶业官方旗舰店",
        "大姐夫",
        "果江南",
        "草原良友官方旗舰店",
        "贵州芝姐一家",
        # "example"
    ]

    for file_name in file_name_list:
        file_path = Path.joinpath(file_dir, file_name)
        main(str(file_path))
