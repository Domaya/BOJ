n = int(input())
origin = n
new = 0
temp = 0
counter = 0

while True:
    temp = n//10 + n%10
    new = temp%10 + n%10*10
    n = new
    counter = counter + 1

    if new == origin:
        break;
print(counter)
