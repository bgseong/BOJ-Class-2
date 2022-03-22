import sys

def sol(N):
  N=str(N)
  li=[]
  for i in range(len(N)):
    li.append(int(N[i]))
  return sum(li)+int(N)
N=int(sys.stdin.readline())
for i in range(N):
  if sol(i) == N:
    print(i)
    break
else:
  print(0)
