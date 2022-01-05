# 소수 셋째자리에서 반올림 -> round()함수 사용
round(123.456, 2)

# / -> 실수형 반환
# % -> 나머지 연산자
# // -> 몫 연산자
# ** -> 거듭제곱 연산자

# <리스트 자료형>
# 비어있는 리스트 선언 : list() or []
a = [1, 2, 3, 4, 5]
print(a)
# 네번째 원소만 출력
print(a[3])
# 크기가 N이고 모든값이 0인 1차원 리스트 초기화
n = 10
a = [0] * 10
print(a)

#--------------------------------------------------------

# <리스트의 인덱싱과 슬라이싱>
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫번째 원소 출력 (9)
print(a[-1])
# 두번째 원소부터 네번째 원소까지 (2,3,4)
print(a[1:4])

#---------------------------------------------------------

# <리스트 컴프리헨션> : 리스트를 초기화하는 방법 중 하나이다.

# 0부터 9까지의 수를 포함하는 리스트 초기화
# range(10) : 0부터 9까지의 수
array = [i for i in range(10)]

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
# 코드 1 : 리스트 컴프리 헨션
array = [i for i in range(20) if i % 2 == 1]
# 코드 2: 일반적인 코드
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]

# N X M 크기의 2차원 리스트 한번에 초기화
array = [[0] * m for _ in range(n)]
# --> 잘못된 코드 : 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식되기 때문
array = [[0] * m] * n

# 언더바(_) 는 반복은 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 사용된다.
# 예시 : "hello" 5번 출력하기
for _ in range(5):
    print("hello")
#---------------------------------------------------------

# <리스트 관련 기타 메서드>
l = [1,2,3]

# 리스트에 원소 삽입
l.append(2)
# 오름차순 정렬
l.sort()
# 내림차순 정렬
l.sort(reverse=True)
# 리스트 원소 뒤집기
l.reverse()
# 특정 인덱스에 데이터 추가 / 인덱스 2에 3추가 -> [1,2,3,3]
a.insert(2,3)
# 값이 3인 데이터 개수 세기
print("값이 3인 데이터 개수는: ", l.count(3))
# 값이 1인 데이터 삭제
l.remove(1)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
l = [1,2,3,4,5,5,5]
remove_set= {3,5} # 집합 자료형
result = [i for i in a if i not in remove_set] # remove_set에 포함되지 않은 값만을 저장

#---------------------------------------------------------

# <문자열 자료형>
data = 'Hello World'
data = "Don't tou know \"Python\"?"

# <문자열 연산>
a = "Hello"
b = "World"
print(a+" "+b)
print(a*3) #HelloHelloHello
print(a[2:4]) #ll
# 문자열은 특정 인덱스 변경 불가능!!
# error : a[2] = 'a'

#---------------------------------------------------------

# <튜플 자료형>
# : 한 번 선언된 값은 변경 불가능 (=문자열)
# 소괄호 () 사용
# 리스트에 비해 상대적으로 공간 효율적임

a = (1,2,3,4,5,6)
# 네번째 원소만 출력
print(a[3])
# 두번째 원소부터 네번째 원소까지
print(a[1:4])

# 튜플, 언제 사용?
# 1. 서로 다른 성질의 데이터를 묶어서 관리할 때 -> 최단 경로 알고리즘
# 2. 데이터의 나열을 Hashing의 키 값으로 사용해야 할 때 : 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있음
# 3. 리스트보다 메모리를 효율적으로 사용해야 할 때

#---------------------------------------------------------

# <사전 자료형> : key value의 쌍을 데이터로 가지는 자료형
# 리스트, 튜플이 값을 순차적으로 저장하는 것과 대비됨
# 키와 값을 쌍으로 데이터를 가지며, 원하는 '변경 불가능한 자료형'을 키로 사용할 수 있음
# 파이썬의 사전 자료형은 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리가능

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# keys() 함수 : 키 데이터만 뽑아서 리스트로 사용
# values() 함수 : 값 데이터만 뽑아서 리스트로 사용
key_list = data.keys()
value_list = data.values()

print(key_list) # dict_keys(['사과','바나나','코코넛']
keylist = list(data.keys()) # 리스트형으로!
print(key_list) # ['사과','바나나','코코넛']

