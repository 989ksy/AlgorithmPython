import math

def is_Prime(a):
  if a == 1:
    return 0
  for i in range(2, int(math.sqrt(a))+1):
    if a % i == 0:
      return 0
  return 1
  

m, n = map(int, input().split())

for i in range(m, n+1):
  if is_Prime(i):
    print(i)