N=int(input())

dic={}

cnt=0

for _ in range(N):
    Input=input()

    # 입력 받은 값이 'enter'인 경우
    # 딕셔너리 dic을 순회하면 값(value)이 1인 항목을 찾음(즉, 한번만 등장한 단어)
    # 이렇게 찾은 단어의 개수를 cnt에 더하고, 딕셔너리 dic을 빈 딕셔너리로 초기화
    if Input=="ENTER":
        for key,value in dic.items():
            if value==1:
                cnt+=1
        dic={}
    else:
        # enter 이외의 입력인 경우
        # 입력 받은 단어가 딕셔너리 dic에 없으면 해당 단어를 key로 추가하고 value를 1로 설정(한번 등장한 단어)
        # 이미 딕셔너리에 있으면 추가되지 않고 넘어감
        if Input not in dic:
            dic[Input]=1

# 남아 있는 단어 처리
# 반복문이 끝난 후에도 남아 있는 딕셔너리 dic을 순회하여 value가 1인 항목을 찾음
# 이렇게 찾은 단어ㅢ 개수를 cnt에 더함
for key,value in dic.items():
    if value==1:
        cnt+=1

#enter 입력이 들어올 때마다 그동안 입력 받은 모든 단어 중 한번만 등장한 단어의 개수를 의미하는 cnt 출력
print(cnt)