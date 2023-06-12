# 딕셔너리 (Dictionary)
warrier = [500, 100, 10.5, 27]
print(warrier)
# 해시맵, 맵, 오브젝트, 딕셔너리 ... => 값을 묶음에서 -> 그 값이 어떠한 특징 호은 속성
warrier = {
    "hp": 500,
    "mp": 100,
    "atk": 10.5,
    "def": 27,
} # 사전을 찾듯이 어떠한 키(찾는 단어) -> 대응되는 값.
print(warrier)

# 딕셔너리 만들기
'''
* 딕셔너리 = {키1 : 값1, 키2: 값2...} # 키는 겹치면 x, 수정할 수 없는 값. 각 키와 값 쌍 콤마(,)구분
'''
kim = {
    "name": "kim",
    "age": 30,
    "marry": False,
}
lee = {
    "name": "lee",
    "name": "봉구", # 같은 딕셔너리 안에서 마지만긍로 key에 대입된 값이 최종 값.
}
print(lee)

print(lee["name"])

# 딕셔너리 키의 자료형
# key -> answkduf. 이 외에도 '수정되지 않는 값'은 모두 key로 쓸 수 있음.
# bool, int, float, tuple, rangge, 문자열... -> key로 쓸 수 있음.

# 딕셔너리 키에 접근 및 할당
# 리스트의 경우 --> 리스트[인덱스] -> 값. 리스트[인덱스] = 새로운 값 ==> 할당.
# 리스트-인덱스, 딕셔너리-키 => 호출 시 리스트의 원소를 인덱스로 호출하는 것 처럼, 딕셔너리의 값을 키로 호출
park = {
    "address": "seoul",
}
print(park["address"])
park["address"] = "busan" # 할당 연산자 -->새로운 값을 대입(할당)
print(park["address"])
# 키를 지정하지 않고 그냥 dictionary를 호출하면?
print(park)

# 빈 딕셔너리 만들기
x = {}
x = dict()
print(x)

# print(park['car'])
# key라고 하는 거는, 딕셔너리를 만들 때 넣어주거나, 아니면 할당할 때 쉽게 넣고 할 수 있는데...
# 이에 할당되지 않는 키는 조회시 에러가 발생
x['car'] = "bmw"
print(x)

data = {
    'kim': 200,
    'park': 300,
}
print(data)
print("kim" in data) # 특정한 key가 존재하는지는
'''
* 키 in 딕셔너리
'''
print("lee" in data)
print("lee" not in data)
print(not "lee" in data)

print(len(data))

d = {
    'scores' : [90, 80, 70],
    'money' : 100,
}
print(d)
print(len(d)) # 키와 갯수를 세어줌 근데 키 값은 1:1 대응아니라, 값의 갯수를 세주는 점.









