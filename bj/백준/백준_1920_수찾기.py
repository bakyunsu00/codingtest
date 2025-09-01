from bisect import bisect_left, bisect_right

natural_num_count = (int(input()))
natural_nums = list(map(int,input().split()))
target_num_count = int(input())
target_nums = list(map(int,input().split()))
results = []
natural_nums.sort()

for target_num in target_nums:
    if bisect_left(natural_nums,target_num) != bisect_right(natural_nums,target_num):
        results.append(1)
    else:
        results.append(0)



for _ in results:
    print(_)