import sys
T=int(sys.stdin.readline())
for Z in range(T):
  H,W,N=map(int,sys.stdin.readline().split())
  f=0
  w=1
  for i in range(N):
    f+=1
    if f>H:
      f=1
      w+=1
  if w<10:
    print(str(f)+"0"+str(w))
  else:
    print(str(f)+str(w))
