# coding: utf-8

import IO_module
import Entity_module


FILE_PATH = ["Entity_module.py", "Entity_config.ini","IO_module.py"]

#FileCheck
for i in range(len(FILE_PATH)):
    IO_module.file_check(FILE_PATH[i])

player_name, player_level = IO_module.load_player("Entity_config.ini")
Player = Entity_module.Braver(player_name, player_level,0,0)

