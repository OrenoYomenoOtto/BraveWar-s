# coding: utf-8

import enum 

class Vector2:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    @property
    def get_x(self) -> int:
        return self.__x
    
    @property
    def get_y(self) -> int:
        return self.__y


class Direction(enum.Enum):
    "W" = 0
    "S" = 1
    "A" = 2
    "D" = 3


class Entity:
    def __init__(self,name:str,level:int) -> None: 
        self.__name = name
        self.__level = level

    @property
    def get_level(self) -> int:
        return self.__level
        
    @property
    def get_name(self) -> str:
        return self.__name

    @get_level.setter
    def set_level(self, level:int) -> None:
        self.__level = level


class Braver(Entity):
    def __init__(self, name: str, level: int) -> None:
        super().__init__(name, level)
        self.__isAlive = True
        self.__move_count = 0 

    @property
    def get_isAlive(self) -> bool:
        return self.__isAlive
    
    @property
    def get_move_count(self) -> int:
        return self.__move_count
    
    def proceed_move_counter(self) -> None:
        self.__move_count += 1
    
    def level_up(self, level:int) -> None:
        Re_level = self.get_level + level
        self.set_level = Re_level

    def battle(self, E_level:int) -> None:
        if self.get_level <= E_level:
            self.__isAlive = False

    def show_status(self) -> str:
        return self.get_name+ "\nレベル:" + str(self.get_level) + "\n移動回数" + str(self.get_move_count) 


class Enemy(Entity):
    def __init__(self, name: str, level: int, isBoss: bool) -> None:
        super().__init__(name, level)
        self.__isBoss = isBoss

    @property
    def get_isBoss(self) -> bool:
        return self.__isBoss


class Item(Entity):
    def __init__(self, name: str, level: int) -> None:
        super().__init__(name, level)


#テスト
# player = Entity("真理",30)
# brave  = Braver("律",40)
# print(brave.show_status())
# brave.level_up(player.get_level)
