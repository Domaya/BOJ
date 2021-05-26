t = int(input())
count = 0

for i in range(t):

    s = input();
    arr = []

    flag = 1
    for i in range(len(s)):
        if s[i] not in arr:
            arr.append(s[i])
        else:
            #체크해야함...
            if arr[-1] == s[i]:
                continue;
            else:
                flag = 0
                break;

    if flag == 1:
        count += 1

print(count)
