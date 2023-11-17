def frequency_map(iterable):
    """Return frequency map over iterable.
    called in same_frequency. copied and modified from exercise 7
    """
    freq_map = {}
    for entry in iterable:
        freq_map[entry] = freq_map.get(entry, 0) + 1
            
    return freq_map

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    s1 = str(num1)
    s2 = str(num2)
    
    return frequency_map(s1) == frequency_map(s2)