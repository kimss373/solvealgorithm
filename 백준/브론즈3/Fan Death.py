n = int(input())

fan = 0
for i in range(1, n+1):
    if n % i == 0:
        fan += i

print((fan * 5) - 24)