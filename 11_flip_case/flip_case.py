def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap_alter = to_swap.swapcase()
    
    swapped = ""
    for char in phrase:
        if char == to_swap or char == to_swap_alter:
            swapped += char.swapcase()
        else:
            swapped += char
    
    return swapped