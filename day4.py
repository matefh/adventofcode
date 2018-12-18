from collections import defaultdict
import numpy as np
f = open('input.txt')
f2 = open('input_sorted.txt', 'w')
lines = f.readlines()
lines = sorted(lines)
for line in lines:
  f2.write(line)

# [1518-11-21 23:56] Guard #433 begins shift
log, sleep_minutes = defaultdict(lambda: [0] * 60), defaultdict(int)
g_id = -1

for line in lines:
  if line[19] == 'G':
    g_id = int(line[26:].split(" ")[0])
  elif line[19] == 'f':
    start_sleep = map(int, line[12:17].split(":"))
  else:
    end_sleep = map(int, line[12:17].split(":"))
    sleep_minutes[g_id] += end_sleep[1] - start_sleep[1]
    for m in range(start_sleep[1], end_sleep[1]):
      log[g_id][m] += 1

max_mins = max(sleep_minutes.values())
g = -1
for k, v in sleep_minutes.items():
  if v == max_mins: g = k
print "Part 1:", g * np.argmax(log[g])

most_frequency, most_freq_sleep_minute, g = 0, -1, -1
for k, mins in log.items():
  minute = np.argmax(mins)
  if most_frequency < mins[minute]:
    most_frequency = mins[minute]
    most_freq_sleep_minute = minute
    g = k
print log
print "Part 2:", g * most_freq_sleep_minute