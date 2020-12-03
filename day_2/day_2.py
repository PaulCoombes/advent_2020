import re

with open(r'day_2\input.txt', 'r') as f:
    passwords = [line.rstrip() for line in f]

rgx =  r"(\d*)-(\d*) (\w): (\w*)"

matches = 0
for p in passwords:
    _, lower, upper, letter, password, _ = re.split(rgx, p)
    if int(lower) <= (password.count(letter)) <= int(upper):
        matches += 1

print (matches)

matches = 0
for p in passwords:
    _, pos1, pos2, letter, password, _ = re.split(rgx, p)
    letter1 = password[int(pos1) - 1]
    letter2 = password[int(pos2) - 1]

    if (letter1 == letter or letter2 == letter) and letter1 != letter2:
        matches += 1

print(matches)