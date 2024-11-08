s = int(input())
count = 0
result = 0

for i in range(1, s+1):
  count += i
  result = i
  
  if count > s:
    result = result - 1
    break

print(result)