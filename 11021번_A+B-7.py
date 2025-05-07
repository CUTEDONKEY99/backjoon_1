a = int(input())
for _ in range(1, a+1):
    b, c = map(int, input().split())
    print(f"Case #{_}:", b+c)