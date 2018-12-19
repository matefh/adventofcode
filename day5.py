f = open('input.txt')
s = f.readline()
s = list(s)
def react(s):
  changed = True
  while changed and len(s) > 0:
    changed = False
    i = 0
    removed = []
    while i < len(s) - 1:
      a, b = s[i], s[i + 1]
      if a != b and a.lower() == b.lower():
        removed.append(i)
        removed.append(i + 1)
        i += 1
        changed = True
      i += 1
    t = []
    for i in range(len(s)):
      if not i in removed:
        t.append(s[i])
    s = t
  return s
s = react(s)
best_len = len(s)
print "Part 1:", best_len
s_original = s
for o in range(26):
  c = chr(ord('a') + o)
  s = []
  for d in s_original:
    if d.lower() != c:
      s.append(d)
  best_len = min(best_len, len(react(s)))
print "Part 2:", best_len