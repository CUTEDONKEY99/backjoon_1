a = int(input())
b = list(map(int, input().split()))
total = 0
for i in range(a):
    total += b[i] / max(b) * 100
print(total/a)
