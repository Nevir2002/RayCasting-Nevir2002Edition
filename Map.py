file = open('Map.txt')
SIZE = int(file.readline())
MAP = [[int(x) for x in file.readline().split()] for i in range(SIZE)]
file.close()