n_list = []

for i in range(10):
  n = int(input())
  n_list.append(n%42)
n_list = set(n_list)
print(len(n_list))