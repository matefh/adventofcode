import math,string,itertools,fractions,heapq,collections,re,array,bisect,copy
import numpy as np

f = open('input.txt')
lines = f.readlines()
adj = collections.defaultdict(list)
nodes = set()
for line in lines:
  u, v = line[5], line[36]
  adj[v].append(u)
  nodes.add(u)
  nodes.add(v)
_nodes = copy.deepcopy(nodes)
_adj = copy.deepcopy(adj)
n = len(nodes)
order = []
while len(nodes) > 0:
  for u in sorted(nodes):
    if len(adj[u]) == 0:
      order.append(u)
      nodes.remove(u)
      for v in nodes:
        if u in adj[v]:
          adj[v].remove(u)
      break
print "Part 1:", ''.join(order)

WORKERS = 5
COST = 60

def exec_time(u):
  return COST + ord(u) - ord('A') + 1

def can_do(u, done):
  for v in adj[u]:
    if not v in done:
      return False
  return True

nodes = copy.deepcopy(_nodes)
adj = copy.deepcopy(_adj)
cur_time = 0
workers = [(exec_time(order[0]), order[0])]
order.remove(order[0])
done = []
while len(order) > 0 or len(workers) > 0:
  
  to_assign = []
  for i in range(len(order)):
    if can_do(order[i], done):
      to_assign.append(order[i])
  to_assign = sorted(to_assign)
  i = 0
  while len(workers) < WORKERS and i < len(to_assign):
    workers.append((cur_time + exec_time(to_assign[i]), to_assign[i]))
    order.remove(to_assign[i])
    i += 1

  print cur_time,
  for i in range(WORKERS):
    if i < len(workers):
      print workers[i],
    print "\t",
  print

  workers = sorted(workers)
  done_task = workers[0]
  workers.remove(workers[0])
  cur_time = done_task[0]
  done.append(done_task[1])

print "Part 2:", cur_time
