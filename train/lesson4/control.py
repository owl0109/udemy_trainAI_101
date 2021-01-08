def control_sample():
    print('==========control==========')
    names = ['鈴木', '佐藤', '田中']
    num = 0
    # ===fro文(ループ)===
    for i in range(5):
        print('Hello' + str(i))

    for name in names:
        print(name)

    # ===if文(条件分岐)===
    if num > 0:
        print('値は正数です')
    elif num == 0:
        print('値は0です')
    else:
        print('値は負の数です')
