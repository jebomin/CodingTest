n = int(input())
test_result = list(map(int, input().split()))
max_score = max(test_result)

new_list = []
for score in test_result:
    new_list.append(score/max_score*100)
test_avg = sum(new_list)/n
print(test_avg)