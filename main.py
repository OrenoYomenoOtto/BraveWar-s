# coding: utf-8

import random
from typing import Final, Tuple
import IO_module
import Entity_module 


FILE_PATH: Tuple[str] = ("Entity_module.py", "Entity_config.ini","IO_module.py","Flavor.json")

#FileCheck
for i in range(len(FILE_PATH)):
    IO_module.file_check(FILE_PATH[i])

#FileLoad
flavor_data = IO_module.load_json("Flavor.json")
player_data = IO_module.load_Entities("Entity_config.ini", "BRAVER", "Braver")
enemy_data_01 = IO_module.load_Entities("Entity_config.ini", "DUNGEON01_ENEMIES", "Enemy")
enemy_data_02 = IO_module.load_Entities("Entity_config.ini", "DUNGEON02_ENEMIES", "Enemy")
item_data_01 = IO_module.load_Entities("Entity_config.ini", "DUNGEON01_ITEMS", "Item")
item_data_02 = IO_module.load_Entities("Entity_config.ini", "DUNGEON02_ITEMS", "Item")

#playerの初期化、オブジェクトの作成
Player = Entity_module.Braver(player_data["Id"], player_data["Name"], player_data["Level"], player_data["Pos_x"], player_data["Pos_y"] )

#Enemiesの初期化、オブジェクトの作成
Enemies = []
for i in range(len(enemy_data_01)):
    Enemies.append(Entity_module.Enemy(enemy_data_01[i]["Id"],enemy_data_01[i]["Name"],enemy_data_01[i]["Level"],enemy_data_01[i]["Pos_x"],enemy_data_01[i]["Pos_y"],False))

# """ダンジョンの初期化"""
dungeon = Entity_module.Dungeon()


# """ダンジョンの盤を表示"""
# Dungeon, DUNGEON_WIDTH, DUNGEON_HIGHT = IO_module.load_dungeon()



# IO_module.show_dungeon()
# """ダンジョンの１階層のループ"""
# #to_move = player()
# while True:
#     IO_module.print_status(Player.give_status())
#     Player.move()
#     Player.proceed_move_counter()   
#     if False == Player.get_isAlive():
#         IO_module.lose_game()

    

# """終了報告"""
# if get_result == escaped:
#     print("Clear: Congratulations! You escaped!")
# elif get_result == happy_end:
#     print("Clear: Congratulations! You escaped! and You married a princess.")
# else:
#     print("Error: No Result")