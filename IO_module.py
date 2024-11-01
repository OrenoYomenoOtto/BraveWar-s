# coding: utf-8
"""
入出力の一括管理を行うモジュール
"""

import os
import sys
import configparser
from typing import Tuple


def file_check(file_path:str) -> None:
    if os.path.exists(file_path):
        print(file_path + "：存在を確認しました。")
    else:
        print("必要なファイルが存在しません。\nファイルを確認してください。\n\n 足りないファイル：" + file_path )
        sys.exit()

def load_player(file_path:str) -> Tuple[str,int]:
    config_ini = configparser.ConfigParser()
    config_ini.read(file_path, encoding="utf-8")
    player_name = config_ini["BRAVER"]["Name"]
    player_level = config_ini["BRAVER"]["Level"]

    return player_name,player_level


def load_dungeon(file_path:str) -> list:
    with open(file_path) as f:
        date = f.read()
        print(date)

def out_result() -> None:
    pass

def print_status() -> None:
    pass

#テスト
# file_path = "test.txt"
# file_check(file_path)
# load_dungeon(file_path)