#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        list_result = []
        for i in range(len(my_list)):
            if my_list[i] % 2:
                list_result.append(False)
            else:
                list_result.append(True)
        return list_result
