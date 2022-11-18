# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring

countries = ['Uzbekistan', 'South Korea', 'Kazakhstan', 'Tajikistan', 'Indonesia', 'Spain', 'England', 'Italia', 'Russia', 'US', 'Portugal', 'Brasil']
print(countries, "\n")

# Ro'yxatning uzunligini konsolga chiqaring

print(f"Ro'yxatning uzunligi: {len(countries)}\n")

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring

print(f"Tartiblangan ro'yxat: {sorted(countries)}\n")

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

print(f"Teskari tartiblangan ro'yxat: {sorted(countries, reverse=True)}\n")

# Asl ro'yxatni qaytadan konsolga chiqaring

print("Asl ro'yxat: ", countries, "\n")

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring

countries.reverse()
print("Teskari ro'yxat: ", countries, "\n")

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.

countries.sort()
print("Alifbo bo'yicha: ", countries, "\n")
countries.sort(reverse=True)
print("Alifbo bo'yicha teskari: ", countries, "\n")
