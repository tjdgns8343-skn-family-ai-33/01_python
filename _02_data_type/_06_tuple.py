# tuple
# - 변경 불가(immutable)한 list
# - sequence type (indexing, slicing, iterable)

print("---tuple---")
t1 = () # empty tuple
t2 = (10) # (int)10
t3 = (10,) # (tuple)(10)
t4 = (10,20,30)
t5 = 10,20 # () 생략 -> automatically packing
t6 = 10, (20,30)
print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4, type(t4))
print(t5, type(t5))
print(t6, type(t6))
print(t6[1])

# tuple indexing, reading

tpl = ('a','b','c','d'  )
print(tpl[0],tpl[1],tpl[2],tpl[3])

# tpl[0] = 'A'
# print(tpl[0],tpl[1],tpl[2],tpl[3])

# tuple slicing
print("---tuple slicing---")
print(tpl[0:2]) # 'a', 'b'
print(tpl[1::2])

# tuple unpacking
print('---tuple unpacking---')
q,w,e,r = tpl
print(q,w,e,r)

*r, t = tpl
print(r,t)
print(type(r))

# tuple을 이용한 변수 값 할당
print(("---designate values with unpacking"))
num1, num2 = 100,200 # directly omited
print(num1, type(num1))
print(num2, type(num2))

print("---swap with tuple---")
num1, num2 = num2, num1

