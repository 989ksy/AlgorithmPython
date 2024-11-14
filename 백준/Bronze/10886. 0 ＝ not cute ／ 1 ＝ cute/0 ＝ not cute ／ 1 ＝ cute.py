n = int(input())
cute = notCute = 0

for i in range(n):
  vote = int(input())
  if vote == 1:
    cute += 1
  else:
    notCute += 1

print("Junhee is not cute!" if notCute > cute else "Junhee is cute!")