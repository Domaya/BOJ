
s = input()
s = s.upper()
temp = {}
count = 0
for i in range(65, 91): #아스키코드 A~Z
    for j in s:
        if j == chr(i):
            count += 1
            temp[chr(i)] = count
    count = 0

maxim = 0
final = 0

for i in temp:
    if temp[i] > maxim:
        maxim = temp[i]
        final = i
    elif temp[i] == maxim:
        final = "?"
print(final)
