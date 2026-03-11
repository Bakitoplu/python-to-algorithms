# ==================================================
# 5. DOSYA: parity.py
# CS50 Python Türkçe öğretici not dosyası
# Bu dosyada modulo (%) kullanımı, çift / tek sayı kontrolü,
# fonksiyon yazımı ve daha kısa boolean dönüş mantığı işlenmektedir.
# ==================================================

# ------------------------------------------------------------------
# 1) İLK YAKLAŞIM: DOĞRUDAN ÇİFT / TEK KONTROLÜ
# ------------------------------------------------------------------
# Kullanıcıdan bir sayı alıyoruz.
# int() ile gelen veriyi tam sayıya çeviriyoruz.
x = int(input("X değerini giriniz: "))

# Modulo (%) operatörü bir bölme işleminin kalanını verir.
# Örneğin 5 % 2 sonucu 1 olur.
# Çünkü 5 sayısı 2'ye bölündüğünde kalan 1'dir.
#
# Çift sayılar 2'ye bölündüğünde kalan 0 verir.
# Tek sayılar ise kalan 1 verir.
if x % 2 == 0:
    print("X sayısı çifttir")
else:
    print("X sayısı tektir")

print("-" * 50)

# ------------------------------------------------------------------
# 2) main() İLE AKIŞI YÖNETME
# ------------------------------------------------------------------
# !!! ÖNEMLİ
# main() yapısı burada çok önemlidir.
# Normalde Python'da bir fonksiyonu kullanmadan önce onu tanımlamış olmamız gerekir.
# Yani ciftek() fonksiyonunu dosyanın üst kısmında çağıracaksak,
# Python ciftek() tanımını daha önce görmüş olmalıdır.
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

    if ciftek(x):
        print("Çifttir")
    else:
        print("Tektir")


# ------------------------------------------------------------------
# 3) İLK FONKSİYONLU YAKLAŞIM
# ------------------------------------------------------------------
# def ciftek(n):
# - ciftek -> fonksiyonun adıdır.
# - n -> dışarıdan gelecek sayıyı temsil eden parametredir.
#
# Bu ilk sürümde işlemi açık açık yazıyoruz.
# Yani sayı çiftse True, değilse False döndürüyoruz.
def ciftek(n):
    if n % 2 == 0:
        return True
    else:
        return False


print("-" * 50)

# ------------------------------------------------------------------
# 4) DAHA KISA YAKLAŞIM: TEK SATIRDA True / False
# ------------------------------------------------------------------
# Bu sürüm de çalışır.
# Burada if ve else yapısını tek satırda yazıyoruz.
#
# return True if n % 2 == 0 else False
# ifadesi şu anlama gelir:
# Eğer sayı çiftse True döndür, değilse False döndür.
def ciftek_tek_satir(n):
    return True if n % 2 == 0 else False


print("-" * 50)

# ------------------------------------------------------------------
# 5) EN TEMİZ YAKLAŞIM: DOĞRUDAN BOOLEAN DÖNDÜRME
# ------------------------------------------------------------------
# !!! ÖNEMLİ
# Bu yapı önemlidir çünkü n % 2 == 0 ifadesi zaten kendi başına
# True veya False üretir.
# Bu yüzden ayrıca "if çiftse True döndür, değilse False döndür"
# yazmak zorunda değiliz.
#
# Yani aşağıdaki sürüm, önceki iki fonksiyonla aynı işi yapar.
# Ama daha kısa, daha net ve daha Pythonic bir yazımdır.
def ciftek_kisa(n):
    return n % 2 == 0


print("-" * 50)

# ------------------------------------------------------------------
# 6) FARKLI YAKLAŞIMLARI KARŞILAŞTIRMA
# ------------------------------------------------------------------
# Şimdi aynı sayı üzerinde üç farklı yaklaşımın da aynı sonucu verdiğini
# görmek için örnek bir kontrol yapıyoruz.
# Böylece eski yöntemle yeni yöntem arasındaki farkın sadece yazımda
# olduğunu, mantığın aynı kaldığını daha net görebiliriz.
example_number = 8
print(f"Örnek sayı: {example_number}")
print(f"İlk fonksiyonlu yaklaşım sonucu: {ciftek(example_number)}")
print(f"Tek satırlı yaklaşım sonucu: {ciftek_tek_satir(example_number)}")
print(f"Kısa yaklaşım sonucu: {ciftek_kisa(example_number)}")

print("-" * 50)

# ------------------------------------------------------------------
# 7) PROGRAMI ÇALIŞTIRMA
# ------------------------------------------------------------------
# En sonda main() çağırıyoruz.
# Böylece programın asıl kullanıcı etkileşimli kısmı burada başlıyor.
main()

print("-" * 50)

# ------------------------------------------------------------------
# 8) KAYNAKÇA
# ------------------------------------------------------------------
# Ana kaynak:
# CS50 Python Notes 1
# https://cs50.harvard.edu/python/notes/1/
# Kullanım alanı: Modulo, parity, boolean return, custom function
# İlgili satırlar: 1-104
#
# Python dokümantasyon kaynakları:
# input()
# https://docs.python.org/3/library/functions.html#input
# İlgili satırlar: 11, 35
#
# int()
# https://docs.python.org/3/library/functions.html#int
# İlgili satırlar: 11, 35
#
# print()
# https://docs.python.org/3/library/functions.html#print
# İlgili satırlar: 21, 23, 25, 58, 73, 93, 94, 95, 96, 98, 104
#
# return
# https://docs.python.org/3/reference/simple_stmts.html#the-return-statement
# İlgili satırlar: 55, 57, 70, 85
#
# Formatted string literals (f-string)
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# İlgili satırlar: 93, 94, 95, 96

"""
   (\_/)
   (•.•)   __)
   /|     /
   /> <\\
"""