#coding utf8

import os
import sys

def file_check(file_path:str) -> None:
    if os.path.exists(file_path):
        print(file_path + "：存在を確認しました。")
    else:
        print("必要なファイルが存在しません。ファイルを確認してください。\n\n 足りないファイル：" + file_path )
        sys.exit()

def print_result() -> None:
    