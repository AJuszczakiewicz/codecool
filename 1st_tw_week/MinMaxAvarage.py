import numpy as np

def max(list):
    if list:
        list = digit_list(list)
        max = list[0]
        for item in list[1:]:
            if max < item:
                max = item
        return max
    else:
        return "Pusta lista"


def min(list):
    if list:
        list = digit_list(list)
        min = list[0]
        for item in list[1:]:
            if min > item:
                min = item
        return min

def average(list):
    if list:
        list = digit_list(list)
        sum = 0
        for item in list:
            sum += item
        return sum/len(list)

def digit_list(list):
    new_list = []
    for item in list:
        if type(item) == int or type(item) == float:
            new_list.append(item)
        elif type(item) == list:
            print(item)
            for num in item:
                if type(num) == int or type(num) == float:
                    new_list.append(num)           
    return new_list

def test_max():
    assert max([3, 2, 6, 1, 67, 3, 5, 1]) == 67
    assert max([2, 1]) == 2
    assert max([-5, 23, 0, "dupa", -9, 12, 99, [2, 106], None, 105, -43]) == 106


def test_min():
    assert min([3, 2, 6, 1, 67, 3, 5, 1]) == 1
    assert min([2, 1]) == 1
    assert min([-5, 23, 0, "dupa", -9, 12, 99, [2, 44], None, 105, -43]) == -43

def test_average():
    assert average([3, 2, 6, 1, 67, 3, 5, 1]) == np.mean([3, 2, 6, 1, 67, 3, 5, 1])
    assert average([2, 1]) == np.mean([2,1])
    assert average([-5, 23, 0, "dupa", -9, 12, 99, [2, 44], None, 105, -43]) == np.mean([-5, 23, 0, -9, 12, 99, 105, -43])


print(max([-5, 23, 0, "dupa", -9, 12, 99, [2, 44], None, 105, -43]))