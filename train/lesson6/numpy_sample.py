import numpy as np


def start():
    # 計算：numpy
    # データの入力
    x = np.array([1, 2, 3])
    y = np.array([2, 3.9, 6.1])

    # データの中心化
    # 平均の算出 =>.mean
    # 中心化 [-1,0,1][-2,-0.1,2.1]
    xc = x - x.mean()
    yc = y - y.mean()

    # パラメータa(傾き)の計算
    # 要素ごとの掛け算(要素積)xc[0]*yc[0],xc[1]*yc[1]...
    xx = xc * xc
    xy = xc * yc

    # 要素ごとの計算結果(xxとxc)を全要素足す(.sum())
    # その後、傾きを求める(xy.sum()/xx.sum())
    a = xy.sum() / xx.sum()
    print(a)
