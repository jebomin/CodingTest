h, m = map(int, input().split())
time = int(input())

h = h+time//60
m = m+time%60

if  m >= 60:
  h = h+1
  m = m-60
if h>= 24:
  h = h-24

print(h,m)