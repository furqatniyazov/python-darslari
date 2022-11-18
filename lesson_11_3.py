# Foydalanuvchidan ikita son kiritishni so'rang,
# sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

if son1 > son2:
    print(son1, "soni", son2, "sonidan katta")
elif son1 < son2:
    print(son2, "soni", son1, "sonidan katta")
else:
    print("Sonlar o'zaro teng")