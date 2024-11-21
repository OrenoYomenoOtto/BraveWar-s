# coding: utf-8
"""
入出力の一括管理を行うモジュール
"""

import os
import sys
import configparser
import ast
import json
import random
import Entity_module
from typing import Tuple, Final


class color:
    RED = "\033[31m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    END = "\033[0m"

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

def load_dungeon_info(file_path: str) -> Tuple[int, int]:
    """
    ダンジョンの情報を読み込む関数
    """
    Entity_config = configparser.ConfigParser()
    Entity_config.read(file_path, encoding="utf-8")
    info = []
    counter = 1
    while True:
        tmp = ast.literal_eval(Entity_config["INFO"][f"Dungeon{str(counter)}"])
        if tmp == None:
            break
        info.append(tmp)
        counter += 1
    return info

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
            # 複数のテキストがある場合にランダムで1つを取得
            if isinstance(data[category], dict):
                text = random.choice(list(data[category].values()))
            else:
                text = data[category]
        print(text)
        print("==================\n")
        return text
    except KeyError:
        error_message = f"Error: '{category}' または '{sub_key}' に対応するテキストが見つかりません。"
        print(error_message)
        return error_message

def out_result(isGenocide: bool, isFaster: bool) -> None:
    if isGenocide == True:
        print(color.RED+"称号が送られます --シリアルキラー--"+color.END)
    if isFaster == True:
        print(color.MAGENTA+"称号が贈られます --クリアもアレも早いわね...--"+color.END)

def out_fin_txt():
    print("おめでとう。\nGameClear")

def print_start_battle(enemy_name: str) -> None:
    VERTICAL_LINE: Final[str] = "==================\n"
    APPEAR_TEXT: Final[str] = enemy_name + "が現れた!!\n"
    output_text = VERTICAL_LINE + APPEAR_TEXT
    print(output_text)

def print_exp(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        exp_list = f.readlines()
    for i in range(len(exp_list)):
        print(exp_list[i], end="")
    print("\n\n")


def print_status(status:str) -> None:
    """
    playerのstatusを表示する関数
    """
    print(color.CYAN+status+color.END)

def print_enemies_status(Enemies: list, Boss: Entity_module.Enemy) -> None:
    VERTICAL_LINE: Final[str] = "=================="
    print(VERTICAL_LINE)
    for Enemy in Enemies:
        enemy_status = Enemy.give_status()
        print(enemy_status)
    boss_status = Boss.give_status()
    print(boss_status)
    print(VERTICAL_LINE)

def select_direction(pos:Entity_module.Vector2) -> int:
    """
    方向を入力する関数
    """
    direction = None
    direction_num = None
    while True:
        direction = input("進む方向を入力してください(W,A,S,D)：")
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
    print(color.RED+"YOU LOSE!! To be continued..."+color.END)
    sys.exit()

#テスト
# file_path = "test.txt"
# file_check(file_path)
# load_dungeon(file_path)