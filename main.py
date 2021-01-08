from train import call_train
from train.lesson6 import numpy_sample
from train.lesson7 import use_pd_plt

import pandas as pd
import matplotlib.pyplot as plt


# trainで学んだ内容を出力 「from train ...」と「call_train.start()」のコメントアウト解除で呼べる(lesson1～lesson5)
# numpy_sampleで学んだ内容を出力 「from train.lesson6 ...」と「numpy_sample.start()」をコメントアウトで呼べる(lesson6)
# use_pd_pltで学んだ内容を出力 「from train.lesson7 ...」と「use_pd_plt.start()」をコメントアウトで呼べる(lesson7)

# call_train.start()
# numpy_sample.start()
# use_pd_plt.start()


# 予測値を計算する関数
def predict(x):
    # 定数項(どうやって求めたかは、./train/lesson7と./train/lesson6の中身を参考に)
    a = 10069.022519284063
    xm = 37.62222
    ym = 145006.92036590326

    # 中心化
    xc = x - xm

    # 予測値の計算
    y_hat = a * xc + ym
    return y_hat


# 値が出力される
print(predict(40))
print(predict(30))

# 20くらいになると、外挿になるので、変な値が出力される
print(predict(20))
