from random import randrange
import sys

# def get_input():
#     num_list = input("Gimme some numbers to sort: ").split(", ")
#     print(num_list)
#     return num_list

def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


def quick_sort(lst, start, end):
    if start >= end:
        return lst
    pivot = randrange(start, end + 1)
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)


def sort(lst):
    quick_sort(lst, 0, len(lst) - 1)
    return lst

def bubble(num_list):
    for j in range(0, len(num_list)-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list

def codecool_sort(num_list):
    for x in range(0, len(num_list)-1):
        bubble(num_list)
    return num_list

def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list
 
    num_listiddle = len(num_list) // 2
    left = num_list[:num_listiddle]
    right = num_list[num_listiddle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge_sort(left, right))
    
def test_codecool_sort():
    assert codecool_sort([3,2,6,1,67,3,5,1]) == [1, 1, 2, 3, 3, 5, 6, 67]
    assert codecool_sort([2,1]) == [1,2]
    assert codecool_sort([]) == []

def test_merge_sort():
    assert codecool_sort([3,2,6,1,67,3,5,1]) == [1, 1, 2, 3, 3, 5, 6, 67]
    assert codecool_sort([2,1]) == [1,2]
    assert codecool_sort([]) == []

def test_sort():
    assert codecool_sort([3,2,6,1,67,3,5,1]) == [1, 1, 2, 3, 3, 5, 6, 67]
    assert codecool_sort([2,1]) == [1,2]
    assert codecool_sort([]) == []

# print(codecool_sort(get_input()))