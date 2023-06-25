import sys

num = int(input())
coordinate = [list(map(int,sys.stdin.readline().split())) for i in range(num)]

coordinate.sort(key=lambda x: [x[1],x[0]])
for i in coordinate:
    print(i[0],i[1])