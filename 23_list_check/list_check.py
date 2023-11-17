def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    to_check = [isinstance(entry, list) for entry in lst]
    return all(to_check)