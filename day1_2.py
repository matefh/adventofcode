f = open('input.txt')
lines = f.readlines()
s = 0
d = {0: 1}
i = 0
while True:
  x = int(lines[i])
  s += x
  # print s, x
  if s in d:
    print s
    break
  d[s] = 1
  i = (i + 1) % len(lines)