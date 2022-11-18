# Quyida bir nechta kodlar berilgan, kodlar avvalgi darsdagi uy vazifalaridan iborat.
# Kodlardagi xatolarni toping va to'g'rilang.
# Har bir dasturda bir nechta xatolar mavjud bo'lishi mumkin.
# Xatolarni topish uchun dasturlarni bir necha marta, turli qiymatlar bilan bajarib ko'ring.

# son = float(input("Juft son kiriting: ")  # ) qolib ketgan (SyntaxError)
# if son%2==0:
#     print("Bu son juft emas.')  # satr " bilan boshlanib, ' bilan tugagan (SyntaxError)
# else:
#     print("Rahmat!"))  # bitta ) ortiqcha (SyntaxError)

# --------------------------------------------------------------------------------

# yosh = (input("Yoshingiz nechida?"))
#
# if yosh<=4 or yosh>=60: # yosh o'zgaruvchisi String turida (TypeError)
#     narh = 0
# elif yosh < 18  # : qolib ketgan (SyntaxError) va yosh o'zgaruvchisi String turida (TypeError)
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")


# --------------------------------------------------------------------------------


# x = float(input("Birinchi sonni kiriting: ")) # ) qolib ketgan (SyntaxError)
# y = float(input("Ikkinchi sonni kiriting: ")) # ) qolib ketgan (SyntaxError)
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     # print(f'{x}<{y}")  #  satr ' bilan boshlanib " bilan tugagan (SyntaxError)
# else  # : qolib ketgan (SyntaxError)
#     print(f"{x}>{y}") # : bo'lmaganidan keyin tabulyatsiya xatoligi hisoblanadi (IdentationError)

# --------------------------------------------------------------------------------

    # print("Savatingiz bo'sh")  # tabulyatsiya xatoligi (IdentationError)
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
    # savat.append(input(f'Savatga {n+1}-mahsulotni qo'shing: '))  # ' bilan ochilgan va orada ' belgi bo'lib yopilgan. Undan keyin yana bitta ochilgan (SyntaxError)

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         # bor_mahsulotlar.append(mahslot)  # mahslot deb nomlangan o'zgaruvchi yo'q (NameError)
#     else:
#         mavjud_emas.append(mahsulot)
#
# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# ------------------------------------------------------------------------------------------

# users = ['alisher1983','aziza','yasina' 'umar']
#
# # login = input("Yangi login tanlang:' )  # " bilan ochilgan satr ' bilan yopilgan (SyntaxError)
#
# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")