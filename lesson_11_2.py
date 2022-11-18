# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm


age = int(input("Yoshingizni kiriting: "))
if age <= 4 or age >= 60:
    print("Kirish bepul!")
elif age < 18:
    print("Kirish 10000 so'm")
else:
    print("Kirish 20000 so'm")