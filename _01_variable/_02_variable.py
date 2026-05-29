

# 변수 (variable)
# - 값(literal)을 저장하는 메모리 상의 공간
# - 각 변수마다 이름이 지정되어 있음(이름을 불러서 사용)

a = 19231293
b = "김성훈"




num = 100
print("num =", num)

num = 304823094839048.392482948204
print("num =", num)

num = 'Hello world'
print("num =", num)
print(type(num))


밥조 = "4조"
print("밥조 =", 밥조)

#변수명은 숫자로 시작해서는 안된다!!!!!!!!!!!!!!!!!!(문법 오류 == 빨간줄)

name_1 = "kongi"
# 1_name = '팥쥐' 는 에러
_1_name = '신데렐라'


# 특수 문자는 언더스코어(_)를 제외하고 사용 불가
# team-name = 'dasjkdf'


# 예약어는 변수명으로 사용 불가
# for if else etc


# python 예약어 종류 확인
import keyword
print(keyword.kwlist)