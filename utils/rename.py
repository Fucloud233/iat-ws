from pathlib import Path

if __name__ == "__main__":
    file_path = Path("output/video")
    for f in file_path.iterdir():
        # https://blog.csdn.net/liao392781/article/details/80181088
        find_res = f.name.split('-')
        if len(find_res) < 2:
            continue
        f_name = find_res[0]
        back_suffix = f.suffix

        new_name = Path.joinpath(file_path, f_name+back_suffix)
        print("[debug] new name: ", new_name)
        f.rename(new_name)
