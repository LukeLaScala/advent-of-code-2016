import string
import collections
sumid = 0

def most_common_char(name):
        maxcount = 0
        maxchar = None
        first = True

        for item in name.lower():
            charcount = name.count(item)

            if ((charcount > maxcount) or ((charcount == maxcount) and (ord(item) < ord(maxchar) ))) :
                maxcount = charcount
                maxchar = item
                first = False

        return maxchar

def most_common_chars(name):
    most_common = list()
    for x in range(5):
        most_cmmn = most_common_char(name)
        most_common.append(most_cmmn)
        name = name.replace(most_cmmn, '')
    return ''.join(most_common)



lines = list(line.rsplit('-', 1) for line in (line.strip('\n') for line in open('input')))
formatted_lines = list()

for x in range(len(lines)):
    checksum = lines[x][-1].rsplit('[', 1)[1].strip(']')
    sector_id = lines[x][-1][0:3]
    lines[x][-1] = sector_id
    lines[x].append(checksum)
    lines[x][0] = lines[x][0].replace('-', "")
    print(lines[x])

for line in lines:
    if most_common_chars(line[0]) == line[-1]:
        sumid += int(line[-2])

print(sumid)