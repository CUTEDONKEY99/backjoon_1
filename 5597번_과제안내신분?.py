# nums = list(range(1,31))
nums_1 = [i for i in range(1, 31)]
for _ in range(28):
    a = int(input())
    nums_1.remove(a)
print(min(nums_1))
print(max(nums_1))