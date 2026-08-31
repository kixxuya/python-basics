fruits = ["사과", "바나나", "사과", "포도"]


for i, fruit in enumerate(fruits):
    print("인덱스", i, ": ", fruit)


for i in range(len(fruits)):
    print("인덱스", i, ": ", fruits[i])

# 값이 있는가 - bool
print("바나나" in fruits)
print("키위" in fruits)

print(fruits.count("사과"))

print(fruits.index("포도"))