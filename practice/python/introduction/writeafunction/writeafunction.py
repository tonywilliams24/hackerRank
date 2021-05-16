def is_leap(year):
    leap = True

    if year % 4 != 0:
        return False

    if year % 100 == 0:
        leap = False

    if year % 400 == 0:
        leap = True

    return leap