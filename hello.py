# Kullanıcıya ismini sor
name = input("What's your name?: ")
# Kullanıcıya merhaba de
"""
    is a comment
"""
print("hello,",name)
print("hello,"+name)
print("hello,")
print(name)

# print(*objects, sep=' ', end='\n', file=None, flush=False) bu print fonksiyonunun dökümanda ki tanımı

# print(fonksiyon adı) "()" (aldığı argümanları içinde bulundurur) "*objects" (harhangi bir sayıda nesne alabilir) "sep" (seperator demek yani ayırıcı bir sonra ki argüman ile bu argümanı ne ile ayıracağını belirtir) "end" (fonksiyonun ne ile biteceğini belirtir) "\n" (yeni satır)

# Burada print bitişinde artık alt satıra geçmeyecek

print("hello,",end="")
print(name)

# Burada iki argüman arasında artık boşluk olmayacak

print("hello,",sep="")
print(name)