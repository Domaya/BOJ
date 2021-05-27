S = input()
arr = []
for j in range(97, 123):
    if chr(j) in S:
        idx = S.index(chr(j))
        arr.append(idx)
    else:
        arr.append(-1)

for i in arr:
    print(i, end = " ")
