num_list = sorted(list(map(int, input().split())))

if num_list[2] >= num_list[0] + num_list[1]:
    print(2*(num_list[0] + num_list[1])-1)
else:
    print(sum(num_list))