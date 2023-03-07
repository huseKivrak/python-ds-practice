def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    #evens_to_doubled = {n: n * 2 for n in nums if n % 2 == 0}
    #str.count(sub[, start[, end]])

    return {letter: phrase.count(letter) for letter in phrase }

    counter = {}

    for letter in phrase:
        if letter in counter:
            counter[letter] = counter[letter] + 1
        else:
            counter[letter] = 1
            
        counter[letter] = counter.get(letter, 0) + 1
