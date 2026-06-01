from datetime import date

from sympy.physics.units.systems import length_weight_time

# (str 문자열 문자형 string)
# " " , ' ' , """ """, ''' ''' 감싸서 표현

print('--- 홑 따옴표')

s1 = 'Hello'
s2 = "World"

print(s1, type(s1))
print(s2, type(s2))
print( s1 + ' ' + s2 )

s3 = "'abc'"

print(s3, type(s3))

# 삼중 따음표
print("""
삼중 따옴표는
입력 된 형식 그대로 문자열(str)로 변환
""")

print("""write forward/back without enter
there is no blank""")

# str 연산
# 1. 문자열 + 문자열 = 이어쓰기
# 2. 문자열 * 양의 정수 = 양의 정수 크기 만큼 반복
print('---문자열 더하기---')
a = 'apple'
b = 'banana'
print(a + ',' + b)
print('-'*20)

# 빼기 나누기 연산은 불가
num_str = '123'
num_int = int(num_str)

print(num_int, type(num_int))

# c = '123sad'
# c_int = int(c)
# print(c_int, type(c_int))

# str method(str api)
#(ref) function, method == 기능(실행 후 결과 변환)

# len(객체): 파이썬 객체 길이 반환
# 파이썬 객체: str list tuple dict set 등
print('---len()---')
text = '오늘 점심은 뭘 먹죠?'
print(len(text))

# str.replace(old,new)
#  - str 내에서 old에 해당하는 문자를 new로 치환(변경)
print('---str.replace()---')
today = '2026-06-01'
print(today, today.replace('-','/'))


# str.strip([str])
# - 문자열 좌우 [str] delete
# - [str] 생략 시 공백 제거
# - 코드 작성법에서 []는 생략 가능

print('---str.strip()---')
some = '             kkk                '
print('[' + some + ']')
print('[' + some.strip()+ ']')

# Upper lower realated str method

origin_str = 'hEllo WolRd'
print(origin_str.upper())
print(origin_str.lower())
print(origin_str.capitalize())
print(origin_str.title())
print(origin_str.swapcase())

x = 10
print("x is %d" %x)
y = 'code'
print("y is %s" %y)

# x, y = 10, 'code'
# print('x is {0}'.format(x))
# print('x is {0} y is {1}'.format(x,y))
# print("x is {new_x} and y is {new_y}".format(new_x = x, new_y = y))
# print('{} + {} + {}'.format(x,y,x+y))

#3. f-string([PYTHON 3.6])
teacher_name = "다람쥐"
x = 1
y = 1.25
print(f"안녕하세요. 오늘부터 여러분과 함께 공부할 {teacher_name} 강사입니다~!")
print("----f-string------")
print(f"{x} + {y} = {x+y}")

# ---------------------------------
# 문자열 인덱싱/슬라이싱
# - 파이썬 문자열(str)은 text sequence 형태를 갖는다
# - sequence: 순차적인, 순서가 있는 데이터 구조
# - index: 순서(base index == 0)
print("---문자열 indexing---")
x = 'Monday'
print('length of x:', len(x)) # index 0,1,2,3,4,5
print(x[0]) # [] == 배열, [0] == str 배열 중 0번째 index
for i in range(len(x)):
    print(x[i])

# 역 인덱스: str을 거꾸로 탐색
for i in range(len(x)):
    print(x[-i-1])

# str slicing: way to bring part of sliced string
# way to write : str[start:stop:step]
# - start : start index
# - stop : final index
# - step : a number of jumping index( When you dont anything, default is 1

text = 'hello world'
print("text:", text)
print("length of text: ", len(text))

print("text[0:5:1]", text[0:5:1]) # 0-4
print("text[0:5]", text[0:5]) # 0-4
print("text[0:5]", text[:5]) # 0-4
print("text[6:11]", text[6:11])
print("text[6:len(text)]", text[6:len(text)])
print("text[6:]", text[6:])
print("text[:]", text[:])

print("text[::2]", text[::2])
print("text[0:11:2]", text[0:11:2])
print("text[::-1]", text[::-1])

# 문자열 불변타입(immutable)
print("---문자열 불변 타입---")
s = 'python' # s 에는 'python' str 메모리 주소가 저장됨
print(s, type(s)) # s 에 저장된 주소를 찾아가서 'python' str을 참조

print("변경 전 s: ", id(s)) # id(변수명):
# id(변수명): 변수에 저장된 값의 주소(위치)를 반환

s = s + ' hello'
print(s, type(s))
print("변경 후 s: ", id(s)) # id(변수명):


# in 연산자(멤버쉽 검사 연산자)
# - 특정 값이 포함되어 있는 지 검사
# - 결과는 bool 형태
print("--- in 연산자---")
txt = "gimbab, ramen, tobokki"
print('ramen' in txt)
print('gatz' in txt)