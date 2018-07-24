import random as r
import time

def selectionSort(nums):
    n = len(nums)
    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1,n):
            if nums[i] < nums[mp]:
                mp = i

        nums[bottom], nums[mp] = nums[mp], nums[bottom]
    return nums

def merge(a,b):
    index_a = 0
    index_b = 0
    c = []
    while index_a < len(a) and index_b < len(b):
        if a[index_a] <= b[index_b]:
            c.append(a[index_a])
            index_a = index_a + 1
        else:
            c.append(b[index_b])
            index_b = index_b + 1
    c.extend(a[index_a:])
    c.extend(b[index_b:])
    return c

def mergeSort(list):
    if len(list) == 0 or len(list) == 1:
        return list[:len(list)]

    halfway = len(list)//2
    list1 = list[0:halfway]
    list2 = list[halfway:len(list)]
    newlist1 = mergeSort(list1)
    newlist2 = mergeSort(list2)
    newlist = merge(newlist1, newlist2)
    return newlist

def bubblesort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def insertionSort(lst):
    for i in range(1, len(lst)):
        j=i
        while j>0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j-=1
    return lst


def quickSort(items):
    if len(items) > 1:
        pivot_index = len(items)//2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quickSort(smaller_items)
        quickSort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items

    return items

if __name__ == '__main__':

    ##selectionSort
    for c in range(0,3):
        lst = [r.randint(0, 100*(10**c)) for i in range(100*(10**c))]
        print('loop count : ', 100*(10**c))
        startTime = time.clock()
        selectionSort(lst)
        endTime = time.clock()
        elapsedTime = endTime - startTime
        print('The elapsed time for selectionSort is : ', elapsedTime)
    print('===================================================')
    ##mergesort
    for c in range(0,3):
        lst = [r.randint(0, 100*(10**c)) for i in range(100*(10**c))]
        print('loop count : ', 100*(10**c))
        startTime = time.clock()
        mergeSort(lst)
        endTime = time.clock()
        elapsedTime = endTime - startTime
        print('The elapsed time for mergeSort is : ', elapsedTime)


    print('===================================================')
   ##bubbleSort
    for c in range(0,3):
        lst = [r.randint(0, 100*(10**c)) for i in range(100*(10**c))]
        print('loop count : ', 100*(10**c))
        startTime = time.clock()
        bubblesort(lst)
        endTime = time.clock()
        elapsedTime = endTime - startTime
        print('The elapsed time for bubbleSort is : ', elapsedTime)

    print('===================================================')
   ##insertionSort
    for c in range(0,3):
        lst = [r.randint(0, 100*(10**c)) for i in range(100*(10**c))]
        print('loop count : ', 100*(10**c))
        startTime = time.clock()
        insertionSort(lst)
        endTime = time.clock()
        elapsedTime = endTime - startTime
        print('The elapsed time for insertionSort is : ', elapsedTime)

    print('===================================================')
   ##quicksort
    for c in range(0,3):
        lst = [r.randint(0, 100*(10**c)) for i in range(100*(10**c))]
        print('loop count : ', 100*(10**c))
        startTime = time.clock()
        lst = quickSort(lst)
        print(lst)
        endTime = time.clock()
        elapsedTime = endTime - startTime
        print('The elapsed time for quickSort is : ', elapsedTime)