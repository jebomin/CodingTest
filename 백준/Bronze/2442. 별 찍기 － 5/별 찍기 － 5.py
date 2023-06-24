#별의 앞부분 공백만 신경쓰는게 포인트
N = int(input())

for i in range(1,N+1):

    b = ' '*(N-i)+'*'*((2*i)-1)

    print(b)