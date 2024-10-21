from collections import deque

# N, M, S = map(int, input().split()) # 인풋
N = int(input())
M = int(input())

# A 만들기 (그래프 표현)
A = [[] for _ in range(N + 1) ] # N + 1 짜리 2차원 배열

# A 인풋
for _ in range(M): # M개의 엣지만큼 인풋 받아
  s, e = map(int, input().split())
  A[s].append(e)
  A[e].append(s)

for i in range(N+1):
  A[i].sort() # 작은거부터 탐색하기 위함


# 인풋 끝. 오예

ans = 0

# DFS
v = [False] * (N + 1) # 특정 노드를 방문했는지 여부 저장. v[i] : i번째 노드를 방문했는지 여부 

def DFS(s): # s번째 노드에 대해 DFS 시작
  # print("현재 방문 : ", s)
  global ans
  ans += 1
  v[s] = True # s번째 노드는 이미 방문했다고 표시 
  # s와 연결된 노드들을 싹 다 방문 
  for i in A[s]:
    if not v[i]: # 방문하고자 하는 I번째 노드가 이미 방문이 안되어있을 때만 DFS 실행 
      DFS(i)


# DFS 실행 
DFS(1)
print(ans - 1)