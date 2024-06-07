import numpy as np

def list_to_string(list):
    full_string=""
    for string in list:
        full_string=full_string+" "+string
    return full_string    

def list_difference(list_1, list_2):
    return [item for item in list_1 if item not in list_2]

def upper_list(lst):
    lst=list(map(lambda x: x.upper(),lst))
    return lst

def unique_list(lst):
    array=np.array(lst)
    unique=np.unique(array)
    unique=list(unique)
    return unique