records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
names = []
second = 101.0
low = 101.0
for record in records:
    name = record[0]
    score = record[1]
    if score < low:
        second = low
        low = score
    elif second > score > low:
        second = score

for student in records:
    if student[1] == second:
        names.append(student[0])
names.sort()
print(names)
