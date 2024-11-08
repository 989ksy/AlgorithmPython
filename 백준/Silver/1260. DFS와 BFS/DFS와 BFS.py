from collections import deque

n, m, v = map(int, input().split())
graph = [ [ ] for _ in range(n+1) ]

# 노드 개수
for _ in range(m):
  s, e = map(int, input().split())
  graph[s].append(e)
  graph[e].append(s)

# 작은 수부터
for i in range(n+1):
  graph[i].sort()
  

# DFS
visited_dfs = [False] * (n+1)

def DFS(s):
  visited_dfs[s] = True
  print(s, end = ' ')
  for i in graph[s]:
    if not visited_dfs[i]:
      DFS(i)

# BFS
visited_bfs = [False] * (n+1)

def BFS(s):
  visited_bfs[s] = True
  queue = [s]
  while queue:
    s = queue.pop(0)
    print(s, end = ' ')
    for i in graph[s]:
      if not visited_bfs[i]:
        visited_bfs[i] = True
        queue.append(i)

DFS(v)
print()
BFS(v)