from bisect import bisect_right, bisect_left

m_card_count = int(input())
cards_nums = sorted(list(map(int,input().split())))
my_card_count = int(input())
my_cards_nums = list(map(int,input().split()))
results = []


for num in my_cards_nums:
    results.append(bisect_right(cards_nums, num) - bisect_left(cards_nums,num))


print(results)