# coding: utf-8

import enum 
import IO_module


class Vector2:
    """
    x,y成分をまとめたクラス
    メンバはprivateで__x, __yを持つ
    """
    def __init__(self, x, y) -> None:
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
    def set_x(self, x) -> None:
        """
        xをセットするメソッド
        ※取り扱い注意
        """
        self.__x = x

    @get_y.setter
    def set_y(self, y) -> None:
        """
        yをセットするメソッド
        ※取り扱い注意
        """
        self.__y = y


class Direction(enum.Enum):
    W = 0
    S = 1
    A = 2
    D = 3


class Entity:
    """
    エンティティの設計書、使用する場合は継承してください。
    メンバはprivateで __name, __level, __x, __yを持つ。
    """
    def __init__(self, name:str, level:int, x:int, y:int) -> None: 
        self.__name = name
        self.__level = level
        self.vector2 = Vector2(x,y)

    @property
    def get_level(self) -> int:
        """
        levelを取得するメソッド
        """
        return self.__level
        
    @property
    def get_name(self) -> str:
        """
        nameを取得するメソッド
        """
        return self.__name
    
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

    @get_name.setter
    def set_name(self, name:str) -> None:
        """
        nameをセットするメソッド
        ※取り扱い注意
        """
        self.__name = name


class Braver(Entity):
    """
    勇者の設計書、エンティティを継承してます。
    メンバはprivateで __name, __level, __x, __y, __isAlive, __move_countを持つ。
    """
    def __init__(self, name: str, level: int, x:int, y:int) -> None:
        super().__init__(name, level, x, y)
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

    def battle(self, E_level:int) -> None:
        """
        戦闘を行うメソッド
        相手のlevelと比較を行い、braverの生死を返す
        """
        if self.get_level <= E_level:
            self.__isAlive = False

    def move(self) -> None:
        """
        braverの座標を変更するメソッド
        """
        direction_num = IO_module.select_direction(self.vector2)
        if direction_num ==Direction.W:
            y_pos = self.vector2.get_y -1
            self.vector2.set_y(y_pos)
        elif direction_num == Direction.S:
            y_pos = self.vector2.get_y +1
            self.vector2.set_y(y_pos)
        elif direction_num == Direction.A:
            x_pos = self.vector2.get_x -1
            self.vector2.set_x(x_pos)
        elif direction_num == Direction.D:
            x_pos = self.vector2.get_x +1
            self.vector2.set_x(x_pos)

    def give_status(self) -> str:
        """
        braverのstatusをstrで渡すメソッド
        """
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
