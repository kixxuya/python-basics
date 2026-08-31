# 2부터 시작해서 8미만으로 2씩 증가하는 수를 출력
for i in range(2, 8, 2):
    print(i)

subjects = "Python"

for i in range(5):
    print(f"5번째: {subjects}")

for i in [0,1,2,3,4]:
    print(f"5,번째: {subjects}")


i = 0
for k in range(5):
    i += k
print(i)

total = sum(range(5))
print(total)

y = 0
print(y for y in range(1,11,2))


for number in range(1, 6):
    if number % 2 == 0:
        print(f"{number}는 짝수입니다.")
    else:
        print(f"{number}는 홀수입니다.")

for number in range(1, 6):
    print(f"{number}는 {"짝수" if number % 2 == 0 else "홀수"}입니다.")