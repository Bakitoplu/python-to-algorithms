# ==================================================
# 9. DOSYA: mario.py
# CS50 Python Türkçe öğretici not dosyası
# Bu dosyada sütun, satır ve kare yazdırma mantığı,
# iç içe döngüler ve fonksiyonlarla soyutlama işlenmektedir.
# ==================================================

# ------------------------------------------------------------------
# 1) EN İLK YAKLAŞIM: AYNI KARAKTERİ TEK TEK YAZDIRMA
# ------------------------------------------------------------------
# Burada aynı çıktıyı tekrar tekrar manuel yazıyoruz.
# Kod çalışır, ama tekrar eden işler için iyi bir yöntem değildir.
print("#")
print("#")
print("#")

print("-" * 50)

# ------------------------------------------------------------------
# 2) for DÖNGÜSÜ İLE SÜTUN YAZDIRMA
# ------------------------------------------------------------------
# Tekrar eden yapıyı for döngüsü ile daha kısa şekilde yazabiliriz.
for _ in range(3):
    print("#")

print("-" * 50)

# ------------------------------------------------------------------
# 3) FONKSİYONLA SÜTUN YAZDIRMA
# ------------------------------------------------------------------
# def print_column(height):
# - print_column -> fonksiyonun adıdır.
# - height -> kaç satır # yazdırılacağını belirleyen parametredir.
#
# Böylece sütunun yüksekliğini istediğimiz zaman değiştirebiliriz.
def print_column(height):
    for _ in range(height):
        print("#")


print_column(3)

print("-" * 50)

# ------------------------------------------------------------------
# 4) DAHA KISA SÜTUN YAZDIRMA YÖNTEMİ
# ------------------------------------------------------------------
# Bu yöntem de çalışır.
# Burada her satıra tek tek # yazdırmak yerine,
# metni çarpma işlemiyle yan yana çoğaltıyoruz.
def print_column_short(height):
    print("#\n" * height, end="")


print_column_short(3)

print("-" * 50)

# ------------------------------------------------------------------
# 5) SATIR YAZDIRMA
# ------------------------------------------------------------------
# Bu kez alta alta değil, yan yana karakter üretmek istiyoruz.
# "#" * width ifadesi karakteri width kadar tekrarlar.
def print_row(width):
    print("#" * width)


print_row(4)

print("-" * 50)

# ------------------------------------------------------------------
# 6) İÇ İÇE DÖNGÜ İLE KARE YAZDIRMA
# ------------------------------------------------------------------
# Burada kare üretmek için iki döngü kullanıyoruz.
# Dış döngü satırları kontrol eder.
# İç döngü ise her satırdaki karakter sayısını kontrol eder.
def print_square_nested(size):
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()


print_square_nested(3)

print("-" * 50)

# ------------------------------------------------------------------
# 7) DAHA TEMİZ YAKLAŞIM: SATIR FONKSİYONU İLE KARE OLUŞTURMA
# ------------------------------------------------------------------
# !!! ÖNEMLİ
# Bu yapı önemlidir çünkü tekrar eden mantığı parçalara ayırıyoruz.
# Kare yazdırırken her satır için yeniden aynı işi yapan ayrı bir satır
# yazdırma fonksiyonunu kullanıyoruz.
#
# Bu yaklaşımın avantajı şudur:
# Daha büyük problemleri küçük parçalara bölerek çözmemizi sağlar.
# Yani bir kareyi tek seferde düşünmek yerine,
# önce "bir satır nasıl yazdırılır?" sorusunu çözüyoruz.
def print_square(size):
    for _ in range(size):
        print_row(size)


print_square(3)

print("-" * 50)

# ------------------------------------------------------------------
# 8) FONKSİYONLARLA AKIŞI TOPARLAMA
# ------------------------------------------------------------------
def main():
    print_square(3)


main()

print("-" * 50)

# ------------------------------------------------------------------
# 9) KAYNAKÇA
# ------------------------------------------------------------------
# Ana kaynak:
# CS50 Python Notes 2
# https://cs50.harvard.edu/python/notes/2/
# Kullanım alanı: Mario, columns, rows, squares, nested loops
# İlgili satırlar: 1-102
#
# Python dokümantasyon kaynakları:
# print()
# https://docs.python.org/3/library/functions.html#print
# İlgili satırlar: 12, 13, 14, 24, 37, 50, 62, 64, 82, 89, 102
#
# range()
# https://docs.python.org/3/library/functions.html#func-range
# İlgili satırlar: 23, 35, 61, 62, 81
#
# Common sequence operations (*)
# https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
# İlgili satırlar: 36, 49
#
# for
# https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
# İlgili satırlar: 23, 35, 61, 62, 81

"""
   (\_/)
   (•.•)   __)
   /|     /
   /> <\\
"""