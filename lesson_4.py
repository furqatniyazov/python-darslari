# "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring

say_hello_world = "Hello World!"  # say_hello_world o'zgaruvchisini ochib, unga string turidagi "Hello World!" qiymatini berdik
print(say_hello_world)  # say_hello_world o'zgaruvchisini chaqirib, uni qiymatini ekranga chiqardik (print() funksiyasi yordamida)



# xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.

xabar = "xabar1"  # xabar nomli o'zgaruvchi ochib unga "xabar1" qiymatini berdik
print(xabar)  # xabar qiymatini ("xabar 1")ni ekranga chiqardik
xabar = "xabar2"  # xabar o'zgaruvchisiga yangi qiymat ("xabar2") berdik
print(xabar)  # xabar qiymatini ("xabar 2")ni ekranga chiqardik



# class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?) Quyidagi kodni bajaring:

# class = 5
# print(class) o'zgaruvchiga class deb nom berib bo'lmaydi. Chunki class so'zi Python dasturlash tilida maxsus so'z hisoblanadi.



# Quyidagi kodni bajaring (Shift+Enter tugmasini bosing):

radius = 5  # radius o'zgaruvchisi ochildi va unga Integer turidagi 5 qiymati berildi
pi = 3.14159  # pi o'zgaruvchisi ochildi va unga Double/Float turidagi 3.14159 qiymati berildi
aylana_yuzi = pi * radius ** 2  # aylana_yuzi o'zgaruvchisi ochildi va unga radius kvadratiga pi ko'paytmasi o'zlashtirildi
print("Radiusi", radius, "ga teng aylananing yuzi=", aylana_yuzi)  # ekranga "Radiusi 5 ga teng aylananing yuzi= 78.53975" matni chiqarildi
