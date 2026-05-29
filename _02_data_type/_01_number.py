# number(숫자)
# 정수
# 실수
# 복소수

#type(변수명 | 값) 함수 : 변수 또는 값의 타입을 확인하는 내장 함수
# 정수(int)
n = 123
print(n, type(n))

price = 1_000_000_000;
print(price, type(price))

import sys
print(sys.maxsize, type(sys.maxsize))

#2진법, 8진법, 16진법

a = 0b100
print(a, type(a))

b = 0o23
print(b, type(b))

c = 0xff
print(c, type(c))



#----------------------------

#실수(float)
f1 = 123.456
print(f1, type(f1))

f2 = -99999.99999
print(f2, type(f2))

# 소수점 아래 16자리 까지 표현 가능
f3 = 1.01234657890123456789
print(f3, type(f3))


#----------------------------

#복소수(complex number)
c1 = 5+4j
print(c1, type(c1))

d = f1 + c1
print(d, type(d))

s1 = 'abc'
print(s1, type(s1))

print(2**64)
print(2**64 - 1)

print( 2**128 > 2**63)