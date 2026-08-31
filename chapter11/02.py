fruits = ["사과", "바나나"]
more_fruits = ["포도", "딸기", "키위"]

print("원래 fruits 과일 개수:", len(fruits))

fruits.extend(more_fruits)

print(fruits)

print("extend 후 fruits 과일 개수:", len(fruits))

