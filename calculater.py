# ==================================================
# calculater.py
# CS50 Python / Week 0 tarzı Türkçe öğretici not dosyası
# Bu dosyada toplama, veri türü dönüşümü, ondalıklı sayılar,
# yuvarlama, sayı biçimlendirme ve fonksiyon kullanımı işlenmektedir.
# ==================================================

# ------------------------------------------------------------------
# 1) TEMEL TOPLAMA İŞLEMİ
# ------------------------------------------------------------------
# Burada doğrudan sayısal değerler ile toplama işlemi yapıyoruz.
# x ve y değişkenleri tam sayı (integer) olarak tutulur.
# z ise bu iki sayının toplam sonucunu saklar.
x = 1
y = 2
z = x + y
print(z)

print("-" * 50)

# ------------------------------------------------------------------
# 2) input() İLE GELEN VERİNİN NEDEN DÖNÜŞTÜRÜLMESİ GEREKİR?
# ------------------------------------------------------------------
# input() fonksiyonu kullanıcıdan veri alır.
# Ancak önemli bir detay vardır:
# input() ile gelen değerler sayı gibi görünse bile metin (string) olur.
# Bu yüzden iki değeri doğrudan toplamak istersek matematiksel toplama yerine
# metin birleştirme davranışı görebiliriz.

# Yanlış kullanım örneği:
# Aşağıdaki iki değer input() ile alındığında string olur.
# Eğer bunları toplarsak örneğin 1 ve 2 yerine "12" sonucu oluşabilir.
x = input("X sayısını giriniz: ")
y = input("Y sayısını giriniz: ")
print("Yanlış kullanım sonucu:", x + y)

print("-" * 50)

# ------------------------------------------------------------------
# 3) int() İLE TAM SAYIYA DÖNÜŞTÜRME
# ------------------------------------------------------------------
# int() fonksiyonu metin olarak gelen sayısal ifadeyi tam sayıya çevirir.
# Böylece artık gerçek matematiksel toplama yapabiliriz.
x = int(input("X sayısını giriniz: "))
y = int(input("Y sayısını giriniz: "))
print("Doğru kullanım sonucu:", x + y)

print("-" * 50)

# ------------------------------------------------------------------
# 4) float() İLE ONDALIKLI SAYILARLA ÇALIŞMA
# ------------------------------------------------------------------
# float() fonksiyonu sayıyı ondalıklı hale getirir.
# Bu sayede 3.5, 10.75 gibi değerlerle işlem yapabiliriz.
x = float(input("X sayısını giriniz: "))
y = float(input("Y sayısını giriniz: "))

# Burada toplamı tekrar z değişkenine atıyoruz.
# Böylece en güncel sonucu z üzerinden takip edebiliriz.
z = x + y
print(z)

print("-" * 50)

# ------------------------------------------------------------------
# 5) round() İLE YUVARLAMA
# ------------------------------------------------------------------
# round() fonksiyonu sayıları yuvarlamak için kullanılır.
# Genel kullanım yapısı şöyledir:
# round(number, ndigits=None)
#
# number  -> Yuvarlanacak sayı
# ndigits -> Virgülden sonra kaç basamak tutulacağını belirtir

# Burada toplam sonucu en yakın tam sayıya yuvarlıyoruz.
z = round(x + y)
print(z)

# Sayıyı binlik ayırıcı ile daha okunur yazdırabiliriz.
# f-string içindeki :, ifadesi sayıyı 1,000 gibi formatlar.
print(f"{z:,}")

print("-" * 50)

# ------------------------------------------------------------------
# 6) BÖLME VE ONDALIK BASAMAK GÖSTERİMİ
# ------------------------------------------------------------------
# Bölme işlemi yaptıktan sonra sonucu ister doğrudan kullanabilir,
# ister belirli bir basamağa yuvarlayabiliriz.
z = x / y
print(z)

# Burada sonucu virgülden sonra 2 basamak olacak şekilde yuvarlıyoruz.
# !!! ÖNEMLİ
# Bu kısım önemlidir çünkü gerçek hayatta özellikle para, ortalama,
# ölçüm ve raporlama gibi işlemlerde sonuçları kontrollü sayıda basamakla
# göstermek gerekir. Aksi halde gereksiz uzun ondalıklı sayılar oluşabilir.
z = round(x / y, 2)
print(z)

# f-string içinde .2f kullanımı sayıyı her zaman 2 ondalık basamakla gösterir.
# Yani sonuç 5 olsa bile ekranda 5.00 şeklinde görünebilir.
print(f"{z:.2f}")

print("-" * 50)

# ------------------------------------------------------------------
# 7) KENDİ FONKSİYONUMUZU OLUŞTURMA
# ------------------------------------------------------------------
# Fonksiyonlar tekrar eden işleri daha düzenli hale getirmek için kullanılır.
# def anahtar kelimesi ile fonksiyon tanımlarız.
#
# def square(n):
# - square -> fonksiyonun adıdır.
# - parantez içindeki n -> fonksiyona dışarıdan gelecek değeri temsil eder.
# - Bu değer fonksiyon içinde n adıyla kullanılır.
#
# Yani biri square(5) yazarsa, burada n değeri 5 olur.

# !!! ÖNEMLİ
# main() fonksiyonu önemlidir çünkü programın başlangıç akışını tek yerde toplar.
# Kod büyüdükçe hangi işlemin nerede başladığını görmek kolaylaşır.
# Bu yapı daha düzenli, okunabilir ve geliştirilebilir dosyalar yazmayı sağlar.
def main():
    x = int(input("X değerini giriniz: "))
    print("x'in karesi:", square(x))


def square(n):
    # Burada sayının karesini alıyoruz.
    # Aşağıdaki üç yöntem aynı mantığa hizmet eder:
    # return n * n
    # return n ** 2
    # return pow(n, 2)
    #
    # Biz burada pow() fonksiyonunu kullanıyoruz.
    return pow(n, 2)


main()

print("-" * 50)

# ------------------------------------------------------------------
# 8) KAYNAKÇA
# ------------------------------------------------------------------
# Ana kaynak:
# CS50 Python Notes 0
# https://cs50.harvard.edu/python/notes/0/
# Kullanım alanı: Bu dosyanın genel konusu ve örnek akışı
# İlgili satırlar: 1-143
#
# Python dokümantasyon kaynakları:
# input()
# https://docs.python.org/3/library/functions.html#input
# İlgili satırlar: 33, 34, 44, 45, 55, 56, 126
#
# print()
# https://docs.python.org/3/library/functions.html#print
# İlgili satırlar: 17, 19, 35, 37, 46, 48, 61, 63, 77, 81, 83, 91, 100, 104, 106, 127, 143
#
# int()
# https://docs.python.org/3/library/functions.html#int
# İlgili satırlar: 44, 45, 126
#
# float()
# https://docs.python.org/3/library/functions.html#float
# İlgili satırlar: 55, 56
#
# round()
# https://docs.python.org/3/library/functions.html#round
# İlgili satırlar: 76, 99
#
# pow()
# https://docs.python.org/3/library/functions.html#pow
# İlgili satırlar: 138
#
# Formatted string literals (f-string)
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# İlgili satırlar: 81, 104

"""
   (\_/)
   (•.•)   __)
   /|     /
   /> <\\
"""