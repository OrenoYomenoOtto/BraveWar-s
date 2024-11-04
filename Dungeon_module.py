# coding: utf-8

import Entity_module


class Dungeon:
    

    

    def draw_map(self) -> str:
        width_line = "-"
        hight_line = "|"
        cross_line = "+"

        return 
    
    def test_print(self):
        return self.__map
 


dungeon = Dungeon(3, 3)
player = Entity_module.Braver("PLAYER", 20, 1, 1)
print(dungeon.test_print())
dungeon.set_Entity(player.get_vector2.get_y, player.get_vector2.get_x)
print(dungeon.test_print())

"""
+---+---+---+---+---+
 | m2 | m5 | m9 |       |  G   |       
+---+---+---+---+---+
 | m1 | m6 |  I1 |       |       |
+---+---+---+---+---+
 | m3 | m7 |  I2 |       |       |
+---+---+---+---+---+
 | m4 | m8 |       |       |       |
+---+---+---+---+---+
 |  S   |       |       |       |       |
+---+---+---+---+---+

"""