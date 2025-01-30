# Juft yoki toq sonni aniqlash
# Foydalanuvchidan son kiritishni so‘rang va uning juft yoki toq ekanligini aniqlang.

son = int(input('son kiriting: '))
if son%2 == 0:
    print('Juft')
else:
    print('Toq')


# Fahrenheit → Celsius aylantirish
# Berilgan haroratni Fahrenheitdan Celsiusga aylantiruvchi dastur yozing.

# t = int(input('Temperature: \n >>>'))
# f_2_c = (t - 30)*2
# print(f_2_c)

#Doira yuzi
# r = int(input('Radius \n >>>'))
# PI = 3.1415
# s = PI * r**2
# print(f'Doira yuzasi:{s:.1f}')


# Katta yoki kichik sonni aniqlash
# Ikki son berilgan, kattasini ekranga chiqaring.
a = int(input('1-son'))
b = int(input('2-son'))

if a > b:
    print(a)
else:
    print(b)

# String teskari qilish
# Foydalanuvchidan so‘z kiritishni so‘rang va uni teskari qilib ekranga chiqaring.

# word = input('So\'z kiriting: ')
# print(word[::-1])

# 3 ga va 5 ga bo‘linadigan sonlarni topish
# Berilgan diapazondagi barcha 3 va 5 ga bo‘linadigan sonlarni ekranga chiqaring.

# stop = int(input('Son kiriting: '))
# l = range(1,stop+1)
# l1 = []
# for i in l:
#     if i%3 == 0 or i%5 == 0:
#         l1.append(i)
# else:
#     print(l1)


# Fibonacci ketma-ketligi
# Berilgan n ta Fibonacci sonlarini chiqaruvchi dastur yozing.
# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n <= 1:
        return 1


# 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