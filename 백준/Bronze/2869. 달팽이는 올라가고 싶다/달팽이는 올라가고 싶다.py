# A = 올라갈 수 있는 거리, B = 미끄러지는 거리, V = 나무 막대 높이
# 올라가야 할 거리 = V-B
# 하루에 갈 수 있는 거리 = A-B

import math

A,B,V = map(int, input().split())
day = (V-B)/(A-B)
print(math.ceil(day))