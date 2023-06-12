# 조건문
# 조건문 -> 특정 조건을 만족시겼을 때 실행시키는 문법
# -> bool, 비교연산자, 논리연산자...

'''
# if 조건문
if 조건식:
    조건을 만족시켰을 때 실행할 코드
'''

my_age = int(input("당신의 나이는:"))
# if my_age > 20:
#     print("술과 담배가 가능합니다.")
#     # 들여쓰기가 안되면 에러가 난다.

# 중첩if문
# if my_age < 20:
#     print("학생입니다.")
#     if my_age >= 17:
#         print("고등학생입니다!")
#     if my_age >= 14 and my_age < 17:
#         print("중학생입니다!")

# if-else
# 성인 <--> 어린이
'''
if 조건식:
    코드1
else:
    코드2
'''
if my_age > 20:
    print("복권을 구입할 수 있습니다.")
else:
    print("복권을 구입할 수 없습니다.")

# 조건문에 다양한 자료형 넣어보기

# 불(bool) -> 숫자가 0이 아니면 -> True, (0만 False)
# 글자는 ""가 아니면 --> True, --> len(시퀀스) == 0 -> False, len(시퀀스) != 0 -> True

if 1: # bool로 알아서 바궈줌 -> bool(...) 씌운 효과
    print("??????")

if 0:
    print("False")

if '':
    print("-----")

if ' ':
    print("  공백")



# 만약에 조건이 여러개면?
# menu = input("마시고 싶은 음료 : (아메리카노, 제로콜라, 물)")
# if menu == "아메리카노": # 각각 별도의 if문
#     print("아메리카노 나왔습니다")
# if menu == "제로콜라": # 각각 별도의 if문
#     print("제로콜라 나왔습니다")
# if menu == "물": # 각각 별도의 if문
#     print("물 나왔습니다")
# else:
#     print("주문할 수 없는 음료입니다")


menu = input("마시고 싶은 음료 : (아메리카노, 제로콜라, 물)")
if menu == "아메리카노": # 각각 별도의 if문
    print("아메리카노 나왔습니다")
elif menu == "제로콜라": # 각각 별도의 if문
    print("제로콜라 나왔습니다")
elif menu == "물": # 각각 별도의 if문
    print("물 나왔습니다")
else:
    print("주문할 수 없는 음료입니다")
# elif는 단독으로 사용할 수 없다.
# elif는 들여쓰기를 하지 않는다.