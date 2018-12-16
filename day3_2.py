import re
from collections import defaultdict
f = open('input.txt')
lines = f.readlines()
c = [[list() for i in range(2000)] for j in range(2000)]
for s in lines:
  parts = re.compile(r'[#@,: x\n\s]+').split(s)
  x, y, w, h = map(int, parts[2:6])
  for i in xrange(x, x + w):
    for j in xrange(y, y + h):
      c[i][j].append(parts[1])
res = 0
G = defaultdict(set)
for i in range(len(c)):
  # print
  for j in range(len(c[0])):
    # print len(c[i][j]), " ",
    for a in c[i][j]:
      for b in c[i][j]:
        G[a].add(b)
for k, v in G.items():
  if len(v) == 1:
    print k
    break