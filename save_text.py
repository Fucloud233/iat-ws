from pathlib import Path


class TextClass:
    def __init__(self, file_name):
        self.path = "./text"
        self.file_name = file_name
        self.file_path = Path.joinpath(self.file_name, self.path)
        Path.mkdir(self.file_path)

    # 追加文字
    def append(self, text):
        with open(self.file_path, "a") as f:
            f.write(text)

