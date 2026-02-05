def alt_caps(original_string):
    """Convert a string to Alternating Caps

    Args:
        original_string (str): A given string with any kind of capitalization
    Returns:
        str: A new string with alternating capitalization
    Examples:
        >>> print(alt_caps("Alternating Capitalization"))
        aLtErNaTiNg CaPiTaLiZaTiOn
    """
    count = 0

    new_string = ""
    for i in original_string:
        if count % 2 == 0:
            new_character = i.upper()
        else:
            new_character = i.lower()
        new_string += new_character
        count += 1
        
        
        
    

    return new_string

print(alt_caps("Alternating Capitalization"))

