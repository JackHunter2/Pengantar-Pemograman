Bil1 = 23
Bil2 = 12
Bil3 = 15

print("Nilai pertama : ", Bil1)
print("Nilai kedua : ", Bil2)
print("Nilai ketiga : ", Bil3)

Nilai = [Bil1, Bil2, Bil3]
Nilai.sort()

if len(Nilai) == 3:
    median = Nilai[1]
else:
    print("Jumlah bilangan harus tepat 3!")
    exit()

print("Median : ", median)
