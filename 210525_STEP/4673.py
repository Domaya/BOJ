def d(n):
    result = n
    for i in str(n):
        result += int(i)
    return result

num = []
for i in range(1, 10001):
    num.append(d(i))

for i in range(1, 10001):
    if i in num:
        pass
    else:
        print(i)
