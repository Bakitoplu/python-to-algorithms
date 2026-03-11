# ==================================================
# 2. DOSYA: calculater.py
# CS50 Python Türkçe öğretici not dosyası
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
# main() yapısı burada çok önemlidir.
# Normalde Python'da bir fonksiyonu kullanmadan önce onu tanımlamış olmamız gerekir.
# Yani square() fonksiyonunu dosyanın üst kısmında çağıracaksak,
# Python square() tanımını daha önce görmüş olmalıdır.
#
# main() kullanınca akışı daha rahat kurabiliriz:
# Üst tarafta önce def ile fonksiyonlarımızı tanımlarız,
# alt tarafta ise sadece main() çağırırız.
# Böylece fonksiyonları mantıklı sırada yazabiliriz ve
# "çağrıyı yukarıda, tanımı aşağıda nasıl kullanırım?" sorunu yaşamayız.
#
# Kısacası main() yapısının asıl amacı sadece görüntüyü güzelleştirmek değil,
# programın çalışma akışını doğru ve kontrollü şekilde kurmaktır.
def main():
    x = int(input("X değerini giriniz: "))
    print("x'in karesi:", square(x))


def square(n):
    # Burada sayının karesini alıyoruz.
    # Aşağıdaki üç yöntem aynı mantığa hizmet eder.
    # Eski / daha açık yaklaşım:
    return n * n


def square_uslu(n):
    # Aynı işlemi üs alma operatörü ile de yapabiliriz.
    # Bu yöntem de doğrudur ve öğretici olduğu için görünür bırakıyoruz.
    return n ** 2


def square_pow(n):
    # Aynı işlemi pow() fonksiyonu ile de yapabiliriz.
    # Yani burada üç farklı yazımın da aynı mantığa çıktığını görüyoruz.
    return pow(n, 2)


main()

print("-" * 50)

# ------------------------------------------------------------------
# 8) FARKLI KARE ALMA YÖNTEMLERİNİ KARŞILAŞTIRMA
# ------------------------------------------------------------------
# Burada aynı sayı üzerinde üç farklı yaklaşımın da aynı sonucu verdiğini
# görüyoruz. Böylece eski yöntemlerin yanlış değil,
# sadece farklı yazımlar olduğunu daha net anlayabiliriz.
example_number = 5
print(f"Örnek sayı: {example_number}")
print(f"Çarpma ile kare alma: {square(example_number)}")
print(f"Üs alma ile kare alma: {square_uslu(example_number)}")
print(f"pow() ile kare alma: {square_pow(example_number)}")

print("-" * 50)

# ------------------------------------------------------------------
# 9) KAYNAKÇA
# ------------------------------------------------------------------
# Ana kaynak:
# CS50 Python Notes 0
# https://cs50.harvard.edu/python/notes/0/
# Kullanım alanı: Bu dosyanın genel konusu ve örnek akışı
# İlgili satırlar: 1-166
#
# Python dokümantasyon kaynakları:
# input()
# https://docs.python.org/3/library/functions.html#input
# İlgili satırlar: 32, 33, 43, 44, 54, 55, 129
#
# print()
# https://docs.python.org/3/library/functions.html#print
# İlgili satırlar: 16, 18, 34, 36, 45, 47, 58, 60, 74, 78, 80, 88, 97, 101, 103, 130, 149, 150, 151, 152
#
# int()
# https://docs.python.org/3/library/functions.html#int
# İlgili satırlar: 43, 44, 129
#
# float()
# https://docs.python.org/3/library/functions.html#float
# İlgili satırlar: 54, 55
#
# round()
# https://docs.python.org/3/library/functions.html#round
# İlgili satırlar: 73, 96
#
# pow()
# https://docs.python.org/3/library/functions.html#pow
# İlgili satırlar: 126
#
# Formatted string literals (f-string)
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# İlgili satırlar: 78, 101, 149, 150, 151, 152

"""
   (\_/)
   (•.•)   __)
   /|     /
   /> <\\
"""