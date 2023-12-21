#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x element of a list

    Args:
        my_list (list): The list to print element from.
        x (int): The number of the element of my_list to print.

    Returns:
        The number of the element printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
