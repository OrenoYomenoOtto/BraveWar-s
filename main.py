# coding: utf-8

from typing import Final, Tuple
import IO_module
import Entity_module 


ENTITY_CONFIG: Final[str] = "Entity_config.ini"
TOTAL_LAYER_NUM: Final[int] = 2 
FILE_PATH: Tuple[str] = ("Entity_module.py", "Entity_config.ini","IO_module.py","Flavor.json","exp.txt")
MAP_WIDTH_SIZE: Final[int] = 5
MAP_HIGHT_SIZE: Final[int] = 5



def create_braver(data: list) -> Entity_module.Braver:
    """
    braverオブジェクトを作成する関数
    """
    braver = Entity_module.Braver(data[0]["Id"], data[0]["Name"], data[0]["Level"], data[0]["Pos_x"], data[0]["Pos_y"] )
    return braver

def create_boss(data: list) -> Entity_module.Enemy:
    """
    bossオブジェクトを作成する関数
    """
    boss = Entity_module.Enemy(data[0]["Id"], data[0]["Name"], data[0]["Level"], data[0]["Pos_x"], data[0]["Pos_y"], True)
    return boss

def create_enemies(data: list) -> list:
    """
    enemyオブジェクトを作成する関数
    """
    enemies = []
    for i in range(len(data)):
        enemies.append(Entity_module.Enemy(data[i]["Id"], data[i]["Name"], data[i]["Level"], data[i]["Pos_x"], data[i]["Pos_y"], False))
    return enemies

def create_items(data: list) -> list:
    """
    itemオブジェクトを作成する関数
    """
    items = []
    for i in range(len(data)):
        items.append(Entity_module.Item(data[i]["Id"], data[i]["Name"], data[i]["Level"], data[i]["Pos_x"], data[i]["Pos_y"]))
    return items

def create_dungeon(boss_data: list, enemy_data: list, item_data: list):
    """
    dungeonオブジェクトとその階層に関連するオブジェクトを作成する関数
    """
    dungeon = Entity_module.Dungeon(MAP_WIDTH_SIZE,MAP_HIGHT_SIZE)
    boss = create_boss(boss_data)
    enemies = create_enemies(enemy_data)
    items = create_items(item_data)
    return dungeon, boss, enemies ,items

def set_entities(dungeon: Entity_module.Dungeon, braver:Entity_module.Braver, boss: Entity_module.Enemy, enemies: list, items: list)-> None:
    """
    entityをdungeonに配置する関数
    """
    dungeon.set_Entity(braver)
    for enemy in enemies:
        dungeon.set_Entity(enemy)
    for item in items:
        dungeon.set_Entity(item)
    dungeon.set_Entity(boss)

def Search_Dungeon(boss_data: list, enemy_data: list, item_data: list):
    """
    Dungeonを探索するpartをまとめた関数
    """
    dungeon, Boss, Enemies, Items = create_dungeon(boss_data, enemy_data, item_data)
    set_entities(dungeon, Player, Boss, Enemies, Items)
    while True:
        #Dungeon, playerのstatus, enemiesのstatusの表示
        IO_module.show_dungeon(dungeon.draw_map())
        IO_module.print_status(Player.give_status())
        IO_module.print_enemies_status(Enemies, Boss)
        #playerを盤から浮かす
        dungeon.delete_Entity(Player)
        #playerを動かし(浮いた状態), counterを増加する
        Player.move()
        Player.proceed_move_counter()
        #playerが別Entityと衝突の有無とplayerの現在地を取得する。衝突の有無で場合分けする
        isCollision, current_pos = dungeon.collision_Entity(Player)
        if isCollision == True:
            #衝突したEntityを取得してEntityの種類で場合分けする
            Collision_Entity = dungeon.get_Entity(current_pos)
            if type(Collision_Entity) is Entity_module.Enemy:
                #Enemyと戦闘が発生しplayerの生死状態を変更する
                Player.battle(Collision_Entity)
                if Player.get_isAlive != True:
                    IO_module.display_flavor_text(flavor_data, "Battle_BraverLose", "scene1")
                    IO_module.lose_game() 
                #EnemyがBossではない場合
                if Collision_Entity.get_isBoss != True:
                    IO_module.display_flavor_text(flavor_data, "Battle_BraverWin", "scene1")
                    Player.level_up(Collision_Entity.get_level)
                    Enemies.remove(Collision_Entity)
                #Bossの場合ループを抜ける
                elif Collision_Entity.get_isBoss == True:
                    if Player.get_isAlive != True:
                        IO_module.display_flavor_text(flavor_data, "BossBattle_BraverLose")
                        break
                    elif Player.get_isAlive == True:
                        IO_module.display_flavor_text(flavor_data, "BossBattle_BraverWin")
                        break
            #Itemを取得した場合
            elif type(Collision_Entity) is Entity_module.Item:
                IO_module.display_flavor_text(flavor_data, "Item")
                Player.level_up(Collision_Entity.get_level)
        #playerを盤の移動先に打つ
        dungeon.set_Entity(Player)

def game_result(braver: Entity_module.Braver, info: list) -> None:
    move_frequency: Final[int] = braver.get_move_count
    kill_num: Final[int] = braver.get_kill_board
    Shortest_steps_num = 0
    Bad_guys_num = 0
    isFaster = False
    isGenocide = False    
    for i in range(len(info)):
        Shortest_steps_num += info[i]["Shortest"]
        Bad_guys_num += info[i]["total_enemy"]
    if move_frequency == Shortest_steps_num:
        isFaster = True
    if kill_num == Bad_guys_num:
        isGenocide = True
    IO_module.out_result(isGenocide, isFaster)
    





#<--main-->

#FileCheck
for i in range(len(FILE_PATH)):
    IO_module.file_check(FILE_PATH[i])

#FileLoad
flavor_data: Final[dict] = IO_module.load_json("Flavor.json")
player_data: Final[list] = IO_module.load_Entities(ENTITY_CONFIG, "BRAVER", "Braver")
enemy_data: Final[list] = []
item_data: Final[list] = []
boss_data: Final[list] = []
dungeon_info_data: Final[list] = IO_module.load_dungeon_info(ENTITY_CONFIG)
for i in range(TOTAL_LAYER_NUM):
    enemy_data.append(IO_module.load_Entities(ENTITY_CONFIG, f"DUNGEON{i}_ENEMIES", "Enemy"))
    item_data.append(IO_module.load_Entities(ENTITY_CONFIG, f"DUNGEON{i}_ITEMS", "Item"))
    boss_data.append(IO_module.load_Entities(ENTITY_CONFIG, f"DUNGEON{i}_BOSS", "Boss"))

#playerの初期化,インスタンス化
Player = create_braver(player_data)

#説明テキストの出力
IO_module.print_exp("exp.txt")

for i in range(TOTAL_LAYER_NUM):
    Search_Dungeon(boss_data[i], enemy_data[i], item_data[i])
    Player.init_pos()
game_result(Player, dungeon_info_data)
IO_module.out_fin_txt()
