# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

taomlar = ["osh", "no'xat sho'rva", "moshxo'rda", "qozonkabob", "mastava"]

# nonushta degan yangi ro'yxatga taomlardan nusxa oling

nonushta = taomlar[:]

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing

nonushta.remove("no'xat sho'rva")
nonushta.remove("qozonkabob")
nonushta.append("kasha")
nonushta.append("saryog'")

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring

print(taomlar, nonushta)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.

nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non" | Xatolik beradi. Chunki tuple ga o'zgartirish kiritib bo'lmaydi