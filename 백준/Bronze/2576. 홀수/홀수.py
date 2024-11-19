input_list = []
odd_list = []

for _ in range(7):
  input_list.append(int(input()))
  
for i in input_list:
  if i % 2 != 0:
    odd_list.append(i)
    
if len(odd_list) > 0:
  print(sum(odd_list))
  print(min(odd_list))
else:
    print(-1)