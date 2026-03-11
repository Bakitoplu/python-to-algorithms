# ==================================================
# 6. DOSYA: house.py
# CS50 Python Türkçe öğretici not dosyası
# Bu dosyada if / elif, or kullanımı, match / case yapısı
# ve birden fazla değeri tek durumda kontrol etme mantığı işlenmektedir.
# ==================================================

# ------------------------------------------------------------------
# 1) KULLANICIDAN İSİM ALMA
# ------------------------------------------------------------------
# input() kullanıcıdan veri alır.
# Burada kullanıcıdan bir karakter ismi istiyoruz.
name = input("Adın ne? ").strip().title()

print("-" * 50)

# ------------------------------------------------------------------
# 2) İLK YAKLAŞIM: HER İSİM İÇİN AYRI if / elif YAZMA
# ------------------------------------------------------------------
# Bu yaklaşım çalışır.
# Her isim için tek tek kontrol yapıyoruz.
#
# Bu yöntem yanlış değildir.
# Ama aynı sonucu üreten isimleri tekrar tekrar yazdığımız için
# biraz uzun ve dağınık bir yapı oluşturur.
if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Kim?")

print("-" * 50)

# ------------------------------------------------------------------
# 3) DAHA KISA YAKLAŞIM: or KULLANIMI
# ------------------------------------------------------------------
# Burada aynı eve ait olan isimleri tek bir koşul içinde birleştiriyoruz.
#
# name == "Harry" or name == "Hermione" or name == "Ron"
# ifadesi şu anlama gelir:
# Kullanıcının girdiği isim bu üç isimden herhangi biri mi?
#
# Bu sürüm, bir öncekiyle aynı işi yapar.
# Ama tekrar sayısını azalttığı için daha kısa bir yazımdır.
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Kim?")

print("-" * 50)

# ------------------------------------------------------------------
# 4) match / case KULLANIMI
# ------------------------------------------------------------------
# match yapısı, bir değeri birden fazla olasılıkla karşılaştırmak için kullanılır.
# Özellikle aynı değişken üzerinde birçok olasılık kontrol ediyorsak,
# bazı durumlarda if / elif zincirine göre daha düzenli görünebilir.
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    # !!! ÖNEMLİ
    # case _ ifadesindeki _ karakteri burada varsayılan durum anlamına gelir.
    # Yani yukarıdaki hiçbir case eşleşmezse program bu bölüme gelir.
    # Bunu if / else yapısındaki else gibi düşünebilirsin.
    case _:
        print("Kim?")

print("-" * 50)

# ------------------------------------------------------------------
# 5) match / case İÇİNDE | KULLANIMI
# ------------------------------------------------------------------
# Bu son sürüm en kısa ve en temiz yaklaşımlardan biridir.
#
# Buradaki | işareti match / case yapısında "veya" anlamında kullanılır.
# Yani aşağıdaki satır şunu söyler:
# İsim Harry, Hermione veya Ron ise Gryffindor yazdır.
#
# !!! ÖNEMLİ
# Buradaki | işareti, bu kullanım özelinde or ile benzer mantık taşır.
# Ama doğrudan match / case yapısının içinde kullanılır.
# Normal if koşulunda bunu böyle yazamayız.
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Kim?")

print("-" * 50)

# ------------------------------------------------------------------
# 6) KAYNAKÇA
# ------------------------------------------------------------------
# Ana kaynak:
# CS50 Python Notes 1
# https://cs50.harvard.edu/python/notes/1/
# Kullanım alanı: if / elif, or, match, case, wildcard pattern örneği
# İlgili satırlar: 1-102
#
# Python dokümantasyon kaynakları:
# input()
# https://docs.python.org/3/library/functions.html#input
# İlgili satırlar: 11
#
# str.strip()
# https://docs.python.org/3/library/stdtypes.html#str.strip
# İlgili satırlar: 11
#
# str.title()
# https://docs.python.org/3/library/stdtypes.html#str.title
# İlgili satırlar: 11
#
# print()
# https://docs.python.org/3/library/functions.html#print
# İlgili satırlar: 24, 36, 55, 65, 88, 98, 102
#
# match
# https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
# İlgili satırlar: 47, 80

"""
   (\_/)
   (•.•)   __)
   /|     /
   /> <\\
"""