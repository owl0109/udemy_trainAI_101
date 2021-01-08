def structure_sample():
    print("##########structure##########")
    num = 3
    '''
    a < b：bのほうが大きい値の時「true」
    a <= b：bがa以上の値の時「true」
    a => b：bがa以下の値の時「true」
    a > b：bのほうが値が小さい時
    a == b：aとbがイコールの時
    a != b：aとbの値が異なる時
    '''
    if num < 2:
        print(str(num) + "は2より小さい値")
    else:
        print(str(num) + "は2以上の値")

    # \nで改行　\tでタブ
    print('test1\ntest2\n\tタブ1\n\tタブ2')
