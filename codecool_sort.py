# num_list = input("Gimme some num_list to sort: ").split()
# print(num_list)
num_list = [3,2,6,1,67,3,5,1]

def codecool_sort(num_list):
    N = len(num_list)
    for x in range(0, N-1):
        for j in range(0, N-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list
    
def test_codecool_sort():
    assert codecool_sort([3,2,6,1,67,3,5,1]) == [1, 1, 2, 3, 3, 5, 6, 67]
    assert codecool_sort([2,1]) == [1,2]
    assert codecool_sort([]) == []