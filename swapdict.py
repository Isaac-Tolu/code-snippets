def swapdict(dict_: dict) -> dict:
    """
    Swaps the keys and values of a dictionary.
    Returns a new dictionary.

    - If any of the values of dict_ is unhashable i.e list or dict,
      the key-value pair would be ignored.

    - If multiple keys in dict_ have the same value,
      the keys would be a list in new_dict i.e
      {'1': 1, '2': 2, '3': 3, '4': 2} -> {1: '1', 2: ['2', '4'], 3: '3'}
    """
    
    new_dict = {}

    for i, j in dict_.items():
        if (type(j) == list) or (type(j) == dict):
            continue

        check = new_dict.get(j)

        if check:
            if type(check) != list:
                new_dict[j] = [check, i]
            else:
                check.append(i)
                new_dict[j] = check
        else:
            new_dict[j] = i

    return new_dict

# Consider dict.setdefault