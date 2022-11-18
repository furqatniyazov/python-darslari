# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
mylist = list(range(120, 1201, 2))

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

print("Sonlar yig'indisi: ", sum(mylist), "\n")

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring

print("Eng kattasi va eng kichigining ayirmasi: ", max(mylist) - min(mylist), "\n")

# Ro'yxatdagi elementlar sonini hisoblang

print("Elementlar soni: ", len(mylist), "\n")

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(mylist[:20])
print(mylist[260:281])
print(mylist[-20:])

