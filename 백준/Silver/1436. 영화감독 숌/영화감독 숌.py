n=int(input())
num=666
cnt=0
#N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.
#즉, 1번째 영화의 제목은 666 | 2번째 영화의 제목은 1666

while True:
    if '666' in str(num): #666이 포함되면 cnt증가
        cnt+=1
    if cnt==n: #n번째 영화제목==n번째 종말숫자
        print(num) #num출력
        break
    num+=1 #숫자를 계속 증가시킴