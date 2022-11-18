# Foydalanuvchidan son kiritishni so'rang,
# agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
import math

son = int(input("Son kiriting: "))
if son >= 0:
    print(math.sqrt(son))
else:
    print("Musbat son kiriting!")