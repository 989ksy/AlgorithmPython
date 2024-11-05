import math

def is_Prime(a):
  if a == 1:
    return 0
  for i in range(2, int(math.sqrt(a))+1):
    if a % i == 0:
      return 0
  return 1
  
m = int(input())
n = int(input())

arr = [ ]

for i in range(m, n+1):
  if is_Prime(i):
    arr.append(i)

if len(arr) > 0:
  print(sum(arr))
  print(min(arr))
  
else:
    print(-1)