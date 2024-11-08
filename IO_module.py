# coding: utf-8
"""
入出力の一括管理を行うモジュール
"""

import os
import sys
import configparser
import ast
import json
import Entity_module
from typing import Tuple, Final


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

def load_Entities(file_path:str, main_key:str, sub_key:str) -> list:
    """
    設定ファイル(Entity_config.ini)から辞書情報を読み込む関数
    データが複数ある場合はdictが入ったlistで返し、そうでない場合はdictで返す
    """
    Entity_config = configparser.ConfigParser()
    Entity_config.read(file_path, encoding="utf-8")
    entities = []
    counter = 1
    while True:
        tmp = ast.literal_eval(Entity_config[main_key][sub_key+str(counter)])
        if tmp == None:
            break
        entities.append(tmp)
        counter += 1
    return entities

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

def show_dungeon(map_list:list) -> None:
    """
    Dungeonを表示する関数
    """
    map_length :Final[int] = len(map_list)
    for i in range(map_length):
        print(map_list[i])

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

def print_start_battle(enemy: Entity_module.Entity, isAlive: bool) -> None:
    VERTICAL_LINE: Final[str] = "==================\n"
    APPEAR_TEXT: Final[str] = enemy.get_name + "が現れた!!\n"
    if(isAlive == True):
        AFTER_THE_BATTLE_TEXT: Final[str] = "ぐへへへぇぇぇ!! ぶち殺してやったぜ!!\n"
    else:
        AFTER_THE_BATTLE_TEXT: Final[str] = "う、うわぁぁぁぁぁ!! テニニニニニン\n"
    output_text = VERTICAL_LINE + APPEAR_TEXT + AFTER_THE_BATTLE_TEXT + VERTICAL_LINE
    print(output_text)



def print_status(status:str) -> None:
    """
    playerのstatusを表示する関数
    """
    print(status)

def print_enemies_status(Enemies: list) -> None:
    VERTICAL_LINE: Final[str] = "=================="
    print(VERTICAL_LINE)
    for Enemy in Enemies:
        enemy_status = Enemy.give_status()
        print(enemy_status)
    print(VERTICAL_LINE)

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