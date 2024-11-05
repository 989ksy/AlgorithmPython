import math

def is_prime(a):
  if a == 1:
    return 0
  for i in range(2, int(math.sqrt(a))+1):
    if a % i == 0:
      return 0
  return 1

n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in arr:
  if is_prime(i):
    cnt += 1

print(cnt)