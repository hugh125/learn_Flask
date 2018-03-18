# -*- conding:utf-8 -*-
'''
# 12345 67890
# BCACA CDABA

def myReturn(str):
    if str == 'A':
        return 'A'
    elif str == 'B':
        return 'B'
    elif str == 'C':
        return 'C'
    elif str == 'D':
        return 'D'
    else:
        return 'NULL'
def No01(str):
    return str

def No02(str):
    pass
    if str == 'A':
        No05('C');
    if str == 'B':
        No05('D');
    if str == 'C':
        No05('A');
    if str == 'D':
        No05('B');

def No03():
    str_A = No03()
    str_B = No06()
    str_C = No02()
    str_D = No04()
    if str_B == str_C and str_B ==str_D:
        return 'A'
    if str_A == str_C and str_A ==str_D:
        return 'B'
    if str_A == str_B and str_A ==str_D:
        return 'D'
    if str_A == str_B and str_A ==str_C:
        return 'D'
    pass

def No04():

    pass

def No05(str):
    if No08() == No05():
        return 'A'

def No06(str):
    if No08() == No02() == No04():
        return 'A'
    if No08() == No01() == 'B':
        return 'B'
    if No08() == No03() == No10():
        return 'C'
    if No08() == No05() == No09():
        return 'D'

    pass

def No07():
    pass

def No08():
    pass

def No09():
    if No01('A') == No06('A'):pass

    pass

def No10():
    pass

strAnswer = []
if __name__ == '__main__':
    pass
    print(strAnswer)
    print('--------------------------------------')

    for i in range(10):
        str = (chr(i // 4 + ord('A')))
        strAnswer.append(str)
    print(strAnswer, '\n')

    myset = set(strAnswer)
    for item in myset:
        print('the %c has found %d' %(item, strAnswer.count(item)))
'''
def judge(x) -> bool:
    print(x)
    minS = min('0123', key=x.count)
    maxS = max('0123', key=x.count)

    return True
    n = [int(i) for i in x]
    select2 = '2301'
    if select2[n[1]] != x[4]:
        return False
    select3 = '2513'
    temp = select3.replace(select3[n[2]], '')
    if x[int(select3[n[2]])] in [x[int(i)] for i in temp]:
        return False

    select4 = [(0, 4), (1, 6), (0, 8), (5, 9)]
    temp = select4[n[3]]
    if x[temp[0]] != x[temp[1]]:
        return False

    select5 = '7386'
    if x[int(select5[n[4]])] != x[4]:
        return False

    select6 = [(1, 3), (0, 5), (2, 9), (4, 8)]
    temp = select6[n[5]]
    if x[temp[0]] != x[7] or x[temp[1]] != x[7]:
        return False

    select7 = '2103'
    if select7[n[6]] != minS:
        return False

    select8 = '6419'
    if abs(int(select8[n[7]]) - int(x[0])) == 1:
        return False

    select9 = '5918'
    temp = x[int(select9[n[8]])] == x[4]
    if (x[0] == x[5]) == temp:
        return False

    select10 = '3241'
    if (x.count(maxS) - x.count(minS)) != int(select10[n[9]]):
        return False
    return True

def to4(x):
    mylist = ['123456789']
    zhengchu = x // 4
    yushu = x % 4
    #print(x, ret, iter(x))
    print('源数字 %d \t 整除 %d \t 余数 %d' %(x, zhengchu, yushu))

    return mylist
    #print(x)
    #return ['AAAAAAAAAA']
    #return ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
    pass

import math
for x in range(int(math.pow(4, 3))):
    '''     x = to4(x)
     '''
    x = to4(x)
    #print(''.join([chr(65 + int(3))]))
    # if judge(x):
    #     print(''.join([chr(65 + int(i)) for i in x]))
for i in ['123456789']:
    print(i)
