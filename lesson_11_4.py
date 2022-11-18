# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
# Yangi, savat degan bo'sh ro'yxat yarating
# va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring
# va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor"
# aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
#

mahsulotlar = ['sabzi', 'kartoshka', 'piyoz', 'pomidor', 'bodring', 'guruch', 'non', 'mosh', 'qaymoq', 'qatiq']
savat = []

for i in range(0, 5):
    savat.append(input(f"{i+1}-mahsulotni kiriting: "))

for s in savat:
    if s.lower() in mahsulotlar:
        print(s, "do'konda bor.")
    else:
        print(s, "do'konda yo'q.")
print("\n")

# Yuqoridagi dasturni quyidagicha o'zgartiring:
# foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi,
# bor_mahsulotlar degan ro'yxatga,
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.
# Agar mavjud_emas ro'yxati bo'sh bo'lsa,
# "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni,
# aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

bor_mahsulotlar = []
mavjud_emas = []

for s in savat:
    if s.lower() in mahsulotlar:
        bor_mahsulotlar.append(s)
    else:
        mavjud_emas.append(s)

if len(mavjud_emas) == 0:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor.")
else:
    print(f"Quyidagi mahsulotlar do'konimizda yo'q:\n{mavjud_emas}")
