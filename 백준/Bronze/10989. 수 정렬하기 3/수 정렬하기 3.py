import sys

input = sys.stdin.readline

n = int(input())
num_array = [0] * 10001

for _ in range(n):
  num = int(input())
  num_array[num] += 1

for i in range(10001):
  if num_array[i] != 0:
    for j in range(num_array[i]):
      print(i)