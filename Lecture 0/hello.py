# ==================================================
# 1. DOSYA: hello.py
# CS50 Python Türkçe öğretici not dosyası
# Bu dosyada kullanıcıdan veri alma, ekrana yazdırma,
# string metotları, fonksiyonlar ve scope mantığını göreceğiz.
# ==================================================

# ------------------------------------------------------------------
# 1) KULLANICIDAN VERİ ALMA
# ------------------------------------------------------------------
# input() fonksiyonu kullanıcıdan klavyeyle bir değer almamızı sağlar.
# Kullanıcı Enter'a bastığında girilen değer metin (string) olarak döner.
name = input("What's your name?: ")

# Çok satırlı string örneği:
# Bu yapı yorum gibi görünse de teknik olarak bir string ifadesidir.
# Bir değişkene atanmadığı için program akışında kullanılmaz.
"""
Bu bir açıklama bloğudur.
Python bunu çalıştırır ama bir değişkene atanmadığı için
programın akışında kullanılmaz.
"""

print("-" * 50)

# ------------------------------------------------------------------
# 2) print() KULLANIMI VE FARKLI YAZDIRMA YÖNTEMLERİ
# ------------------------------------------------------------------
# print() fonksiyonu ekrana çıktı vermek için kullanılır.
# Aynı bilgiyi farklı yollarla yazdırabiliriz.

# Virgülle ayrı argüman gönderme:
# print() birden fazla değeri yan yana yazdırabilir.
# Varsayılan olarak araya bir boşluk bırakır.
print("hello,", name)

# String birleştirme:
# + operatörü ile iki metni birleştirebiliriz.
# Burada dikkat edilmesi gereken nokta, boşluğu bizim eklememiz gerektiğidir.
print("hello, " + name)

# Alt alta iki farklı print() kullanımı:
print("hello,")
print(name)

# f-string kullanımı:
# Başına f getirilen metinlerde süslü parantez içindeki değişkenler
# doğrudan metnin içine yerleştirilir.
print(f"Hello, {name}")

print("-" * 50)

# ------------------------------------------------------------------
# 3) print() FONKSİYONUNUN TEMEL MANTIĞI
# ------------------------------------------------------------------
# print() fonksiyonunun temel yapısı şöyledir:
# print(*objects, sep=' ', end='\n', file=None, flush=False)
#
# objects : Yazdırılacak değerler
# sep     : Değerlerin arasına konulacak ayırıcı
# end     : Yazının sonunda ne olacağını belirler
# \n      : Yeni satır anlamına gelir

# end="" kullanılırsa print() satır sonunda alt satıra geçmez.
print("hello,", end="")
print(name)

# sep parametresi, birden fazla değer arasındaki ayırıcıyı belirler.
print("hello,", name, sep="")

print("-" * 50)

# ------------------------------------------------------------------
# 4) TIRNAK İŞARETLERİ VE KAÇIŞ KARAKTERİ
# ------------------------------------------------------------------
# Aynı tırnak türünü metnin içinde kullanmak istersek sorun yaşayabiliriz.
# Bu durumda ya farklı tırnak kullanırız ya da kaçış karakterinden yararlanırız.

# Aşağıdaki kullanım hatalı olurdu:
# print("Hello, \"Friends\"")

# Çözüm 1: Dışta tek tırnak, içte çift tırnak kullanmak
print('Hello, "friends"')

# Çözüm 2: Kaçış karakteri (\) kullanmak
print("Hello, \"friends\"")

print("-" * 50)

# ------------------------------------------------------------------
# 5) STRING METOTLARI: strip(), capitalize(), title()
# ------------------------------------------------------------------
# String metotları metinler üzerinde işlem yapmamızı sağlar.
# Buradaki önemli nokta şudur:
# String metotları çoğu zaman mevcut metni yerinde değiştirmez,
# bize işlenmiş yeni bir değer döndürür.

# strip() baştaki ve sondaki gereksiz boşlukları temizler.
name = name.strip()
print(name)

# capitalize() yalnızca ilk harfi büyütür.
# Geri kalan harfleri küçük yapabilir.
name = name.capitalize()
print(name)

# title() her kelimenin ilk harfini büyütür.
name = name.title()
print(name)

print("-" * 50)

# ------------------------------------------------------------------
# 6) METOT ZİNCİRLEME (METHOD CHAINING)
# ------------------------------------------------------------------
# Bir metotun döndürdüğü sonucu hemen başka bir metotla işleyebiliriz.
# Buna zincirleme kullanım denir.
name = name.strip().title()
print(name)

