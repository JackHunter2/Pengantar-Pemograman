i = list(range(1,10))
print("list angka, ",i)

ganjil = 0
genap = 0

for j in i:
    if j % 2 ==0:
        genap +=1
    else:
        ganjil +=1

print("Jumlah bilangan genap : ", genap)
print("Jumlah bilangan ganjil : ", ganjil)


