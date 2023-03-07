def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'
    """
    flipped = ''
    for letter in phrase:
        if to_swap.upper() == letter or to_swap.lower() == letter:
            flipped += letter.swapcase()
        else:
            flipped += letter
    return flipped

