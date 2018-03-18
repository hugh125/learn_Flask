#! /usr/bin/python
# -*- coding:utf-8 -*-
#http://www.cnblogs.com/yupeng/p/3414820.html

def GetCurTime():
    import time
    #time.sleep(0.234)
    return time.strftime("%y-%m-%d %H:%M:%S.", time.localtime())

def bubble_sort(l):
    flag = True
    for i in range(len(l) - 1, 0, -1):
        if flag:
            flag = True
            for j in range(i):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    flag = True
        else:
            break
    print('bubble_sort:\t', GetCurTime(), l)

def MyBubble_sort(mylist):
    for i in range(0, len(mylist)):
        for j in range(len(mylist) - 1, i, -1):
            if mylist[j] < mylist[j - 1]:
                mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]
    print('MyBubble_sort:\t', GetCurTime(), mylist)

def selection_sort(mylist):
    for i in range(0, len(mylist)):
        min = i
        for j in range(i+1, len(mylist)):
            if mylist[j] < mylist[min]:
                min = j
        mylist[i], mylist[min] = mylist[min], mylist[i]
    print('selection_sort:\t', GetCurTime(), mylist)

def insertion_sort(mylist):
    for i in range(1, len(mylist)):
        save = mylist[i]
        j = i
        while j > 0 and mylist[j - 1] > save:
            mylist[j] = mylist[j - 1]
            j -= 1
            #print('insertion_sort:\t', GetCurTime(), mylist)
        mylist[j] = save
    print('insertion_sort:\t', GetCurTime(), mylist)

def sub_sort(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low

def quick_sort(array, low, high):
    if low < high:
        key_index = sub_sort(array, low, high)
        quick_sort(array, low, key_index)
        quick_sort(array, key_index + 1, high)

def BinarySerch(array, low, high, key):
    index = -10
    mid = (low + high) // 2
    if array[mid] == key:
        index = key
    if (array[mid] < key) and (low < high):
        index = BinarySerch(array, mid + 1, high, key)
    if (array[mid] > key) and (low < high):
        index = BinarySerch(array, low, high - 1, key)
    return index

if __name__ == '__main__':
    pass
    _9_9 = '\n'.join(['\t'.join(['%d*%d=%d' %(x, y, x*y) for y in range(1, (x+1))]) for x in range(1, 10)])
    #print(_9_9, '\n\n')
    li = [21, 44, 2, 45, 33, 4, 3, 7, 67, 6]
    print('src_sort:\t\t', GetCurTime(), li)
    print('len(mylist) = ', len(li))
    #bubble_sort(li)
    #MyBubble_sort(li)
    #selection_sort(li)
    insertion_sort(li)

    array = [8, 10, 9, 6, 4, 16, 5, 13, 26, 18, 45, 34, 17, 2, 23, 1, 7, 3]
    print(array)
    quick_sort(array, 0, len(array) - 1)
    print(array)

    arrayBinary = [3, 2, 1, 34, 56, 57, 78, 86, 45]
    print(arrayBinary)
    print(BinarySerch(arrayBinary, 54))