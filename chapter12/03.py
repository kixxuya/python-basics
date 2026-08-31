tags = ["Python", "AI", "Python", "Data", "AI"]
print(tags)
print(type(tags))
print(len(tags))

unique_tags = set(tags)
print(unique_tags)
print(type(unique_tags))
print(len(unique_tags))

# 인공지능을 썼는지 안썼는지
# set을 쓰지 말고 list기능만 써서 unique_tags를 구현하시오

unique_tags = []
for tag in tags:
    if not tag in unique_tags:
        unique_tags.append(tag)

print(unique_tags)