# coding: utf-8

import IO_module
import Entity_module 


FILE_PATH = ["Entity_module.py", "Entity_config.ini","IO_module.py"]

#FileCheck
for i in range(len(FILE_PATH)):
    IO_module.file_check(FILE_PATH[i])

"""プレイヤーの初期化"""
player_name, player_level = IO_module.load_player("Entity_config.ini")
Player = Entity_module.Braver(player_name, player_level,0,0)

"""ダンジョンの表示"""
def show_dungeon_board(board):
    IO_module.load_dungeon()

"""ダンジョンの初期化"""
dungeon_board = []
"""ダンジョンの表示"""
#show_dungeon(dungeon_board)
"""エネミーの初期化"""
#enemy = Enemy()
"""入力と終了条件の確認の繰り返し"""
#to_move = player
while True:
    IO_module.print_status(Player.give_status())
    
    Player.move()
    Player.proceed_move_counter()   
    if False == Player.get_isAlive():
        IO_module.lose_game()

    

#終了報告
