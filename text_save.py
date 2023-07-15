import os
from pathlib import Path


class TextClass:
    def __init__(self, file_name):
        self.base_path = Path("output/text")
        self.file_name = file_name
        self.file_path = Path.joinpath(self.base_path, self.file_name)

        if not self.base_path.exists():
            os.mkdir(self.base_path)

    # 追加文字
    def append(self, text):
        with open(self.file_path, "a") as f:
            f.write(text)

    def write(self, text: str):
        texts = text.split("。")
        with open(self.file_path, "w") as f:
            for text_line in texts:
                f.write(text_line + "。\n")
        print("[debug] write " + self.file_name + " success!")