# Aynı işlemi kullanıcıdan yeni veri alırken de tek satırda yapabiliriz.
name = input("What's your name?: ").strip().title()
print(name)

print("-" * 50)

# ------------------------------------------------------------------
# 7) split() İLE VERİYİ PARÇALAMA
# ------------------------------------------------------------------
# split(" ") metni boşluk karakterine göre parçalara ayırır.
# Eğer kullanıcı ad ve soyad girdiyse, iki parçaya bölünebilir.
first, last = name.split(" ")

# first değişkeni ilk parçayı, last değişkeni ikinci parçayı tutar.
# Burada ikisini de ayırdık ama ekrana tüm ismi yazdırmaya devam ediyoruz.
print(f"Hello, {name}")

# İstersek yalnızca adı da yazdırabiliriz.
print(f"Your first name is: {first}")
print(f"Your last name is: {last}")

print("-" * 50)

# ------------------------------------------------------------------
# 8) KENDİ FONKSİYONUMUZU YAZMA
# ------------------------------------------------------------------
# Fonksiyonlar tekrar eden işleri düzenli hale getirmemizi sağlar.
# def anahtar kelimesi ile fonksiyon tanımlarız.
#
# def hello(to="World"):
# - hello -> fonksiyonun adıdır.
# - parantez () -> fonksiyona dışarıdan veri alabileceğimiz yerdir.
# - to -> fonksiyonun parametresidir.
#         Yani dışarıdan gelen değer bu isimle tutulur.
# - "World" -> varsayılan değerdir.
#              Eğer kullanıcı bir değer göndermezse to değişkeni "World" olur.

# !!! ÖNEMLİ
# main() yapısı burada çok önemlidir.
# Normalde Python'da bir fonksiyonu kullanmadan önce onu tanımlamış olmamız gerekir.
# Yani hello() fonksiyonunu dosyanın üst kısmında çağıracaksak,
# Python hello() tanımını daha önce görmüş olmalıdır.
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
    # Kullanıcıdan isim alıyoruz.
    # strip() ve title() ile veriyi daha temiz ve düzenli hale getiriyoruz.
    person_name = input("What's your name?: ").strip().title()

    # Kullanıcıdan gelen ismi hello() fonksiyonuna gönderiyoruz.
    hello(person_name)

    # Bu çağrıda argüman göndermiyoruz.
    # Bu yüzden hello() fonksiyonu varsayılan değer olan "World" ile çalışır.
    hello()


def hello(to="World"):
    print(f"Hello, {to}")


main()

print("-" * 50)

# ------------------------------------------------------------------
# 9) SCOPE (DEĞİŞKENLERİN ETKİ ALANI)
# ------------------------------------------------------------------
# Scope, bir değişkenin nerede var olduğunu ve nerede kullanılabildiğini anlatır.
# Bir fonksiyon içinde tanımlanan değişken genellikle sadece o fonksiyon içinde yaşar.
# Bunu daha net görmek için ayrı bir örnek yapıyoruz.
def main_scope():
    name = input("Scope örneği için adını yaz: ")
    hello_scope(name)


def hello_scope(person_name="World"):
    print(f"Hello, {person_name}")


main_scope()

print("-" * 50)

# ------------------------------------------------------------------
# 10) KAYNAKÇA
# ------------------------------------------------------------------
# Ana kaynak:
# CS50 Python Notes 0
# https://cs50.harvard.edu/python/notes/0/
# Kullanım alanı: Bu dosyanın genel konusu ve örnek akışı
# İlgili satırlar: 1-157
#
# Python dokümantasyon kaynakları:
# input()
# https://docs.python.org/3/library/functions.html#input
# İlgili satırlar: 11, 117, 167
#
# print()
# https://docs.python.org/3/library/functions.html#print
# İlgili satırlar: 24, 33, 38, 39, 44, 61, 62, 65, 82, 86, 100, 101, 102, 112, 119, 135, 144
#
# str.strip()
# https://docs.python.org/3/library/stdtypes.html#str.strip
# İlgili satırlar: 88, 104, 117
#
# str.capitalize()
# https://docs.python.org/3/library/stdtypes.html#str.capitalize
# İlgili satırlar: 93
#
# str.title()
# https://docs.python.org/3/library/stdtypes.html#str.title
# İlgili satırlar: 97, 104, 117
#
# str.split()
# https://docs.python.org/3/library/stdtypes.html#str.split
# İlgili satırlar: 113
#
# Formatted string literals (f-string)
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# İlgili satırlar: 44, 123, 144

"""
   (\_/)
   (•.•)   __)
   /|     /
   /> <\\
"""