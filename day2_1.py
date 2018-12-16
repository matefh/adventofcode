import collections
f = open('input.txt')
lines = f.readlines()
two, three = 0, 0
for s in lines:
  c = collections.Counter(list(s))
  c = {v: k for k, v in c.iteritems()}
  if 2 in c and c[2] > 0: two += 1
  if 3 in c and c[3] > 0: three += 1
print two * three