# x = int(input("X değerini giriniz: "))

# if x % 2 == 0:
#     print("X sayısı çifttir")
# else:
#     print("X sayısı tektir")

print("-"*50)

def main():
    x = int(input("X değerini giriniz: "))
    if ciftek(x):
        print("Çifttir")
    else:
        print("Tektir")


def ciftek(n):
    if n % 2 == 0:
        return True
    else:
        return False


# def ciftek(n):
#     return n % 2 == 0

main()