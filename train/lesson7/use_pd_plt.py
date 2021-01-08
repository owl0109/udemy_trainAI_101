import pandas as pd
import matplotlib.pyplot as plt


def start():
    # データ操作：pandas
    # df：データフレーム
    # csvを読み込む
    df = pd.read_csv('./train/lesson7/sample.csv')

    # データの中心化(値ー平均値)
    df_c = df - df.mean()
    # 値が変わっていることを確認
    print(df.head(3))
    print(df_c.head(3))

    # meanの値がほぼ0になっていることを確認する
    # e-15 => 10の-15乗。ほぼ0
    print(df_c.describe())

    # データの抽出
    # x=部屋の広さ,y=家賃
    x = df_c['x']
    y = df_c['y']

    # パラメータa(傾き)を求める
    xx = x * x
    xy = x * y
    a = xy.sum() / xx.sum()
    print(a)

    # 40平米の部屋について調べる
    x_new = 40
    mean = df.mean()
    print(mean['x'])

    # 中心化
    xc = x_new - mean['x']
    print(xc)

    # 単回帰分析による予測
    yc = a * xc
    print(yc)

    # 元のスケールの予測値
    y_hat = a * xc + mean['y']
    print(y_hat)

    # グラフの描画：matplot
    # 横軸をx 縦軸をyとして、散布図(scatter)をプロット
    # plotで線の表示
    # legend()で凡例の表示
    # showでグラフ表示
    plt.scatter(x, y, label='y')
    plt.plot(x, a * x, label='y_hat', color='red')
    plt.legend()
    plt.show()
