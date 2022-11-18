# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
# Foydalanuvchidan yangi login tanlashni so'rang
# va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
# Agar ro'yxatda bunday login mavjud bo'lsa,
# "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

foydalanuvchilar = ['login1', 'login2', 'login3', 'login4', 'login5']

foydalanuvchi = input("Loginni kiriting: ")

if foydalanuvchi in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {foydalanuvchi}!")
