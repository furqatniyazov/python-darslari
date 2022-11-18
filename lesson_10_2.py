# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa,
# "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring.
# Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.

foydalanuvchi_ismi = input("login kiriting: ")
if foydalanuvchi_ismi == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {foydalanuvchi_ismi}!")
