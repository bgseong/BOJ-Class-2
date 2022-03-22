import sys

N=int(sys.stdin.readline())
i=1
c=0
while 1:
  if i<=N and N<=i+(6*c):
    break
  i+=6*c
  c+=1
print(c+1)
