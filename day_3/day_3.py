with open(r'day_3\input.txt', 'r') as f:
    course = [line.rstrip() for line in f]

height = len(course)
width = len(course[1])

def trees_hit(right, down):
    trees = 0
    x = 0
    y = 0
    for i in range(0, height - 1, down):
        x += right
        y += down
        x = x % width

        if course[y][x] == '#':
            trees += 1

    return (trees)


print (trees_hit(3, 1))

print (trees_hit(1, 1) 
     * trees_hit(3, 1) 
     * trees_hit(5, 1) 
     * trees_hit(7, 1)
     * trees_hit(1, 2))
