def swapdict(dict_):
    
    new_dict = {}
    for i, j in dict_.items():
        if (type(j) == list) or type(j) == dict:
            continue
        new_dict[j] = i

    return new_dict

# TESTCASE: Same values for different keys
print(swapdict({'1': 1, '2': 2, '3': 2}))