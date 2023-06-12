# 시퀀스 자료형

# 리스트, 튜플, 문자열, range. -> 공통점 -> 값이 연속적(sequence)으로 이어져 있다.

print('파이션', '파', '이', '썬') # 단어들의 합쳐진 것 -> 문자열

# 시퀀스 자료형의 공통 기능(특징)

## 특정한 값이 (안에) 있는지 확인
## -> 요소(element) -> 묶음 안에 존재하는지를 확인
## 값 in 시퀀스객체
## 객체 : 특정한 자료형타입에 속하는 것을 -> 객체

shoes = ['아디다스', '나이키', '뉴발란스']
print("shose", shoes)
print("'아디다스' in shoes :", '아디다스' in shoes)
print("'프로스펙스' in shoes :", '프로스펙스' in shoes)
print("'푸마' not in shoes :", '푸마' not in shoes, not '푸마' in shoes)

# 시퀀스 타입(자료형)의 속하는 시퀀스 객체들의 공통적인 기능.
# 시퀀스 타입 (문자열, 리스트, 튜플, 레인지)
t = ("1", "2", "3")
print("t", t)
print("'1' in t :", '1' in t)
r = range(500, 100, -25)
print("r :", list(r))
print("200 not in r :", 200 not in r)
# 문자열 검색
phone_number = "010-9999-9999"
print("phone_number :", '0' in phone_number)
print("010 in phone_number :", '010' in phone_number)
print("9 in phone_number:", '9' in phone_number)
# 문자열은 연속된 부분집합의 형태로 단어들을 검색(다른 시퀀스는 안됨)

## 연결(concatenation)
# 시퀀스 객체는 + 연산자를 이용하여서 객체를 서로 연결하여 새 객체를 만들 수 있음.
# 시퀀스 객체1 + 시퀀스 객체 2 (원만하면 동일 타입...그런데 강제로 붙이면 연결되기도 함...)
a = [0,1,2,3]
a = list(range(4))
b = [4,5,6,7]
b = list(range(4,8))
print ("a + b:", a + b)

# 튜플
a = ("a", "b", "c", "d")
a = tuple("abcd")
a = list("abcd")
b = ("e", "f", "g", "h")
b = tuple("efgh")
b = list("efgh")
print("a + b:", a + b)

# 시퀀스 자료형 중에 연결 안되는 것 : range가 연결이 안됨.
# print(range(10) + range(10,20))

print(list(range(10)) + list(range(10,20)))

# 문자열도 시퀀스도 --> 연결(+)
# greeting = "Hello"
# my_name = input("당신의 이름 : ")
# print(greeting + " " + my_name)

# 문자열과 숫자 연결
# money = input("받고 싶은 돈 : ")
# print(type(money))
# print("당신의 계좌에 " + money + "만원이 입금 되었습니다!")

# money = int(input("받고 싶은 돈 : "))
# print(type(money))
# print("당신의 계좌에 " + str(money) + "만원이 입금 되었습니다!")

## 반복

# * 연산자는 시퀸스 객체를 특정 횟수만틈 반복하여 시퀀스 객체를 만듭니다.
'''
- 시퀀스객체 * 정수
- 정수 * 시퀀스객체
'''

k = [0, 10, 20, 30]
print(k + k + k)
print("k를 3번 반복한다", k * 3)
k *= 3
print (k)
# range는 안됨
# print(range(10)*3)
print(tuple(range(10))*3)

hello = "안녕"
print(hello * 3)

## 길이 구하기
## 시퀀스 객체의 요소(element) 계수 구하기
## len -> length의 약자. 파이썬의 len은 함수. len(...)
## 길이 -> 객체에 딸린 메소드|함수 -> length, size...(다른 언어)
## len(시퀀스객체)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # 피보나치 수열
print(len(a))
b = ("a", 1, True, 1.5)
print(len(b))
c = "hello"
print(len(c))

# range
print(len(range(75,20, -4)))

# 문자열 : len -> 포함된 '문자' 개개의 갯수
# 파이썬은 숫자, 영어, 한글의 길이 구분 x -> 똑같이 길이 1씩
c = "hello world"
print(len(c)







