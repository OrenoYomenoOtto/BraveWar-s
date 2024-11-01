# coding: utf-8

import enum 
import IO_module


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
    
    @get_x.setter
    def set_x(self, x) -> None:
        self.__x = x

    @get_y.setter
    def set_y(self, y) -> None:
        self.__y = y


class Direction(enum.Enum):
    W = 0
    S = 1
    A = 2
    D = 3


class Entity:
    def __init__(self, name:str, level:int, x:int, y:int) -> None: 
        self.__name = name
        self.__level = level
        self.vector2 = Vector2(x,y)

    @property
    def get_level(self) -> int:
        return self.__level
        
    @property
    def get_name(self) -> str:
        return self.__name
    
    @property
    def get_vector2(self) -> Vector2:
        return self.vector2

    @get_level.setter
    def set_level(self, level:int) -> None:
        self.__level = level

    @get_name.setter
    def set_name(self, name:str) -> None:
        self.__name = name


class Braver(Entity):
    def __init__(self, name: str, level: int, x:int, y:int) -> None:
        super().__init__(name, level, x, y)
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

    def move(self) -> None:
        direction_num = IO_module.select_direction(self.vector2)
        if direction_num ==Direction.W:
            self.vector2.set_y()
        elif direction_num == Direction.S:
            self.vector2.set_y()
        elif direction_num == Direction.A:
            self.vector2.set_x()
        elif direction_num == Direction.D:
            self.vector2.set_x()

    def give_status(self) -> str:
        return self.get_name+ "\nレベル:" + str(self.get_level) + "\n移動回数" + str(self.get_move_count) 


class Enemy(Entity):
    def __init__(self, name: str, level: int, x:int, y:int, isBoss: bool) -> None:
        super().__init__(name, level, x, y)
        self.__isBoss = isBoss

    @property
    def get_isBoss(self) -> bool:
        return self.__isBoss


class Item(Entity):
    def __init__(self, name: str, level: int) -> None:
        super().__init__(name, level)
