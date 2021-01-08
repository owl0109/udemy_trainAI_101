from train.lesson1 import cal, variable
from train.lesson2 import structure
from train.lesson3 import multiple_cal
from train.lesson4 import control
from train.lesson5 import func


# variable=>変数について
# cal => 四則演算について
# structure => 基本構文について
# multiple_cal => 複数の変数を扱う(配列：リスト,タプル,辞書)
# control => 制御文
# func => 関数について
def start():
    variable.var_sample()
    cal.cal_sample()
    structure.structure_sample()
    multiple_cal.multiple_cal_sample()
    control.control_sample()
    func.func_sample()