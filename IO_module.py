#coding: utf8
"""
入出力の一括管理を行うモジュール
"""

import os
import sys

def file_check(file_path:str) -> None:
    if os.path.exists(file_path):
        print(file_path + "：存在を確認しました。")
    else:
        print("必要なファイルが存在しません。\nファイルを確認してください。\n\n 足りないファイル：" + file_path )
        sys.exit()

def load_dungeon(file_path:str):
    with open(file_path) as f:
        date = f.read()
        print(date)

def out_result() -> None:
    pass

def print_status() -> None:
    pass

#テスト
file_path = "test.txt"
file_check(file_path)
load_dungeon(file_path)