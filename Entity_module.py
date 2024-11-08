# coding: utf-8

import enum 
from typing import Final
import IO_module


class Vector2:
    """
    x,y成分をまとめたクラス
    メンバはprivateで__x, __yを持つ
    """
    def __init__(self, x:int, y:int) -> None:
        self.__x = x
        self.__y = y

    @property
    def get_x(self) -> int:
        """
        xを取得するメソッド
        """
        return self.__x
    
    @property
    def get_y(self) -> int:
        """
        yを取得するメソッド
        """
        return self.__y
    
    @get_x.setter
    def set_x(self, x: int) -> None:
        """
        xをセットするメソッド
        ※取り扱い注意
        """
        self.__x = x

    @get_y.setter
    def set_y(self, y: int) -> None:
        """
        yをセットするメソッド
        ※取り扱い注意
        """
        self.__y = y

    def set_vector2(self, x: int, y: int):
        self.__x = x
        self.__y = y


class Direction(enum.IntEnum):
    W = 0
    S = 1
    A = 2
    D = 3


class Entity:
    """
    エンティティの設計書、使用する場合は継承してください。
    メンバはprivateで __name, __level, vector2を持つ。
    """
    def __init__(self, Id:str, name:str, level:int, x:int, y:int) -> None: 
        self.__Id: Final[str]= Id
        self.__name: Final[str] = name
        self.__level: Final[int] = level
        self.vector2 = Vector2(x,y)

    @property
    def get_Id(self) -> str:
        """
        Idを取得するメソッド
        """
        return self.__Id

    @property
    def get_name(self) -> str:
        """
        nameを取得するメソッド
        """
        return self.__name

    @property
    def get_level(self) -> int:
        """
        levelを取得するメソッド
        """
        return self.__level
        
    @property
    def get_vector2(self) -> Vector2:
        """
        Vector2を取得するメソッド
        """
        return self.vector2

    @get_level.setter
    def set_level(self, level:int) -> None:
        """
        levelをセットするメソッド
        ※取り扱い注意
        """
        self.__level = level


class Braver(Entity):
    """
    勇者の設計書、エンティティを継承してます。
    メンバはprivateで __name, __level, vector2, __isAlive, __move_countを持つ。
    """
    def __init__(self, Id: str, name: str, level: int, x: int, y: int) -> None:
        super().__init__(Id, name, level, x, y)
        self.__iniPosX: Final[int] = x
        self.__iniPosY: Final[int] = y
        self.__isAlive = True
        self.__move_count = 0 

    @property
    def get_isAlive(self) -> bool:
        """
        isAliveを取得するメソッド
        """
        return self.__isAlive
    
    @property
    def get_move_count(self) -> int:
        """
        move_countを取得するメソッド
        """
        return self.__move_count
    
    def proceed_move_counter(self) -> None:
        """
        move_counterを1増加させる
        """
        self.__move_count += 1
    
    def level_up(self, level:int) -> None:
        """
        braverのlevelを変更する
        """
        Re_level = self.get_level + level
        self.set_level = Re_level

    def battle(self, enemy:Entity) -> None:
        """
        戦闘を行うメソッド
        相手のlevelと比較を行い、braverの生死を返す
        """
        Enemy_Level: Final[int] = enemy.get_level
        if self.get_level <= Enemy_Level:
            self.__isAlive = False
        IO_module.print_start_battle(enemy, self.__isAlive)

    def move(self) -> None:
        """
        braverの座標を変更するメソッド
        """
        direction_num = IO_module.select_direction(self.vector2)
        if direction_num ==Direction.W:
            y_pos = self.vector2.get_y -1
            self.vector2.set_y = y_pos
        elif direction_num == Direction.S:
            y_pos = self.vector2.get_y +1
            self.vector2.set_y = y_pos
        elif direction_num == Direction.A:
            x_pos = self.vector2.get_x -1
            self.vector2.set_x = x_pos
        elif direction_num == Direction.D:
            x_pos = self.vector2.get_x +1
            self.vector2.set_x = x_pos

    def init_pos(self) -> None:
        """
        playerの位置を設定値に変える
        """
        self.vector2.set_vector2(self.__iniPosX, self.__iniPosY )

    def give_status(self) -> str:
        """
        braverのstatusをstrで渡すメソッド
        """
        return self.get_name+ "\nレベル:" + str(self.get_level) + "\n移動回数" + str(self.get_move_count) 


class Enemy(Entity):
    def __init__(self, Id: str, name: str, level: int, x: int, y: int, isBoss: bool) -> None:
        super().__init__(Id, name, level, x, y)
        self.__isBoss = isBoss

    @property
    def get_isBoss(self) -> bool:
        return self.__isBoss
    
    def give_status(self) ->str:
        return self.get_Id+ " " + self.get_name + " レベル: " + str(self.get_level) 


class Item(Entity):
    def __init__(self, Id: str, name: str, level: int, x: int, y: int) -> None:
        super().__init__(Id, name, level, x, y)


class Dungeon:
    VERTICAL_LINE: Final[str] = "+---"
    HORIZON_LINE: Final[str] = "|"
    LINE_END: Final[str] = "+"
    EMPTY_SQUARE :Final[str] = "   "
    
    def __init__(self, width:int, hight:int ) -> None:
        self.__width: Final[int] = width
        self.__hight: Final[int] = hight
        self.__map = [["" for j in range(self.__hight)] for i in range(self.__width)]

    @property
    def get_width(self) -> int:
        return self.__width
    
    @property
    def get_hight(self) -> int:
        return self.__hight
    
    @property
    def get_map(self) -> list:
        return self.__map
    
    def collision_Entity(self, entity:Entity) -> bool:
        isCollision = False
        pos = entity.get_vector2
        pos_x: Final[int] = pos.get_x
        pos_y: Final[int] = pos.get_y    
        if self.__map[pos_y][pos_x] != "":
            isCollision = True
        return isCollision, pos
    
    def get_Entity(self, pos:Vector2) -> Entity:
        pos_x: Final[int] = pos.get_x
        pos_y: Final[int] = pos.get_y
        return self.__map[pos_y][pos_x]    

    def set_Entity(self, entity:Entity) -> None:
        pos = entity.get_vector2
        pos_x: Final[int] = pos.get_x
        pos_y: Final[int] = pos.get_y    
        self.__map[pos_y][pos_x] = entity

    def delete_Entity(self, entity:Entity) -> None:
        pos = entity.get_vector2
        pos_x: Final[int] = pos.get_x
        pos_y: Final[int] = pos.get_y    
        self.__map[pos_y][pos_x] = ""

    def draw_map(self) -> list:
        dungeon_map = [] 
        vertical_lines: Final[str] = Dungeon.VERTICAL_LINE * self.__width + Dungeon.LINE_END
        for i in range(self.__hight*2):
            if i%2 == 0:
                dungeon_map.append(vertical_lines)
            elif i%2 == 1:
                vertical_squares = ""
                for j in range(self.__width*2):
                    if j%2 == 0:
                        vertical_squares += Dungeon.HORIZON_LINE
                    elif j%2 == 1:
                        if self.__map[i//2][j//2] != "":
                            if 1 == len(self.__map[i//2][j//2].get_Id):
                                vertical_squares += self.__map[i//2][j//2].get_Id+"  "
                            else:
                                vertical_squares += self.__map[i//2][j//2].get_Id+" "
                        else:
                            vertical_squares += Dungeon.EMPTY_SQUARE
                vertical_squares += Dungeon.HORIZON_LINE
                dungeon_map.append(vertical_squares)
        dungeon_map.append(vertical_lines)
        return dungeon_map
                
