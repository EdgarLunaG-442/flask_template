from copy import deepcopy


def filter_object(elem, fields):
    copy_elem = deepcopy(elem)
    for field in fields:
        copy_elem.pop(field)
    return copy_elem
