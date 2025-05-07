a = int(input())
b = list(map(int,input()))
total = 0
for i in range(a):
    total += b[i]
print(total)