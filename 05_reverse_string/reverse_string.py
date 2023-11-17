def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    
    # Better solution:
    return phrase[::-1]
    
    # chars_list = list(phrase)
    # chars_list.reverse()
    
    # s = ""
    # for char in chars_list:
    #     s = s + char
    # return s