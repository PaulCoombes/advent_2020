import copy
with open(r'day_1\input.txt', 'r') as f:
    expenses = [int(line.rstrip()) for line in f]

for e in expenses:
    for e2 in expenses:
        offset = 2020 - e - e2
        if offset > 0:
            for e3 in expenses: 
                if e3 == offset:
                    print(e, e2, e3)
                    print(e * e2 * e3)
