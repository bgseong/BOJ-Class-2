import sys
while 1:
  x,y,z=sorted(map(int,sys.stdin.readline().split()))
  if x+y+z == 0:
    break
  if x**2+y**2==z**2:
    print("right")
  else:
    print("wrong")
