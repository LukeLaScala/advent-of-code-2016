x = 0
y = 0
vectors = list()
visited = list()

# 0 -> NORTH
# 1 -> EAST
# 2 -> SOUTH
# 3 -> WEST

direction = 0

input = open('in.txt', 'r+').read().strip('\n').split(', ')

def visited_before(visited, current):
    for visit in visited:
        if visit == current:
            print(current)
    return False


for directions in input:
  vectors.append((directions[0], directions[1:]))

for vector in vectors:
  if vector[0] == 'R':
    direction+=1
  else:
    direction-=1

  direction = (direction + 4) % 4
  magnitude = int(vector[1])
  
  if direction == 0:
    for i in range(magnitude):
      y += 1
      visited_before(visited, (x, y))
      visited.append((x, y))

  if direction == 1:
    for i in range(magnitude):
      x += 1
      visited_before(visited, (x, y))
      visited.append((x, y))

  if direction == 2:
    for i in range(magnitude):
      y -= 1
      visited_before(visited, (x, y))
      visited.append((x, y))

  if direction == 3:
    for i in range(magnitude):
      x -= 1
      visited_before(visited, (x, y))
      visited.append((x, y))

x,y = str(abs(x)), str(abs(y))
print("x: " + x)
print("y: " + y)
print("x + y: " + str(int(x) + int(y)))
