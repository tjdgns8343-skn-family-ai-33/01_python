


# 논리형 Boolean

a = True
b = False
# print(a, type(a))
# print(b, type(b))
#
# print(a == b )
# print(a != b )
# print(a < b )
# print(a <= b )
# print(a >= b )


# and or
a = 1
b = 3
print( a != b and 100 >99 and True)



# T or T == T
# T or F == T
# F or T == T
# F or F == F

# 60점 이상 입력 시 합격 (True) / 아니면 불합격 (False)
print("---합격/불합격---")
#
score = int(input('점수를 입력하세요: '))
# if score >= 60 and score <= 100:
#     print('합격')
# elif score >= 0 and score <= 60:
#     print('불합격')
# else:
#     print('Error')

result = score >=60
print( '합격 여부:', '합격' if result == True else '불합격')
