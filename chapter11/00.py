scores = [86, 92, 78, 66, 77, 88, 99, 100, 55, 25, 50]

print(scores)

print(scores[0])


total = 0
for score in scores:
    total += score
print(f"총점은 {total}입니다.")

mean_score = sum(scores) / len(scores)
print(f"평균 점수는 {mean_score}입니다.")

print(f"총 합계 점수는 {total}이고, 인원은 {len(scores)}명 입니다. 이때 평균은 {mean_score}입니다.")

# 그룹이 2그룹 상위(51~100} 하위(1~50)그룹의 합계, 인원수 평균을 각각 출력하시오.

high_group = [score for score in scores if 51 <= score <= 100]
low_group = [score for score in scores if 1 <= score <= 50]

print(f"상위 그룹 점수 통계(51~100점) - 합계: {sum(high_group)}, 인원수: {len(high_group)}, 평균: {sum(high_group)/len(high_group) if len(high_group) > 0 else 0}")
print(f"하위 그룹 점수 통계(1~50점) - 합계: {sum(low_group)}, 인원수: {len(low_group)}, 평균: {sum(low_group)/len(low_group)if len(low_group) > 0 else 0}")


# 또는


count_high = 0
count_low = 0

total_high = 0
total_low = 0

for score in scores:
    if score >= 51:
        count_high += 1
        total_high += score
    else:
        count_low += 1
        total_low += score

avg_high = total_high / count_high if count_high > 0 else 0
avg_low = total_low / count_low if count_low > 0 else 0

print(f"상위 그룹 점수 통계(51~100점) - 합계: {total_high}, 인원수: {count_high}, 평균: {avg_high}")
print(f"하위 그룹 점수 통계(1~50점) - 합계: {total_low}, 인원수: {count_low}, 평균: {avg_low}")