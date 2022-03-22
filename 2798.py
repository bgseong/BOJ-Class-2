import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
li=sorted(list(map(int,sys.stdin.readline().split())))
C=deque()
try:
  for i in range(N):
    for j in range(i+1,N):
      for h in range(j+1,N):
        if li[i]+li[j]+li[h] <= M:
          C.append(li[i]+li[j]+li[h])
except:
  pass
print(max(C))
