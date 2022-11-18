# Foydalanuvchidan biror butun son kiritishni so'rang.
# Foydalanuvchi kiritgan sonni 2 dan 10 gacha bo'lgan sonlardan
# qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

son = int(input("Son kiriting: "))
count = 0
for i in range(2, 11):
    if son % i == 0:
        count += 1
        print(f"{son} soni {i} soniga qoldiqsiz bo'linadi")

if count == 0:
    print(f"{son} soni 2 dan 10 gacha bo'lgan hech qaysi songa qoldiqsiz bo'linmaydi")