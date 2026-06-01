# Set
# - duplicated X
# - not sequence type
# - iterable O
# - method related set served
# - symbol = {}



print('---Set---')
st  = {2,1,4,1,2,3,2,2,3,4,1,4}
print(st, type(st))


print('---list -> set change(delete duplicated ones)---')
lst = [1,3,1,4,4,2,3,1,4,2,2,3,3]
st2 = set(lst)
print(st2, type(st2))
#
tpl = (1,2,3,3,4,4,4,2,1,4,2)
st3 = set(tpl)
print(st3, type(st3))

# set -> list convert
lst2 = list(st2)
print("lst2:", lst2)

# Set Add
# Set Remove
# Set Iterable
# Set Calculation

print('---component add---')
my_nums = {20,30,40}
my_nums.add(10)
my_nums.add(10)
my_nums.add(10)

print(my_nums, type(my_nums))

# Remove component
print('my_nums:', my_nums)

# 전체 제거(clear)
my_nums.clear()
print("After clear my_nums:", my_nums)

# Set Iterable
my_nums = {30,40,70,90}

# my_nums에서 값을 하나 꺼내어 num변수에 저장(빤복)
for num in my_nums:
    print(num)

# 집합연산
print('--- set 집합연산 ---')
m = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
n = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

print('합집합: ', m.union(n))
print('교집합: ', m.intersection(n))
print('차집합: ', m.difference(n))
print('대칭차집합: ', m.symmetric_difference(n)) # 합집합 - 교집합