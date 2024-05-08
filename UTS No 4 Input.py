Bil1 = float(input("Masukkan nilai pertama : "))
Bil2 = float(input("Masukkan nilai kedua : "))
Bil3 = float(input("Masukkan nilai ketiga : "))

Nilai = [Bil1, Bil2, Bil3]
Nilai.sort()

if len(Nilai) == 3:
    median = Nilai[1]
else:
    print("Jumlah bilangan harus tepat 3!")
    exit()

print("Median : ", median)
