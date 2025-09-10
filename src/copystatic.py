# python
import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for name in os.listdir(source_dir_path):
        src = os.path.join(source_dir_path, name)
        dst = os.path.join(dest_dir_path, name)
        print(f" * {src} -> {dst}")
        if os.path.isfile(src):
            shutil.copy(src, dst)
        else:
            copy_files_recursive(src, dst)
