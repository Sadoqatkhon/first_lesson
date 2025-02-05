# Juft yoki toq sonni aniqlash
# Foydalanuvchidan son kiritishni so‘rang va uning juft yoki toq ekanligini aniqlang.

# son = int(input('son kiriting: '))
# if son%2 == 0:
#     print('Juft')
# else:
#     print('Toq')


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
# # Ikki son berilgan, kattasini ekranga chiqaring.
# a = int(input('1-son'))
# b = int(input('2-son'))
#
# if a > b:
#     print(a)
# else:
#     print(b)

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
    pass


# 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

# Homework
# 7. Palindrom so‘zni aniqlash
#
# word = input('So\'z kiriting: ')
# if word == word[::-1]:
#     print(True)
# else:
#     print(False)

# 05.02.2025 kungi dars va masalalar

# 1
# Satr ichidagi unlilarni sanash
# Berilgan matndagi barcha unli harflarni sanovchi dastur yozing.
#
# unli = ['a','i','u','o','e']
# text = input('Matn kiriting: ')
# m = 0
# for k in text:
#     if k in unli:
#         m+=1
#
# print(m)

# 2
# Mukammal sonni aniqlash
# Berilgan son mukammal son (o‘zidan tashqari bo‘luvchilari yig‘indisi o‘ziga teng) ekanligini tekshiring.

# n = int(input('Bir son kiriting: '))
# yigindi = 0
# for i in range(1,n):
#     if n%i == 0:
#         yigindi += i
#
# if yigindi == n:
#     print(f' {n} soni mukammal son')
# else:
#     print(f' {n} soni mukammal son emas')

# 3
# Tub sonni aniqlash
# Berilgan son tub yoki yo‘qligini aniqlovchi funksiya yozing.
# n = int(input('Bir son kiriting: '))
# a = 0
# if n> 0:
#     for i in range(2,n-1):
#         if n % i == 0 :
#             a = 1
#             break
# if a == 0:
#     print(f'{n} tub son')
# else:
#     print(f'{n} tub son emas')


# 4 Robocontestdan masala
#
# a,b = input('Oraliqni kiriting: ').split( )
# a= int(a)
# b = int(b)
# if b >= a:
#     print('Urinishlar soni:', b-a+1 )