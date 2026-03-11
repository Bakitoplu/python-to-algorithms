# ==================================================
# 3. DOSYA: compare.py
# CS50 Python Türkçe öğretici not dosyası
# Bu dosyada if, elif, else, karşılaştırma operatörleri
# ve birden fazla farklı karşılaştırma yaklaşımı işlenmektedir.
# ==================================================

# ------------------------------------------------------------------
# 1) KULLANICIDAN İKİ DEĞER ALMA
# ------------------------------------------------------------------
# input() ile gelen veriler metin olduğu için,
# int() kullanarak bunları tam sayıya çeviriyoruz.
x = int(input("X değeri nedir? "))
y = int(input("Y değeri nedir? "))

print("-" * 50)

# ------------------------------------------------------------------
# 2) İLK YAKLAŞIM: ÜÇ AYRI if KULLANIMI
# ------------------------------------------------------------------
# Bu yaklaşım çalışır.
# Çünkü her koşul ayrı ayrı kontrol edilir.
#
# Ancak burada küçük bir verimsizlik vardır:
# x > y doğruysa, x < y ve x == y kontrollerini tekrar sormaya gerek kalmaz.
# Buna rağmen bu yapı öğretici olduğu için görmek faydalıdır.
if x > y:
    print("X, Y'den daha büyüktür")
if x < y:
    print("X, Y'den daha küçüktür")
if x == y:
    print("X, Y'ye eşittir")

print("-" * 50)

# ------------------------------------------------------------------
# 3) DAHA İYİ YAKLAŞIM: if / elif / else
# ------------------------------------------------------------------
# !!! ÖNEMLİ
# Bu yapı önemlidir çünkü koşullar birbirini dışlayan durumlardır.
# Yani x hem büyük hem küçük hem de eşit olamaz.
# Bu yüzden ilk doğru koşul bulunduğunda diğerlerini tekrar kontrol etmek yerine
# elif ve else kullanmak daha mantıklıdır.
if x > y:
    print("X, Y'den daha büyüktür")
elif x < y:
    print("X, Y'den daha küçüktür")
else:
    print("X, Y'ye eşittir")

print("-" * 50)

# ------------------------------------------------------------------
# 4) EŞİT DEĞİL MANTIĞI: or KULLANIMI
# ------------------------------------------------------------------
# Bu yaklaşım mantık olarak çalışır.
# Çünkü x < y veya x > y ise zaten sayılar eşit değildir.
#
# Ama bu yazım gereksiz yere uzun kalır.
# Çünkü Python'da bunun için doğrudan != operatörü vardır.
if x < y or x > y:
    print("X, Y'ye eşit değildir")
else:
    print("X, Y'ye eşittir")

print("-" * 50)

# ------------------------------------------------------------------
# 5) DAHA KISA YAKLAŞIM: != KULLANIMI
# ------------------------------------------------------------------
# Bu sürüm, bir öncekiyle aynı işi daha kısa şekilde yapar.
# != operatörü "eşit değil" anlamına gelir.
if x != y:
    print("X, Y'ye eşit değildir")
else:
    print("X, Y'ye eşittir")

print("-" * 50)

# ------------------------------------------------------------------
# 6) KAYNAKÇA
# ------------------------------------------------------------------
# Ana kaynak:
# CS50 Python Notes 1
# https://cs50.harvard.edu/python/notes/1/
# Kullanım alanı: if statements, elif, else, or, compare örneği
# İlgili satırlar: 1-98
#
# Python dokümantasyon kaynakları:
# input()
# https://docs.python.org/3/library/functions.html#input
# İlgili satırlar: 11, 12
#
# int()
# https://docs.python.org/3/library/functions.html#int
# İlgili satırlar: 11, 12
#
# print()
# https://docs.python.org/3/library/functions.html#print
# İlgili satırlar: 14, 15, 27, 29, 31, 44, 46, 48, 61, 63, 72, 74

"""
   (\_/)
   (•.•)   __)
   /|     /
   /> <\\
"""