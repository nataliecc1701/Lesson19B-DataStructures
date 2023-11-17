def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    vals = values.copy()
    while len(vals) < len(keys):
        vals.append(None)
    return {keys[i]:vals[i] for i in range(len(keys))}
    
    # tried another approach creating a list of tuples first
    # then decided to try dict comprehension before finishing.
    # [(keys[i], values[i]) if len(values > i) else (keys[i], None) for i in range(len(keys))]
    
    # solution uses the Enumerate constructor to make (index, key) tuples and go from there