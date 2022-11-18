# friends nomli bo'sh ro'yxat tuzing
# va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

friends = ['Salohiddin', 'Sherzod', 'Alisher', 'Rustam', 'Dilshod', 'Shohruh', 'Laziz']

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.

friends.remove('Laziz')
friends.remove('Rustam')
friends.remove('Sherzod')

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

friends.append('Javohir')
friends.insert(0, 'Akobur')
friends.insert(4, 'Farxod')

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating.
# .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini
# friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(3))
