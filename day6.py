f = open('input.txt')
lines = f.readlines()
ps = [map(int, lines[i].split(", ")) for i in range(len(lines))]
MAX = 400
def manhattan_dist(x, y, i, j):
  return abs(x - i) + abs(y - j)
area = [0] * len(ps)
is_infinite = [False] * len(ps)
nearest_point = [[-1 for i in range(MAX)] for j in range(MAX)]
for x in range(MAX):
  for y in range(MAX):
    min_dist = 1000000
    points_with_min_dist = 0
    point_with_min_dist = -1
    for i in range(len(ps)):
      dist = manhattan_dist(x, y, ps[i][0], ps[i][1])
      if min_dist > dist:
        min_dist = dist
        points_with_min_dist = 1
        point_with_min_dist = i
      elif min_dist == dist:
        points_with_min_dist += 1
    if points_with_min_dist == 1:
      nearest_point[x][y] = point_with_min_dist
    if min(x, y) == 0 or max(x, y) == (MAX - 1):
      is_infinite[point_with_min_dist] = True
for x in range(MAX):
  for y in range(MAX):
    p = nearest_point[x][y]
    if p >= 0 and not is_infinite[p]:
      area[p] += 1
print "Part 1:", max(area)

dist_sum = [[0 for i in range(MAX)] for j in range(MAX)]
ans = 0
for x in range(MAX):
  for y in range(MAX):
    for i in range(len(ps)):
      dist_sum[x][y] += manhattan_dist(x, y, ps[i][0], ps[i][1])
    if dist_sum[x][y] < 10000:
      ans += 1
print "Part 2:", ans

