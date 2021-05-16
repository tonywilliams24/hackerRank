n = 5
arr = [2, 3, 6, 6, 5]
high = -101
runner = -102

for x in arr:
    if x > high:
        runner = high
        high = x
    elif runner < x < high:
        runner = x


print(runner)
