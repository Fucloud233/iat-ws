# -*- coding = utf-8 -*-
# @Time : 2023/07/16 10:40
# @Autor : Fucloud
# @FIle : text_save_test.py
# @Software : PyCharm


from text_save import TextClass

if __name__ == '__main__':
    text_class = TextClass("../output/text/example", "example")
    text_class.write("hello")
