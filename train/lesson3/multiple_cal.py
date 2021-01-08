def multiple_cal_sample():
    print("##########multiple_cal##########")
    #  ===リスト===
    numbers = [1, 2, 3, 4, 5]
    names = []

    # リストは0が最初
    print(numbers[0])
    # 「0:3」で0から3番目を表示(1,2,3と出力される)
    print(numbers[0:3])
    # 「:2」最初から[1]まで
    print(numbers[:2])
    # 「2:」[3]から全部取り出して
    print(numbers[2:])

    print(names)
    # .appendで追加
    names.append('test1')
    names.append('test2')
    print(names)
    # removeで削除
    names.remove('test2')
    print(names)

    # ===タプル===
    t = (2, 3, 4, 5, 6)
    print(t[0])
    print(t[0:3])
    # t[0] = 0 タプルは上書き不可。

    # ===辞書===
    result = {'数学': 90, '英語': 50, '理科': 60}
    print(result)
    print(result['数学'])
