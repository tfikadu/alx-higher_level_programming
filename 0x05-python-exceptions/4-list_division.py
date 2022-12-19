#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_List = []
    for i in range(list_length):
        try:
            div = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except TypeError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            new_List.append(div)
    return new_List
