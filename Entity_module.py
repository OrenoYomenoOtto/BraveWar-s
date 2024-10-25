# coding: utf-8

class Entity:
    def __init__(self,name:str,level:int):
        self.__name = name
        self.__level = level

    @property
    def name(self):
        """
        nameのgetterメソッド
        """
        return self.__name
    
    @property
    def level(self):
        """
        levelのgetterメソッド
        """
        return self.__level


class Player(Entity):
    def __init__(self, name:str, level:int):
        super().__init__(name, level)
        self.__move_count = 0
        self.__isAlive = True

    @property
    def move_count(self):
        """
        move_countのgetterメソッド
        """
        return self.__move_count
    
    @property
    def isAlive(self):
        """
        isAliveのgetterメソッド
        """
        return self.__isAlive
    
    def level_up(self,level:int):
        self.__level += level

    def raise_move_counter(self):
        self.__move_count += 1

    def battle(self,E_level:int):
        """
        戦闘を行う関数\n
        引数 E_level : 敵のlevel\n
        具体的な処理 \n
        playerの生死状態を行う。
        """
        if self.__level >= E_level:
            self.__isAlive = False


class Enemy(Entity):
    def __init__(self, name:str, level:int, isBoss:bool):
        super().__init__(name, level)
        self.__isBoss = isBoss

    @property
    def isBoss(self):
        return self.__isBoss


#テスト
player = Player("勇者",10)
enemy1 = Enemy("雑魚",5,False)
enemy2 = Enemy("雑魚",20,False)

player.battle(enemy1.level)
print(player.isAlive)
player.battle(enemy2.level)
print(player.isAlive)