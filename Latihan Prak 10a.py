def printme(str):
    "This prints a passed string into this function"
    print(str)
    return
printme("hello world")

def jumlah(angka):
    total = 0
    for x in angka:
        total += x
    return total

print("Jumlah :", jumlah((8,3,1,4,5)))

def cek_ganjil_genap(angka):
    if angka%2==0:
        print("genap")
    else:
        print("ganjil")
    return

cek_ganjil_genap(5)

def rata_rata(a,b,c):
    return (a+b+c)/3
rata_rata(1,2,3)

def kalkulator(angka1,angka2):
    print(angka1+angka2)
    print(angka1-angka2)
    print(angka1*angka2)
    print(angka1/angka2)

kalkulator(1,2)
