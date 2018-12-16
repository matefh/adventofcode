f = open('input.txt')
lines = f.readlines()
print sum(map(int, lines))