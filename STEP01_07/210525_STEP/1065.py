#입력은 최대 네 자리수
#1000일땐 등차수열X
#두자리수/세자리수만 고려하면 됨
#두자리수까지 모두 한수임

def hansoo(num):
    count = 0
    if num < 100:
        count = num
    else: #num이 세자리 숫자
        count = 99
        for i in range(100, num+1):
            num = str(i)
            if (int(num[2]) - int(num[1])) == (int(num[1]) - int(num[0])):
                count += 1
    return count

Q = int(input())
print(hansoo(Q))
