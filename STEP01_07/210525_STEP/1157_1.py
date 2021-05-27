import time
start = time.time()

#문자열 입력받기
word=input()
#문자열 대문자로 변환하기
word=word.upper()
#알파벳을 담을 딕셔너리 초기화하기
alphabet={}

#단어당 몇회나오는지 딕셔너리에 담기
for i in word:
  if i in alphabet:
    alphabet[i]+=1
  else:
    alphabet[i]=1

#정답과 몇회인지를 담을 변수 초기화하기
answer=0
big=0

#정답구하기
for i in alphabet:
  if alphabet[i]>big:
    big=alphabet[i]
    answer=i
  elif alphabet[i]==big:
    answer='?'
    

print(answer)

print("time : ", time.time() - start)
