import re
import numpy as np
f = open('input.txt')
lines = f.readlines()
c = np.zeros((2000,2000))
for s in lines:
  parts = re.compile(r'[#@,: x\n\s]+').split(s)
  x, y, w, h = map(int, parts[2:6])
  for i in xrange(x, x + w):
    for j in xrange(y, y + h):
      c[i][j] += 1
res = 0
for i in range(len(c)):
  for j in range(len(c[0])):
    if c[i][j] > 1:
      res += 1
print res