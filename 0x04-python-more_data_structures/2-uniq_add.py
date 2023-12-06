#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for j in set(my_list):
        result += j
    return (result)
