#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for j in range(len(my_list)):
        if new_list[j] is search:
            new_list[j] = replace
    return (new_list)
