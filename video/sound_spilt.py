# -*- coding = utf-8 -*-
# @Time : 2023/07/15 17:59
# @Autor : Fucloud
# @FIle : sound_spilt.py
# @Software : PyCharm

# Refer:
# https://blog.csdn.net/xuqingda/article/details/86540333
# https://www.cnblogs.com/zhaoke271828/p/17007046.html

import os
import librosa
from pathlib import Path


# 获取音频总时长
def get_dur_time(file_name: str):
    return librosa.get_duration(path=file_name)


def audio_cut(audio_in_path: Path, audio_out_path):
    """
    :param audio_in_path: 输入音频的绝对路径
    :param audio_out_path: 切分后输出音频的绝对路径
    :return:
    """

    total_dur_time = get_dur_time(str(audio_in_path))
    single_dur_time = 600

    suffix = audio_in_path.suffix

    cur_time = 0
    count = 1
    while cur_time < total_dur_time:
        # 生成切片的文件名
        split_name = audio_out_path + '\\' + str(count) + suffix

        print("[debug] total time: {} cur time: {}".format(total_dur_time, cur_time))
        cmd = "ffmpeg -i {in_path} -vn -acodec copy -ss {Start_time} -t {Dur_time} {out_path}".format(
            in_path=audio_in_path,
            out_path=split_name, Start_time=cur_time, Dur_time=cur_time+single_dur_time)

        print("[debug] ", cmd)
        os.system(cmd)

        cur_time += single_dur_time
        count += 1


def split_sound(audio_in_name: Path):
    real_file_name = audio_in_name.stem
    audio_out_dir = "output\\sound\\" + real_file_name
    if not Path(audio_out_dir).exists():
        os.mkdir(audio_out_dir)

    audio_cut(audio_in_name, audio_out_dir)


if __name__ == "__main__":
    file_path = Path("output/sound")

    for f in file_path.iterdir():
        # 获取文件路径
        f_name = Path.joinpath(file_path, f.name)
        # 跳过路径
        if Path(f_name).is_dir():
            continue
        print("[debug] file name: ", f_name)

        # 分割音频
        split_sound(f_name)