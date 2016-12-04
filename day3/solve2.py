lengths = list()
actual_lengths = list()
lengths1 = list()
lengths2 = list()
lengths3 = list()
possible = 0
impossible = 0
with open('in.txt') as f:
    for line in f:
        lengths.append(line.lstrip('  ').strip('\n').split('  '))

def check(l1, l2, l3):
    return (l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2

for x in range(0, len(lengths), 3):
    length = list()
    lengths[x] = filter(lambda a: a != '', lengths[x])
    lengths[x + 1] = filter(lambda a: a != '', lengths[x + 1])
    lengths[x + 2] = filter(lambda a: a != '', lengths[x + 2])

    length.append(lengths[x][0])
    length.append(lengths[x + 1][0])
    length.append(lengths[x + 2][0])
    actual_lengths.append(length)

    length = list()

    length.append(lengths[x][1])
    length.append(lengths[x + 1][1])
    length.append(lengths[x + 2][1])
    actual_lengths.append(length)

    length = list()

    length.append(lengths[x][2])
    length.append(lengths[x + 1][2])
    length.append(lengths[x + 2][2])
    actual_lengths.append(length)

for length in actual_lengths:
    length = filter(lambda a: a != '', length)
    if check(int(length[0]), int(length[1]), int(length[2])):
        possible += 1
    else:
        impossible += 1

print("Impossible: " + str(impossible))
print("Possible: " + str(possible))