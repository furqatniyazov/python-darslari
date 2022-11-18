# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing.
# Ro'yxatni konsolga chiqaring.

peoples = []
for i in range(0, int(input("Bugun nechta odam bilan uchrashdingiz?: "))):
    peoples.append(input(f"{i+1}-odamning ismini kiriting: "))

print("Bugun uchrashgan odamlar ro'yxati:", peoples)