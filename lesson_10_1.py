# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing,
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring.
# GM uchun ikkala harfni katta qiling.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
print("\n")

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.

for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())
