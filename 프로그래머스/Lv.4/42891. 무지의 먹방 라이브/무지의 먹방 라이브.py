# 최악의 경우 음식의 수만큼만 roop를 돌면 되므로 시간복잡도가 줄어든다.
from operator import itemgetter

def solution(food_times, k):
  foods = [] # (먹는데 걸리는 시간, 음식 번호) 저장
  n = len(food_times) # 음식의 수
  for i in range(n):
    foods.append((food_times[i], i+1))
    
  # 튜플의 첫번째 인덱스 기준으로 정렬(걸리는 시간이 작은 음식부터 큰 음식순으로 정렬)
  foods.sort() 
  pretime = 0
  for i, food in enumerate(foods): # 음식을 먹는 roop
    diff = food[0] - pretime
    if diff != 0:
      spend = diff * n # 현재 음식을 다먹는데 걸리는 시간
      if spend <= k:
        k -= spend 
        pretime = food[0]
      else:
        idx = k % n # 여기서 n은 남은 음식의 수이다
        # 남은 음식을 번호 순으로 다시 정렬
        sublist = sorted(foods[i:], key=itemgetter(1)) 
        return sublist[idx][1]

    n -= 1 # 현재 음식 다 먹음
  # for문 도중 return이 안됬다는 것은 k가 남았다 
  # -> 음식을 다 먹었다 -> -1 반환  
  return -1