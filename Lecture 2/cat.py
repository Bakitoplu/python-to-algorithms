# ==================================================
# 7. DOSYA: cat.py
# CS50 Python Türkçe öğretici not dosyası
# Bu dosyada tekrar eden işlemleri döngülerle yapma, while ve for kullanımı,
# kullanıcıdan güvenli veri alma ve fonksiyonlarla akışı düzenleme işlenmektedir.
# ==================================================

# ------------------------------------------------------------------
# 1) EN İLK YAKLAŞIM: AYNI KODU TEK TEK YAZMA
# ------------------------------------------------------------------
# Burada aynı satırı üç kez manuel yazıyoruz.
# Kod çalışır, ama tekrar eden işler için iyi bir yöntem değildir.
print("Miyav")
print("Miyav")
print("Miyav")

print("-" * 50)

# ------------------------------------------------------------------
# 2) while DÖNGÜSÜ İLE GERİYE DOĞRU SAYMA
# ------------------------------------------------------------------
# i değişkeni 3'ten başlar.
# Her turda bir azaltılır ve 0 olana kadar döngü devam eder.
i = 3
while i != 0:
    print("Miyav")
    i = i - 1

print("-" * 50)

# ------------------------------------------------------------------
# 3) while DÖNGÜSÜ İLE İLERİYE DOĞRU SAYMA
# ------------------------------------------------------------------
# Bu kez 1'den başlayıp 3'e kadar gidiyoruz.
# Mantık yine aynı: koşul sağlandığı sürece döngü çalışır.
i = 1
while i <= 3:
    print("Miyav")
    i = i + 1

print("-" * 50)

# ------------------------------------------------------------------
# 4) PYTHON'DA DAHA YAYGIN YAKLAŞIM: 0'DAN BAŞLAMAK
# ------------------------------------------------------------------
# Programlamada saymaya çoğu zaman 0'dan başlarız.
# i += 1 ifadesi, i = i + 1 ile aynı işi yapar.
i = 0
while i < 3:
    print("Miyav")
    i += 1

print("-" * 50)

# ------------------------------------------------------------------
# 5) for DÖNGÜSÜ: LİSTE ÜZERİNDE DOLAŞMA
# ------------------------------------------------------------------
# Bu sürüm de çalışır.
# Burada döngü [0, 1, 2] listesindeki her değer için bir kez çalışır.
for i in [0, 1, 2]:
    print("Miyav")

print("-" * 50)

# ------------------------------------------------------------------
# 6) for DÖNGÜSÜ: range() KULLANIMI
# ------------------------------------------------------------------
# range(3) bize 0, 1 ve 2 değerlerini üretir.
# Bu yüzden listeyi tek tek yazmak zorunda kalmayız.
for i in range(3):
    print("Miyav")

print("-" * 50)

# ------------------------------------------------------------------
# 7) _ KULLANIMI
# ------------------------------------------------------------------
# !!! ÖNEMLİ
# Daha sonra kullanılmayacak olan ve adının önemli olmadığı değişkenler için
# Python'da gelenek olarak _ kullanılır.
# Burada döngü sayısını önemsiyoruz ama i değerinin kendisini kullanmıyoruz.
for _ in range(3):
    print("Miyav")

print("-" * 50)

# ------------------------------------------------------------------
# 8) TEK SATIRDA ÇOKLU ÇIKTI ÜRETME
# ------------------------------------------------------------------
# "Miyav\n" * 3 ifadesi metni 3 kez üretir.
# end="" kullanmamızın sebebi, print() fonksiyonunun fazladan bir boş satır
# eklememesini sağlamaktır.
print("Miyav\n" * 3, end="")

print("-" * 50)

# ------------------------------------------------------------------
# 9) KULLANICIDAN VERİ ALIRKEN İLK / DAHA ZAYIF YAKLAŞIM
# ------------------------------------------------------------------
# Bu yapı çalışabilir, ama iyi bir yöntem değildir.
# Çünkü kullanıcı tekrar yanlış girerse aynı satırları tekrar tekrar yazmamız gerekir.
# Yani sorun çözülebilir olsa da ölçeklenebilir ve temiz bir yöntem değildir.
n = int(input("N değerini giriniz: "))
if n < 0:
    n = int(input("N değerini giriniz: "))
    if n < 0:
        n = int(input("N değerini giriniz: "))

print(f"İlk yaklaşım sonunda elde edilen değer: {n}")

print("-" * 50)

# ------------------------------------------------------------------
# 10) DAHA GÜÇLÜ YAKLAŞIM: while True, continue ve break
# ------------------------------------------------------------------
# continue komutu döngünün bir sonraki turuna geçer.
# break komutu ise döngüyü tamamen sonlandırır.
#
# Burada amaç şudur:
# Kullanıcı negatif sayı girdikçe tekrar sor.
# Pozitif bir sayı girince döngüden çık.
while True:
    n = int(input("N değerini giriniz: "))
    if n < 0:
        continue
    else:
        break

for _ in range(n):
    print("Miyav")

print("-" * 50)

# ------------------------------------------------------------------
# 11) DAHA TEMİZ YAKLAŞIM: continue KULLANMADAN break
# ------------------------------------------------------------------
# Bu sürüm, bir öncekiyle aynı işi daha temiz yapar.
# Çünkü burada negatif durumda ayrıca continue yazmak zorunda değiliz.
# Sadece doğru durumda döngüyü kırmamız yeterlidir.
while True:
    n = int(input("N değerini giriniz: "))
    if n > 0:
        break

for _ in range(n):
    print("Miyav")

print("-" * 50)

# ------------------------------------------------------------------
# 12) FONKSİYONLARLA DAHA DÜZENLİ YAPI KURMA
# ------------------------------------------------------------------
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("N sayısını giriniz: "))
        if n > 0:
            # Burada normalde break de kullanılabilir.
            # Ama return kullandığımız için hem döngüden çıkıyoruz
            # hem de değeri doğrudan main() fonksiyonuna gönderiyoruz.
            return n


def meow(n):
    for _ in range(n):
        print("Miyav")


main()

print("-" * 50)

# ------------------------------------------------------------------
# 13) KAYNAKÇA
# ------------------------------------------------------------------
# Ana kaynak:
# CS50 Python Notes 2
# https://cs50.harvard.edu/python/notes/2/
# Kullanım alanı: Loops, while, for, continue, break, meow örneği
# İlgili satırlar: 1-224
#
# Python dokümantasyon kaynakları:
# print()
# https://docs.python.org/3/library/functions.html#print
# İlgili satırlar: 13, 14, 15, 17, 26, 29, 38, 41, 50, 53, 61, 63, 71, 73, 83, 85, 93, 95, 109, 111, 130, 132, 146, 148, 170, 175
#
# input()
# https://docs.python.org/3/library/functions.html#input
# İlgili satırlar: 103, 105, 107, 123, 141, 160
#
# int()
# https://docs.python.org/3/library/functions.html#int
# İlgili satırlar: 103, 105, 107, 123, 141, 160
#
# range()
# https://docs.python.org/3/library/functions.html#func-range
# İlgili satırlar: 70, 82, 129, 145, 169
#
# return
# https://docs.python.org/3/reference/simple_stmts.html#the-return-statement
# İlgili satırlar: 165
#
# Formatted string literals (f-string)
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# İlgili satırlar: 109
#
# while
# https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
# İlgili satırlar: 25, 37, 49, 122, 140, 159
#
# for
# https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
# İlgili satırlar: 60, 70, 82, 129, 145, 169

"""
   (\_/)
   (•.•)   __)
   /|     /
   /> <\\
"""