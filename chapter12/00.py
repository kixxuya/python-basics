int_num = (2)
tuple_num = (2,)
tuple_num2 = (2,3,4)  # 쉼표를 붙여야 튜플로 인식됨
tuple_num3 = 2,3,4,5,6  # 괄호를 생략해도 튜플로 인식됨

print(f"{int_num}의 타입은 {type(int_num)}입니다.")
print(f"{tuple_num}의 타입은 {type(tuple_num)}입니다.")
print(tuple_num2[1])
print(len(tuple_num2))

