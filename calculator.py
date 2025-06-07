def toplama(a, b):
    return a + b

def ayyrma(a, b):
    return a - b

def kopeltme(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "0-a bölmek mümkin däl!"
    return a / b

print("Hasaplaýjy")
print("1.Toplama\n2.Ayyrma\n3.Köpeltme\n4.Bölme")

secim = input("Amaly saýla (1/2/3/4): ")
a = float(input("1-nji sany giriz: "))
b = float(input("2-nji sany giriz: "))

if secim == '1':
    print("Netije:", toplama(a, b))
elif secim == '2':
    print("Netije:", ayyrma(a, b))
elif secim == '3':
    print("Netije:", kopeltme(a, b))
elif secim == '4':
    print("Netije:", bolme(a, b))
else:
    print("Nädogry saýlaw!")
