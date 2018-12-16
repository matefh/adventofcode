f = open('input.txt')
lines = f.readlines()
n = len(lines)
for i in range(n):
  for j in range(i + 1, n):
    ans = []
    s = list(lines[i])
    t = list(lines[j])
    diff = 0
    for k in range(min(len(s), len(t))):
      if s[k] != t[k]: diff += 1
      else: ans.append(s[k])
    if diff == 1:
      print ''.join(ans)
