#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result = []
    for i in range(list_length):
        try:
            index = my_list_1[i] / my_list_2[i]
        except TypeError:
            index = 0
            print("wrong type")
            continue
        except ZeroDivisionError:
            index = 0
            print("division by 0")
            continue
        except IndexError:
            index = 0
            print("out of range")
            continue
        finally:
            result.append(index)
    return result
