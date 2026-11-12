def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


def total(numbers):
    result = 0
    for n in numbers:
        result += n
    return result


def broken_total():
    return missing_total
