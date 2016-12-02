directions_list = open('in.txt').read().split('\n')

row = 1
col = 1
keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8','9']
         ]
code = ""
for directions in directions_list:
    for char in directions:
        if char == 'R':
            if col != 2:
                col += 1

        if char == 'L':
            if col != 0:
                col -= 1

        if char == 'D':
            if row != 2:
                row += 1

        if char == 'U':
            if row != 0:
                row -= 1

    code += keypad[row][col]

print("Code: " + code)
