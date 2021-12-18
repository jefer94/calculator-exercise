__all__ = ['addition']

def addition(*args):
    acc = 0

    if not args:
        return acc

    for number in args:
        acc += number

    return acc
