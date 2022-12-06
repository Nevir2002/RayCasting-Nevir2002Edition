file = open('Map.txt')
MAP = []
for line in file:
    a = [int(x) for x in line.split()]
    # print(*a)
    MAP.append(a)
SIZE_X = len(MAP[0])
SIZE_Y = len(MAP)
# print(SIZE_X,SIZE_Y)
file.close()