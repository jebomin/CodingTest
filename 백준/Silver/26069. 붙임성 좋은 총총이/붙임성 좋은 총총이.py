import sys
input = sys.stdin.readline

n = int(input())
dance = {'ChongChong'}

for i in range(1, n+1):
    # a와 b가 만났다.
    a, b = input().rstrip().split()
    
    # 두 사람 중 한 사람만 추고 있다면
    # 추고 있지 않은 사람을 추게 만들면 된다.
    if a in dance:
        dance.add(b)

    if b in dance:
        dance.add(a)

print(len(dance))