print(data['사과']) # Apple

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# 이렇게도 초기화 가능
b = {
    '홍길동' : 97,
    '이순신' : 98
}

#---------------------------------------------------------

# <집합 자료형>
# : 중복 허용 X, 순서가 없다
# 집합은 리스트 or 문자열을 이용해서 초기화 가능 -> set() 이용
# 중괄호 {} 안에 각 원소를 , 기준으로 구분하여 삽입함으로써 초기화 가능
# 데이터 조회 및 수정에 있어서 O(1)이 시간에 처리 가능

# 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5]) # {1,2,3,4,5}
# 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}  # {1,2,3,4,5}

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
print(a | b)  # 합집합
print(a & b)  # 교집합
print(a - b)  # 차집합

# <집합 자료형 관련 함수>
data = set([1, 2, 3])
# 새로운 원소 추가
data.add(4)  # {1,2,3,4}
# 새로운 원소 여러 개 추가
data.update([5, 6])  # {1,2,3,4,5,6}
# 특정한 값을 갖는 원소 삭제
data.remove(3)  # {1,2,4,5,6}

#---------------------------------------------------------

# <사전 자료형과 집합 자료형의 특징>

# 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있다.
# 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.

#---------------------------------------------------------

# <기본 입출력>
# input() : 한 줄의 문자열을 입력 받는 함수
# map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

# 1. 공백을 기준으로 구분된 데이터를 입력 받을 때
list(map(int, input().split()))  # 공백을 기준으로 입력 받은 데이터를 정수형으로 만들어줌
# <예시>
n = int(input())  # 데이터의 개수 입력
data = list(map(int, input().split()))  # 각 데이터를 공백을 기준으로 구분하여 입력
data.sort(reverse=True)  # [761, 433, 100]

# 2. 공백을 기준으로 구분된 데이터의 개수가 많지 않다면
a, b, c = map(int, input().split())  # a,b,c에 차례대로 넣기
# <예시>
n, m, k = map(int, input().split())

# 3. 빠르게 입력 받기
# sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드 이용
# -> 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용해야함
# <예시>
import sys # 표준 라이브러리 사용
data = sys.stdin.readline().rstrip()

# 자주 사용되는 표준 출력 방법 : print()
# 출력 이후에 줄바꿈을 수행함
# 원치 않으면 'end'속성을 이용할 수 있음
# <예시>
print(5, end=" ")
# <예시 2>
answer = 7
print("정답은" + str(answer) + "입니다") # 문자열과 정수형 연산 불가능

# f-string
# : 문자열 앞에 접두사 'f'을 붙여 사용
# : 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있음
print(f"정답은 {answer}입니다")

# ---------------------------------------------------------

# <조건문>
# if ~ elif ~ else
x = 15
if x >= 10:
    print("x>=10")  # 파이썬에서는 코드의 블록을 들여쓰기로 지정
elif x >= -10:
    print("x>= -10")
else:
    print("hahaha")

# 파이썬의 기타 연산자
# 다수의 데이터를 담는 자료형을 위해 in 연산자와 not in 연산자가 제공
# 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용 가능

# x in 리스트 : 리스트 안에 x가 들어가 있을 때 True임
# x not in 문자열 : 문자열 안에 x가 들어가 있지 않을 때 True임

# pass
# : 아무것도 처리하고 싶지 않을 때 사용
# <예시> 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우
score = 85
if score >= 80:
    pass
else:
    print('성적이 80점 미만입니다')

# if ~ else문을 한줄에 작성하기
score = 85
result = "성공" if score >= 80 else "실패" # if 가 참이라면 result=성공 출력 거짓이면 실패
print(result) # 성공

#---------------------------------------------------------

# <반복문>
# : while문, for문

# <while문 예시>
# 1부터 9까지 모든 정수의 합 구하기
i = 1
result = 0
# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1
print(result)

# 1부터 9까지 모든 홀수의 합 구하기
i = 1
result = 0
# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)

# for문
# for 변수 in 리스트:
# 특정한 변수를 이용하여 in 뒤에 오는 데이터(리스트, 튜플)에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문

# <예시>
array = [9, 8, 7, 6, 5]
for x in array:
    print(x)

# for문에서 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용
# range(시작 값, 끝 값 + 1)
# 인자를 하나만 넣으면 자동으로 시작 값은 0이 됨

