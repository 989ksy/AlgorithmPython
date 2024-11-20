n = int(input())
num_array = []

for _ in range(n):
  num_array.append(int(input()))

num_array.sort()

for i in num_array:
  print(i)