import itertools
from itertools import tee, count, groupby
from operator import truth


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def tabulate(function, start=0):
    return map(function, count(start))


def is_valid(value):
    def adjacent_equality(pair):
        p, q = (int(pair[0]), int(pair[1]))

        if p is q:
            return True

        return False

    def lesser_neighbour(pair):
        p, q = (int(pair[0]), int(pair[1]))

        if (p is q) or (p < q):
            return False

        return True

    str_value = str(value)

    try:
        next(filter(
            adjacent_equality,
            pairwise(str_value)
        ))
    except StopIteration:
        return False

    try:
        next(filter(
            lesser_neighbour,
            pairwise(str_value)
        ))
        return False
    except StopIteration:
        return True

    raise RuntimeError


def santa_ripper(start, stop, validator):
    filtered = filter(
        truth,
        map(
            validator,
            iter(x for x in range(start, stop + 1))
        )
    )
    return sum(1 for _ in filtered)


def is_valid_extended(value):
    def adjacent_equality(pair):
        p, q = (int(pair[0]), int(pair[1]))

        if p is q:
            return True

        return False

    def lesser_neighbour(pair):
        p, q = (int(pair[0]), int(pair[1]))

        if (p is q) or (p < q):
            return False

        return True

    def no_biggie():
        int_tuple = [int(x) for x in str_value]
        d = {len(list(g)): k for k, g in itertools.groupby(int_tuple)}
        return 2 in d.keys()

    str_value = str(value)

    try:
        next(filter(
            adjacent_equality,
            pairwise(str_value)
        ))
    except StopIteration:
        return False

    try:
        next(filter(
            lesser_neighbour,
            pairwise(str_value)
        ))
        return False
    except StopIteration:
        pass

    return no_biggie()