# <예시>
result =0
for i in range(1,10): # i는 1부터 9까지의 모든 값을 순회
    result += i

# continue : 반복문에서 남은 코드의 실행을 건너뛰고 다음 반복을 진행하고자 할 때 사용
# <예시>
# 1부터 9까지의 홀수 합
for i in range(1,10):
    if i % 2 == 0:
        continue
    result += i
print(result)

# break : 반복문 즉시 탈출
# <예시>
# 1부터 5까지의 정수를 차례대로 출력
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1
    
# <예시>
# 특정 번호의 학생을 제외하기
scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4} # 85점 65점 학생
for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다")

# 중첩된 반복문
# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()

#---------------------------------------------------------

# <함수>

# 함수
# def 함수명(매개변수):
#     실행할 소스코드
#     return 반환값

def add(a,b):
    return a+b
print(add(3,4))

# global
# : global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다
# <예시>
a = 0
def func():
    global a
    a += 1

for i in range(10):
    func()
print(a) # 10 출력

# <예시>
array = [1,2,3,4,5]
def func():
    global array
    array = [3,4,5]
    array.append(6)
func()
print(array) # [3,4,5,6]

# 여러 개의 반환 값
# : 파이썬 함수는 여러 개의 반환 값을 가질 수 있다.
def operator(a, b):
    add = a + b
    sub = a - b
    mult = a * b
    div = a / b
    return add, sub, mult, div

a, b, c, d = operator(4, 2)

#---------------------------------------------------------

# <람다 표현식>
# : 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있다
# : 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 특징!

# <비교>
# 일반적인 add()메서드 사용
def add(a, b):
    return a + b

print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))

# <예시>
# 내장 함수에서 자주 사용되는 람다 함수
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
def my_key(x):
    return x[1]
print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

# 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
# map() : 각각의 원소에 어떠한 함수 적용
result = map(lambda a, b: a + b, list1, list2)

print(list(result))

#---------------------------------------------------------

# <유용한 표준 라이브러리>
    # 1. 내장 함수
    # : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공

        result = sum([1, 2, 3]) # sum()
        min_result = min(7, 3, 4, 5) # min()
        max_result = max(7, 3, 4, 5) # max()
        result = eval("(3+5)*7") # eval()
        result = sorted([9,3,5,6,1], reverse=True) # sorted()
        
        array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
        result = sorted(array, key=lambda x: x[1], reverse=True) # sorted() with key
        
    # 2. itertools
    # : 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공
    
        # 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 제공하는 것
        # {'a','b','c'}에서 세개를 선택하여 나열 
            from itertools import permutations
            
            data = ['a', 'b', 'c']  # 데이터 준비
            result = list(permutations(data, 3))  # 모든 순열 구하기

        # 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
        # {'a','b','c'}에서 순서를 고려하지 않고 두개를 뽑는 경우
            from itertools import combinations
            
            data = ['a', 'b', 'c']  # 데이터 준비
            result = list(combinations(data, 3))  # 2개를 뽑는 모든 조합 구하기
            
        # 중복 순열
            from itertools import product

            data = ['a', 'b', 'c']  # 데이터 준비
            result = list(product(data,repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)

        # 중복 순열
        from itertools import combinations_with_replacement
        
        data = ['a', 'b', 'c']  # 데이터 준비
        result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
        
    # 3. heapq
    # : 힙 자료구조 제공

    # 4. bisect
    # : 이진 탐색 기능 제공

    # 5. collections
    # : 덱, 카운터 자료구조 포함

        # Counter
        # : 등장 횟수를 세는 기능, 리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇번 씩 등장했는지 알려줌

            from collections import Counter

            counter=Counter(['red','blue','red','green'])

            print(counter['blue']) # blue 등장 횟수 출력
            print(counter['red']) # red 등장 횟수 출력
            print(dict(counter)) # {'red':2, 'blue':1, 'green':1}

    # 6. math
    # : 필수적인 수학적 기능 제공 (펙토리얼, 제곱근, 최대공약수, 삼각함수, 파이)

        # 최대 공약수 -> gcd()
            import math
            # 최소 공배수 구하는 함수
            def lcm(a,b):
                return a*b//math.gcd(a,b)
            a=21
            b=14

            print(math.gcd(21,14)) # 최대 공약수 계산
            print(lcm(21,14)) # 최대 공배수 계산
