# coding: utf-8
"""
入出力の一括管理を行うモジュール
"""

import os
import sys
import configparser
import json
import re
import enum
import Entity_module
from typing import Tuple


def file_check(file_path:str) -> None:
    """
    ファイルの有無を確認する関数
    ファイルがない場合はプログラムを終了する。
    """
    if os.path.exists(file_path):
        print(file_path + "：存在を確認しました。")
    else:
        print("必要なファイルが存在しません。\nファイルを確認してください。\n\n 足りないファイル：" + file_path )
        sys.exit()

def load_player(file_path:str) -> Tuple[str,int]:
    """
    設定ファイルからplayerの情報を読み込む関数
    読み込む値は"Name"と"Level"
    """
    config_ini = configparser.ConfigParser()
    config_ini.read(file_path, encoding="utf-8")
    player_name = config_ini["BRAVER"]["Name"]
    player_level = config_ini["BRAVER"]["Level"]
    return player_name,player_level

def load_enemy_pos_list(dungeon:list, x:int, y:int) -> Tuple[list, int]:
    enemy_counter = 0
    enemy_list = []
    for i in range(y):
        for j in range(x):
            enemy_id = dungeon[i][j]
            if re.match("M",enemy_id) != None:
                enemy_info = [enemy_id, j, i]
                enemy_list.append(enemy_info)
                enemy_counter += 1
    return enemy_list, enemy_counter   

def load_enemy_info(data, category, sub_key=None):
    try:
        if sub_key:
            text = data[category][sub_key]
        else:
            text = data[category]
        return text
    except KeyError:
        error_message = f"Error: '{category}' または '{sub_key}' に対応するテキストが見つかりません。"
        print(error_message)
        return error_message
    

def load_item(file_path:str) -> Tuple[str,int]:
    """
    設定ファイルからitemの情報を読み込む関数
    読み込む値は"Name"と"Level"
    """
    config_ini = configparser.ConfigParser()
    config_ini.read(file_path, encoding="utf-8")
    item_name = config_ini["ITEM"]["Name"]
    item_level = config_ini["ITEM"]["Level"]
    return item_name,item_level


def load_item_pos_list(dungeon:list, x:int, y:int):
    item_counter = 0
    item_list = []
    for i in range(y):
        for j in range(x):
            if re.match("I",dungeon[i][j]) != None:
                enemy_info = [dungeon[i][j], i, j]
                item_list.append(enemy_info)
                item_counter += 1
    return item_list, item_counter   

def load_dungeon(file_path:str) -> Tuple[list, int, int]:
    """
    Dungeonを読み込む関数
    """
    map_list = []
    with open(file_path) as f:
        lines = f.readlines()
    for i in lines:
        one_line = i.replace("\n", "").split(",")
        map_list.append(one_line)
    x = len(map_list[0])
    y = len(map_list)
    return map_list , x, y

def show_dungeon(map_list:list, map_size_x:int, map_size_y:int):
    """
    Dungeonを表示する関数
    """
    cell_size = 3

    for i in map_list:
        for j in range(map_size_x):
            print(i[j].center(cell_size) + "|", end="")
        print("")

def load_json(file_path:str) -> dict:
    """
    jsonファイルを読み込む関数
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: '{file_path}' ファイルが見つかりません。")
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' は正しいJSON形式ではありません。")
    return None

def display_flavor_text(data, category, sub_key=None):
    """
    flavor.jsonを出力する関数
    """
    try:
        if sub_key:
            text = data[category][sub_key]
        else:
            text = data[category]
        print(text)
        return text
    except KeyError:
        error_message = f"Error: '{category}' または '{sub_key}' に対応するテキストが見つかりません。"
        print(error_message)
        return error_message

def out_result() -> None:
    pass

def print_status(status:str) -> None:
    """
    playerのstatusを表示する関数
    """
    print(status)

def select_direction(pos:Entity_module.Vector2) -> int:
    """
    方向を入力する関数
    """
    direction = None
    direction_num = None
    while True:
        direction = input("進む方向を入力してください：")
        if (direction == "W" or direction =="w") and can_move_direction_W(pos):
            direction_num = 0
            break
        elif (direction == "S" or direction =="s") and can_move_direction_S(pos):
            direction_num = 1
            break
        elif (direction == "A" or direction =="a") and can_move_direction_A(pos):
            direction_num = 2
            break
        elif (direction == "D" or direction =="d") and can_move_direction_D(pos):
            direction_num = 3
            break
        else:
            print("無効な入力です。\"W\",\"A\",\"S\",\"D\"のいずれかを入力してください。")
    return direction_num

def can_move_direction_W(pos:Entity_module.Vector2) -> bool:
    Is_move = True
    if(pos.get_y ==0):
        Is_move = False
        print("その方向には動けないよ...")
    return Is_move

def can_move_direction_S(pos:Entity_module.Vector2) -> bool:
    Is_move = True
    if(pos.get_y == 4):
        Is_move = False
        print("その方向には動けないよ...")
    return Is_move

def can_move_direction_A(pos:Entity_module.Vector2) -> bool:
    Is_move = True
    if(pos.get_x == 0):
        Is_move = False
        print("その方向には動けないよ...")
    return Is_move

def can_move_direction_D(pos:Entity_module.Vector2) -> bool:
    Is_move = True
    if(pos.get_x == 4):
        Is_move = False
        print("その方向には動けないよ...")
    return Is_move

def lose_game() -> None:
    print("you are lose!! To be a continued...")
    sys.exit()

#テスト
# file_path = "test.txt"
# file_check(file_path)
# load_dungeon(file_path)