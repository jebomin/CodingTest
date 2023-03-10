n_list = []
for _ in range(9):
  i = int(input())
  n_list.append(i)

print(max(n_list))
print(n_list.index(max(n_list))+1)