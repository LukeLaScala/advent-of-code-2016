lengths = list()
possible = 0
impossible = 0
with open('in.txt') as f:
    for line in f:
        lengths.append(line.lstrip('  ').strip('\n').split('  '))

def check(l1, l2, l3):
    return (l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2

for length in lengths:
    length = filter(lambda a: a != '', length)
    if check(int(length[0]), int(length[1]), int(length[2])):
        possible += 1
    else:
        impossible += 1

print("Impossible: " + str(impossible))
print("Possible: " + str(possible))
