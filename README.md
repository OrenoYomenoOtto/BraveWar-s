# BraveWar-s

## 作成するファイル
- Enthity_module.py
- Enthity.ini
- Battle_module.py
- Dungeon_module.py
- Dungeon.txt
- Event_module.py
- Flaver.json
- FLAG_module.py
- FLAG.ini
- IO_module.py
- main.py

## 各ファイルの内容
### Enthity_module.py
エンティティクラス,プレイヤークラス,敵クラス,Bossクラスの４つを記述したファイル。

プレイヤークラス,敵クラス,Bossクラスはエンティティクラスを親クラスとして継承する。

メンバ変数はプロテクト変数にして記述する,またsetterメソッドgetterメソッドを用意する。

※pythonでは変数の前に"_"を入れるとproteced変数に,またsetter,getterメソッドはデコレータで用意されているそうです...
#### 必要なモジュール,ファイル
- Enthity.ini
- configparser
- os
- errno
- Enum

#### Class Direction(Enum)
※移動方向をEnum型で扱う
- W = 0
- S = 1
- A = 2
- D = 3

#### Class Enthity
- _level :int
- _name  :str
- \_\_init\_\_(level,name)  protectedでそれぞれ設定
- int level()      レベルを参照する関数　@property
- void level(int)  レベルを設定・変更する関数　@level.setter
- str naem()       名前を参照する関数  @property
- void name(str)   名前を設定・変更する関数   @name.setter

#### Class Player
- _move  :int
- \_\_init\_\_(level,name)  Enthityを継承
- int move(str)       ダンジョンを移動する関数
- void move()
- void level_up(int)  levelを変更する関数

#### Class Enemy
- \_\_init\_\_(level,name)  Enthityを継承

※特に新しい関数がないので継承だけ....意味ないですね(´;ω;｀)

#### Class Boss
void Flavor()

### Enthity.ini
プレイヤー,敵,Bossの初期値をまとめたの設定ファイル

### Battle_module.py
戦闘に関する関数等をまとめたファイル
- bool CanYouBeatMe(int,int)  戦闘結果を返す関数
- void Battle()               戦闘時のテキスト出力と戦闘後の処理を行う関数
 
### Flavor_module.py
Flavor.jsonを読み取り、タイミングで使用するファイル

### Flavor.json
フレーバーテキストを辞書型でまとめた設定ファイル

### main.py
これで実行



