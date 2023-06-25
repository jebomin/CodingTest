n = int(input())
member_lst = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member_lst.append((age, name)) #튜플로 묶어 member_lst 리스트에 추가, 즉 각 회원의 정보는 (나이, 이름) 형태의 튜플

member_lst.sort(key = lambda x : x[0])	# (age, name)에서 age를 기준으로 정렬

for i in member_lst:
    print(i[0], i[1]) #i[0]는 나이, i[1]은 이름