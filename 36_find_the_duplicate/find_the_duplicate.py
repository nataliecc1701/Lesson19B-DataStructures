def frequency_map(iterable):
    """Return frequency map over iterable.
    this is the same one as I made for problem 34
    """
    freq_map = {}
    for entry in iterable:
        freq_map[entry] = freq_map.get(entry, 0) + 1
            
    return freq_map

def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    
    # inefficient way
    # freq_map = frequency_map(nums)
    # for item in freq_map.items():
    #     if item[1] > 1:
    #         return item[0]
    # return None
    
    # better way
    for num in nums:
        if nums.count(num) == 2:
            return num
    return None

    # even better to use a set of things we've seen so far (this runs in O(N^2))