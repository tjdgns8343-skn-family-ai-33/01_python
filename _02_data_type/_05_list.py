# sequence type
# - str, list, tuple
# - keep the sequence of stored values
# - possible for indexing and slicing
# - 순회(iterable) 가능


# List
# - many values(literal)을 묶어서 정리(container data type)
# - feature: changable list size with motion


print("---list---")
lst = [1,2,3,4,5]
print("lst: ",lst)
print("len(lst): ",len(lst))
print("lst[0]: ", lst[0])
print("lst[1]: ", lst[1])
print("lst[2]: ", lst[2])
print("lst[:]: ", lst[:])

# - list는 동적으로 크기변경이 가능한 mutable 자료형이다!
# - mutable: list,set,dict
# - immutable: int, float, bool, str, tuple
print("---mutable check---")
print("lst: ",lst)
print("before append id", id(lst))

before_id = id(lst)

# list.append(value)
lst.append(999)
print("lst: ",lst)
print("after append id", id(lst))
print('append before after same? : ', before_id == id(lst))


# list.insert(index, 값)
# - index에 값을 삽입하는 메서드
# - every values get back by one from designated index

print("---list.insert()---")
lst.insert(1,1.5)
lst.insert(0,0)
print("after insert lst: ",lst)
print('insert before after same? : ', before_id == id(lst))

# list update(수정)
# list 저장요소 추가/수정/삭제
print("--list update---")
lst[0] = -10
print("lst", lst)

# 특정 인덱스 값 제거
# list.pop(index): 해당 인덱스 값이 제거
# 제거된 index 뒤 요소들을 한 칸씩 당김
print("---list remove---")
lst.pop(2)
print("lst", lst)
print('id(lst): ', id(lst))

# 2차원 list
students = [
    ['Kim', 1],
    ['Seong', 2],
    ['Hoon',3]
]

print("students: ", students)
print("students[0]: ", students[0][0])
print(len(students))
# print(len(students[0][0]))

# str.split(구분자)
# - str을 구분자를 기준으로 나눠서 list 형태로 반환

# print(len(students[0][1]))

# 10시 20분 상봉역 출발 - 40분 입석 - 50분 좌석
# 12시 - 2시 밥 순두부? 메밀막국수? 감자옹심이?
# 2시 - 7시 서핑 커피 간식
# 8시 저녁 조개구이 라면

# csv(Comma Separated Value)
data = "KIM, 28, Seoul, Seochogu"
data_ = data.split(',')
print('data_ :', data_)

print(data)

# list Slicing(same with slicing str)
print("---List Slicing---")

texts = ['hello','안녕','곤니찌와','봉주르','Hallo']

print(texts[:2])
print(texts[1:3])
print(texts[:3:2])
print(texts[2:])

# change list values with slicing
print(texts)
texts[0:2] = ["aaa","bbb"]
print(texts)
texts[1:3:1] = ["^^","ㅡㅡ"]

print("---plus function list---")
a = [10,10]
b = [30,40]
a = a+b
print(a)

b = b+a

print(b)

# list 순회(순차 접근, 순차 반복)
# - iterable 특징을 가지는 자료형만 가능
print("---list iterable---")
lst = ['a','b','c']

for v in lst:
    print(v)

# list index, value iterable
for index, v in enumerate(lst):
    print(f'lst[{index}] : {v}')


# list api
print("---list.count(value)---") #how many the same values are in list
fruits = ['apple','banana','cherry','apple','melon']
print('fruits.count("apple"): ', fruits.count("apple"))
print('fruits.count("banana"): ', fruits.count("banana"))
print('fruits.count("melon"): ', fruits.count("melon"))
print('fruits.count("kiwi"): ', fruits.count("kiwi"))

# sort
# list.sort() : 원본 리스트 내에서 정렬(in-place)
# -> 원본 데이터가 변경 (원본 데이터 손실)

# sorted(list) : 정렬된 새 리스트를 반환 (not in place)
# -> 원본 데이터가 별도로 유지

print("---list.sort()---")
nums = [100,30,50,60,20]
print("nums: ", nums)
nums.sort()
print(nums) # 정렬 수행
nums.sort(reverse=True)
print(nums)

print('---key 속성 -> 정렬 기준 함수---')
fruits.append("kiwi")
print("fruits: ", fruits)

# len 함수를 정렬 기준으로 설정
fruits.sort(key = len)
print("정렬 후 fruits:", fruits)


# 커스텀 정렬기준함수
print("---custom sorting---")
fruits.sort(key = len, reverse = True)
def my_sort(elem):
    return len(elem), elem # tuple로 우선순위 지정

fruits.sort(key=my_sort)
print(fruits)


# sorted(list) : 원본 유지 정렬(new list 반환)
print("---sorted(list)---")
nums = [9,2,4,7,1]
nums_2 = sorted(nums)
print("nums :", nums)
print("nums_2 :", nums_2)



# list unpacking
# list == 변수의 묶음
print("---unpacking---")
nums = [9,2,4,7,1]
numbers = [10,20,30]
a,b,c = numbers
print("a :", a)
print("b :", b)
print("c :", c)

# d = 0번 인덱스 요소(10)
# *e = 1,2 인덱스 요소[20,30] -> 나머지를 list 형태로 변환
d, *e = numbers
print(d,e)

numbers = [10,20,30,40,50]
a, *b, c = numbers
print("a :", a)
print("b :", b)
print("c :", c)

