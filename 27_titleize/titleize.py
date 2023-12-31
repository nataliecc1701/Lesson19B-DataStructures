def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    output = ""
    for word in phrase.split():
        output += word.capitalize() + " "
    
    return output.strip()
    
    # or, apparently, I could have done this with a built-in method.