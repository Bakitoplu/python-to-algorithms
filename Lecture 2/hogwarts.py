# ==================================================
# 8. DOSYA: hogwarts.py
# CS50 Python Türkçe öğretici not dosyası
# Bu dosyada list, len, dict ve sözlükler içinde veri tutma mantığı
# Hogwarts örneği üzerinden işlenmektedir.
# ==================================================

# ------------------------------------------------------------------
# 1) İLK YAKLAŞIM: LİSTEDEKİ DEĞERLERİ TEK TEK YAZDIRMA
# ------------------------------------------------------------------
# students adlı listede öğrenci isimlerini tutuyoruz.
# Liste içindeki verilere köşeli parantez ve indeks numarası ile ulaşılır.
students = ["Hermione", "Harry", "Ron"]
print(students[0])
print(students[1])
print(students[2])

print("-" * 50)

# ------------------------------------------------------------------
# 2) DAHA İYİ YAKLAŞIM: for İLE LİSTE ÜZERİNDE DOLAŞMA
# ------------------------------------------------------------------
# Liste büyürse tek tek print yazmak verimsiz olur.
# Bu yüzden for döngüsü ile listedeki her öğrenciyi sırayla yazdırıyoruz.
students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)

print("-" * 50)

# ------------------------------------------------------------------
# 3) len() KULLANARAK İNDEKS VE DEĞERİ BİRLİKTE GÖSTERME
# ------------------------------------------------------------------
# len(students), listenin kaç elemanlı olduğunu verir.
# range(len(students)) sayesinde 0'dan listenin uzunluğuna kadar indeks üretiyoruz.
# i + 1 kullanmamızın sebebi, ekranda 1'den başlayan insan dostu sıra göstermek istememizdir.
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])

print("-" * 50)

# ------------------------------------------------------------------
# 4) İKİ AYRI LİSTE İLE İLİŞKİ KURMA
# ------------------------------------------------------------------
# Bu yaklaşım mantık olarak çalışır.
# Öğrenciler bir listede, evler başka bir listede tutulur.
# Aynı indeks numarasındaki verilerin birbirine ait olduğunu varsayarız.
#
# Ama bu yöntem büyüdükçe dağınık hale gelir.
# Çünkü iki listenin sırasını her zaman birebir korumamız gerekir.
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
print(students[0], houses[0], sep=", ")
print(students[1], houses[1], sep=", ")
print(students[2], houses[2], sep=", ")
print(students[3], houses[3], sep=", ")

print("-" * 50)

# ------------------------------------------------------------------
# 5) DAHA UYGUN YAPI: dict KULLANIMI
# ------------------------------------------------------------------
# !!! ÖNEMLİ
# dict yani sözlük yapısında anahtar (key) ile değer (value) eşleştiririz.
# Burada öğrencinin adı key, evi ise value olur.
# Bu yüzden iki ayrı listeyi sırayla takip etmek zorunda kalmayız.
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

print("-" * 50)

# ------------------------------------------------------------------
# 6) SÖZLÜKTE SADECE ANAHTARLAR ÜZERİNDE DOLAŞMA
# ------------------------------------------------------------------
# for student in students yazdığımızda,
# döngü sözlüğün anahtarları üzerinde dolaşır.
# Yani burada sadece öğrenci isimleri yazdırılır.
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student)

print("-" * 50)

# ------------------------------------------------------------------
# 7) ANAHTAR VE DEĞERİ BİRLİKTE YAZDIRMA
# ------------------------------------------------------------------
# Burada students[student] ifadesi ile,
# döngüde gelen öğrencinin ev bilgisini de alıyoruz.
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student])

print("-" * 50)

# ------------------------------------------------------------------
# 8) DAHA TEMİZ ÇIKTI: sep KULLANIMI
# ------------------------------------------------------------------
# sep=", " kullanarak çıktıdaki değerlerin arasına virgül ve boşluk koyuyoruz.
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=", ")

print("-" * 50)

# ------------------------------------------------------------------
# 9) DAHA ZENGİN VERİ YAPISI: LİSTE İÇİNDE SÖZLÜKLER
# ------------------------------------------------------------------
# Burada artık her öğrenci için sadece isim ve ev değil,
# patronus bilgisini de tutuyoruz.
#
# Yani students artık bir list.
# Ama listenin her elemanı ayrı bir dict yapısıdır.
#
# None, burada bir değerin bulunmadığını gösterir.
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

print("-" * 50)

# ------------------------------------------------------------------
# 10) KAYNAKÇA
# ------------------------------------------------------------------
# Ana kaynak:
# CS50 Python Notes 2
# https://cs50.harvard.edu/python/notes/2/
# Kullanım alanı: Lists, len, dictionaries, Hogwarts örneği
# İlgili satırlar: 1-140
#
# Python dokümantasyon kaynakları:
# print()
# https://docs.python.org/3/library/functions.html#print
# İlgili satırlar: 12, 13, 14, 24, 35, 48, 49, 50, 51, 67, 82, 96, 111, 126, 140
#
# len()
# https://docs.python.org/3/library/functions.html#len
# İlgili satırlar: 34
#
# range()
# https://docs.python.org/3/library/functions.html#func-range
# İlgili satırlar: 34
#
# list
# https://docs.python.org/3/tutorial/datastructures.html
# İlgili satırlar: 11, 23, 34, 47, 125
#
# dict
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# İlgili satırlar: 63, 79, 93, 108, 125
#
# None
# https://docs.python.org/3/library/constants.html#None
# İlgili satırlar: 130

"""
   (\_/)
   (•.•)   __)
   /|     /
   /> <\\
"""