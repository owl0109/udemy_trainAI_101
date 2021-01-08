def var_sample():
    print("##########variable##########")
    name = 'KIJIMA'
    num = 123
    flo = 1.23

    printer(name)
    printer(num)
    printer(flo)


def printer(var):
    # 変数を表示
    print(var)
    # 変数の型を表示
    print((type(var)))
