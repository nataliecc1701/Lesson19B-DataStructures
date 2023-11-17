def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    
    prepped_phrase = ""
    
    # remove non-alphanumeric characters such as spaces and apostrophes
    for char in phrase:
        if char.isalpha():
            prepped_phrase += char.lower()
    
    return prepped_phrase == prepped_phrase[::-1]