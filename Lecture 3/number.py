x = int(input("X değerini giriniz: "))
print(f"X değeri {x}'dir ")

# X değerini giriniz: cat
# ValueError: invalid literal for int() with base 10: 'cat'

try:
    x = int(input("X değerini giriniz: "))
    print(f"X değeri {x}'dir ")
except ValueError:
    print("X bir tamsayı değil")

# X değerini giriniz: cat
# X bir tamsayı değil

try:
    x = int(input("X değerini giriniz: "))
except ValueError:
    print("X bir tamsayı değil")

print(f"X değeri {x}'dir ")

# NameError: name 'cat' is not defined bu hatanın sebebi dönüştürme işlemi başarısız olduğu için değer ataması yapılamıyor çünkü satırın sağında ki hata tüm satırın çalışmasını iptal ediyor

try:
    x = int(input("X değerini giriniz: "))
except ValueError:
    print("X bir tamsayı değil")
else:
    print(f"X değeri {x}'dir ")


