def partition(lst, fn):
    """Partition lst by predicate.

     - lst: list of items
     - fn: function that returns True or False

     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0

        >>> def is_string(el):
        ...     return isinstance(el, str)

        [[2, 4], [1, 3]]

        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    trueList = []
    falseList = []

    for val in lst:
        if fn(val):
            trueList.append(val)
        else:
            falseList.append(val)
    return [trueList, falseList]