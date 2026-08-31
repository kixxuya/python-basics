
fruits = ["사과", "바나나", "포도", "딸기"]

# 값으로 삭제, remove()는 반환하는 값이 없음.
fruits.remove("바나나")

print(fruits)

# 인덱스로 삭제, pop()는 삭제한(삭제 당한) 값을 반환함. 보통 꺼내온 값을 사용할 때 사용함.
removed = fruits.pop(1)

print(removed)
print(fruits)

del fruits[0]

print(fruits)