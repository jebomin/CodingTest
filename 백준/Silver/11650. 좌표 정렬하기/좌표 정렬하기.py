n = int(input())

a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

a.sort()

for i in a:
    print(i[0], i[1])