# Kullanıcıdan isim al
name = input("What's your name?: ")

# Çok satırlı yorum örneği
"""
Bu bir açıklama bloğudur.
Python bunu çalıştırır ama bir değişkene atanmadığı için
programın akışında kullanılmaz.
"""

# İsmi ekrana yazdırmanın farklı yolları
print("hello,", name)          # Virgülle ayrı argüman gönderme
print("hello," + name)         # String birleştirme
print("hello,")
print(name)

# f-string kullanımı
# Süslü parantez içindeki değişkenler doğrudan metnin içine yerleştirilir.
print(f"Hello, {name}")

print("-" * 50)

# print() fonksiyonunun temel yapısı:
# print(*objects, sep=' ', end='\n', file=None, flush=False)
#
# objects : Yazdırılacak değerler
# sep     : Değerler arasına konulacak ayırıcı
# end     : Yazının sonunda ne olacağını belirler
# \n      : Yeni satır anlamına gelir

# end="" kullanılırsa print alt satıra geçmez.
print("hello,", end="")
print(name)

# sep parametresi birden fazla değer arasındaki ayırıcıyı belirler.
print("hello,", name, sep="")

print("-" * 50)

# Tırnak işaretlerini doğru kullanma
# Aynı tırnak türünü metin içinde kullanacaksak kaçış karakteri gerekir.
# print("Hello,"Friends"")  # Hatalı kullanım

print('Hello, "friends"')
print("Hello, \"friends\"")

print("-" * 50)

# strip() metnin başındaki ve sonundaki boşlukları temizler.
name = name.strip()
print(name)

# capitalize() metnin ilk harfini büyük harf ile değiştirir.
name = name.capitalize()
print(name)

# title() metinde ki her kelimenin ilk harfini büyük harf ile değiştirir
name = name.title()
print(name)

# string fonksiyonları zincileme da kullanabiliriz
name = name.strip().title()
name = input("What's your name?: ").strip().title()
print(name)

# split() dizeyi birden fazla dize halinde böler
first , last = name.split(" ")
print(f"Hello, {name}")

print("-" * 50)

"""
   (\_/)
   (•.•)   __)
   /|     /
   /> <\
"""