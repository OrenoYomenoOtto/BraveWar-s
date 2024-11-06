# coding: utf-8

import random
from typing import Final, Tuple
import IO_module
import Entity_module 
import sys

ENTITY_CONFIG: Final[str] = "Entity_module.py" 
FILE_PATH: Tuple[str] = ("Entity_module.py", "Entity_config.ini","IO_module.py","Flavor.json")
MAP_WIDTH_SIZE: Final[int] = 5
MAP_HIGHT_SIZE: Final[int] = 5


#FileCheck
for i in range(len(FILE_PATH)):
    IO_module.file_check(FILE_PATH[i])

#FileLoad
flavor_data = IO_module.load_json("Flavor.json")
player_data = IO_module.load_Entities(ENTITY_CONFIG, "BRAVER", "Braver")
enemy_data_01 = IO_module.load_Entities(ENTITY_CONFIG, "DUNGEON01_ENEMIES", "Enemy")
enemy_data_02 = IO_module.load_Entities(ENTITY_CONFIG, "DUNGEON02_ENEMIES", "Enemy")
item_data_01 = IO_module.load_Entities(ENTITY_CONFIG, "DUNGEON01_ITEMS", "Item")
item_data_02 = IO_module.load_Entities(ENTITY_CONFIG, "DUNGEON02_ITEMS", "Item")
boss_data = IO_module.load_Entities(ENTITY_CONFIG, "DUNGEON_BOSS", "Boss")

#enemy_data[] = IO_module.load_Entit

#playerの初期化,インスタンス化
Player = Entity_module.Braver(player_data[0]["Id"], player_data[0]["Name"], player_data[0]["Level"], player_data[0]["Pos_x"], player_data[0]["Pos_y"] )

#Enemiesの初期化,インスタンス化
Enemies = []
for i in range(len(enemy_data_01)):
    Enemies.append(Entity_module.Enemy(enemy_data_01[i]["Id"],enemy_data_01[i]["Name"],enemy_data_01[i]["Level"],enemy_data_01[i]["Pos_x"],enemy_data_01[i]["Pos_y"],False))

#Bossの初期化,インスタンス化
Boss = Entity_module.Enemy(boss_data[0]["Id"], boss_data[0]["Name"], boss_data[0]["Level"], boss_data[0]["Pos_x"], boss_data[0]["Pos_y"], True)

#Itemの初期化,インスタンス化
Items = []
if type(item_data_01) is list:
    for i in range(len(item_data_01)):
        Items.append(Entity_module.Item(item_data_01[i]["Id"],item_data_01[i]["Name"],item_data_01[i]["Level"],item_data_01[i]["Pos_x"],item_data_01[i]["Pos_y"]))
else:
    Items.append(Entity_module.Item(item_data_01["Id"],item_data_01["Name"],item_data_01["Level"],item_data_01["Pos_x"],item_data_01["Pos_y"]))

#dungeonの初期化,インスタンス化
dungeon = Entity_module.Dungeon(MAP_WIDTH_SIZE,MAP_HIGHT_SIZE)



#dungeonにオブジェクトを配置
dungeon.set_Entity(Player)
for Item in Items:
    dungeon.set_Entity(Item)
for Enemy in Enemies:
    dungeon.set_Entity(Enemy)
dungeon.set_Entity(Boss)




"""ダンジョンの１階層のループ"""


while True:
    IO_module.show_dungeon(dungeon.draw_map())
    IO_module.print_status(Player.give_status())
    dungeon.delete_Entity(Player)
    Player.move()
    isCollision, current_pos = dungeon.collision_Entity(Player)
    if(isCollision == True):
        Collision_Entity = dungeon.get_Entity(current_pos)
        Player.battle(Collision_Entity.get_level)
        if False == Player.get_isAlive:
            IO_module.lose_game() 
        if type(Collision_Entity) is Entity_module.Enemy:
            if Collision_Entity.get_isBoss == False:
                Player.level_up(Collision_Entity.get_level)
        elif type(Collision_Entity) is Entity_module.Item:
            Player.level_up(Collision_Entity.get_level)
    dungeon.set_Entity(Player)
    Player.proceed_move_counter()   

    

# """終了報告"""
# if get_result == escaped:
#     print("Clear: Congratulations! You escaped!")
# elif get_result == happy_end:
#     print("Clear: Congratulations! You escaped! and You married a princess.")
# else:
#     print("Error: No Result")