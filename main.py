# coding: utf-8

import random
from typing import Final, Tuple
import IO_module
import Entity_module 

FILE_PATH: Tuple[str] = ("Entity_module.py", "Entity_config.ini","IO_module.py","Flavor.json","Enemy_list.json")

#FileCheck
for i in range(len(FILE_PATH)):
    IO_module.file_check(FILE_PATH[i])

#FileLoad
flavor_data = IO_module.load_json("Flavor.json")
player_data = IO_module.load_Entities("Entity_config.ini", "BRAVER", "Braver")
enemy_data_01 = IO_module.load_Entities("Entity_config.ini", "DUNGEON01_ENEMIES", "Enemy")
enemy_data_02 = IO_module.load_Entities("Entity_config.ini", "DUNGEON01_ENEMIES", "Enemy")
item_data_01 = IO_module.load_Entities("Entity_config.ini", "DUNGEON01_ITEMS", "Item")
item_data_02 = IO_module.load_Entities("Entity_config.ini", "DUNGEON01_ITEMS", "Item")

Player = Entity_module.Braver(player_data["Id"], player_data["Name"], player_data["Level"], player_data["Pos_x"], player_data["Pos_y"] )

for i in range(len(enemy_data_01)):
    

# """ダンジョンの初期化"""
# dungeon_board = []

# """ダンジョンの盤を表示"""
# Dungeon, DUNGEON_WIDTH, DUNGEON_HIGHT = IO_module.load_dungeon()

# """敵の初期化"""
# enemy_list, enemy_counter  = IO_module.load_enemy_pos_list(Dungeon, DUNGEON_WIDTH, DUNGEON_HIGHT)

# for i in range(enemy_counter):
#     enemy_id = enemy_data_01_floor[i].get("id")
#     enemy_level = enemy_data_01_floor[i].get("level")
#     Entity_module.Enemy(enemy_id, enemy_level, enemy_list[1], enemy_list[2], False)



# for i in range(enemy_counter):
#     enemy_name, enemy_level = IO_module
#     enemy = Entity_module.Enemy(enemy_list[i][0], enemy_list[i][1], enemy_list[i][2], False)
    

# IO_module.show_dungeon()
# """ダンジョンの１階層のループ"""
# #to_move = player()
# while True:
#     IO_module.print_status(Player.give_status())
#     Player.move()
#     Player.proceed_move_counter()   
#     if False == Player.get_isAlive():
#         IO_module.lose_game()

    

"""終了報告"""
if get_result == escaped:
    print("Clear: Congratulations! You escaped!")
elif get_result == happy_end:
    print("Clear: Congratulations! You escaped! and You married a princess.")
else:
    print("Error: No Result")