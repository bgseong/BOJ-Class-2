import sys
from collections import deque

T=int(sys.stdin.readline())
for _ in range(T):
  N,M=map(int,sys.stdin.readline().split())
  dic={}
  for i,n in enumerate(map(int,sys.stdin.readline().split())):
    dic[i] = n
  li=deque(dic.items())
  i=1  
  res={}
  while len(li)>0:
    if li[0] != max(li,key=lambda x:x[1]):
      li.rotate(-1)
    else:
      x,y=li.popleft()
      res[x] = i
      i+=1
  print(res[M])
