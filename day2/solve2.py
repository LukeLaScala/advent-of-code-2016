directions_list = open('in.txt').read().split('\n')

row = 3
col = 1
keypad = [
     ['0', '0', '0', '0', '0', '0', '0'],
     ['0', '0', '0', '1', '0', '0', '0'],
     ['0', '0', '2', '3', '4', '0', '0'],
     ['0', '5', '6', '7', '8', '9', '0'],
     ['0', '0', 'A', 'B', 'C', '0', '0'],
     ['0', '0', '0', 'D', '0', '0', '0'],
     ['0', '0', '0', '0', '0', '0', '0']
        ]

code = ""

def inKeyPad(row, col):
    return keypad[row][col] != '0'

for directions in directions_list:
    for char in directions:
        if char == 'R':
            if inKeyPad(row, col + 1):
                col += 1

        if char == 'L':
            if inKeyPad(row, col - 1):
                col -= 1

        if char == 'D':
            if inKeyPad(row + 1, col):
                row += 1

        if char == 'U':
            if inKeyPad(row - 1, col):
                row -= 1

    code += keypad[row][col]

print("Code: " + code)

