# ==================================================
# grade.py
# CS50 Python / Week 1 tarzı Türkçe öğretici not dosyası
# Bu dosyada karşılaştırma operatörleri, and kullanımı,
# zincirli karşılaştırma ve daha kısa not hesaplama mantığı işlenmektedir.
# ==================================================

# ------------------------------------------------------------------
# 1) KULLANICIDAN PUAN ALMA
# ------------------------------------------------------------------
# input() kullanıcıdan veri alır.
# int() ise gelen metni tam sayıya çevirir.
score = int(input("Puan: "))

print("-" * 50)

# ------------------------------------------------------------------
# 2) İLK YAKLAŞIM: and İLE AÇIK ARALIK KONTROLÜ
# ------------------------------------------------------------------
# Bu yöntem çalışır ve mantık olarak doğrudur.
# Her not aralığını alt ve üst sınırla tek tek kontrol ederiz.
#
# Burada önemli olan nokta şudur:
# Örneğin A notu verirken hem 90'dan büyük/eşit olmasını
# hem de 100'den küçük/eşit olmasını ayrıca kontrol ediyoruz.
# Bu yaklaşım öğretici olduğu için görmek faydalıdır.
if score >= 90 and score <= 100:
    print("Seviye: A")
elif score >= 80 and score < 90:
    print("Seviye: B")
elif score >= 70 and score < 80:
    print("Seviye: C")
elif score >= 60 and score < 70:
    print("Seviye: D")
else:
    print("Seviye: F")

print("-" * 50)

# ------------------------------------------------------------------
# 3) DAHA TEMİZ YAKLAŞIM: ZİNCİRLİ KARŞILAŞTIRMA
# ------------------------------------------------------------------
# !!! ÖNEMLİ
# Bu yapı önemlidir çünkü Python'da karşılaştırmaları zincirli şekilde yazabiliriz.
# Yani 90 <= score <= 100 ifadesi,
# "score hem 90'dan büyük/eşit hem de 100'den küçük/eşit mi?"
# sorusunu tek satırda daha temiz şekilde anlatır.
#
# Bu sürüm, bir öncekiyle aynı işi yapar.
# Ama yazımı daha kısa ve daha okunurdur.
if 90 <= score <= 100:
    print("Seviye: A")
elif 80 <= score < 90:
    print("Seviye: B")
elif 70 <= score < 80:
    print("Seviye: C")
elif 60 <= score < 70:
    print("Seviye: D")
else:
    print("Seviye: F")

print("-" * 50)

# ------------------------------------------------------------------
# 4) EN KISA VE EN PRATİK YAKLAŞIM
# ------------------------------------------------------------------
# Bu son sürüm, yukarıdaki mantığın daha sade halidir.
#
# Burada üst sınırları tekrar tekrar yazmıyoruz.
# Çünkü if / elif yapısı yukarıdan aşağıya sırayla çalışır.
# Örneğin score 95 ise ilk koşul sağlanır ve program aşağı inmez.
# Bu yüzden sonraki satırlarda ayrıca "100'den küçük mü"
# ya da "90'dan küçük mü" diye tekrar kontrol yazmamız gerekmez.
#
# Yani bu yapı daha kısa olduğu için değil sadece,
# gereksiz kontrolleri kaldırdığı için de daha güçlüdür.
if score >= 90:
    print("Seviye: A")
elif score >= 80:
    print("Seviye: B")
elif score >= 70:
    print("Seviye: C")
elif score >= 60:
    print("Seviye: D")
else:
    print("Seviye: F")

print("-" * 50)

# ------------------------------------------------------------------
# 5) KAYNAKÇA
# ------------------------------------------------------------------
# Ana kaynak:
# CS50 Python Notes 1
# https://cs50.harvard.edu/python/notes/1/
# Kullanım alanı: Conditionals, and, zincirli karşılaştırma, grade örneği
# İlgili satırlar: 1-79
#
# Python dokümantasyon kaynakları:
# input()
# https://docs.python.org/3/library/functions.html#input
# İlgili satırlar: 10
#
# int()
# https://docs.python.org/3/library/functions.html#int
# İlgili satırlar: 10
#
# print()
# https://docs.python.org/3/library/functions.html#print
# İlgili satırlar: 12, 31, 52, 73, 79

"""
   (\_/)
   (•.•)   __)
   /|     /
   /> <\\
"""