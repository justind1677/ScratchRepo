"""Small calculator used to exercise the kit loop."""


def add(a, b):
    return a + b


def percent_change(old, new):
    if old == 0:
        raise ValueError("old value cannot be zero")
    return round((new - old) / old * 100, 2)


def clamp(value, low, high):
    if low > high:
        raise ValueError("low cannot be greater than high")
    return min(max(value, low), high)
