def MenghitungNilai():
    angka = input("Nilai : ")
    angka = [float(i) for i in angka.split()]
    total = sum(angka)
    Nilai = total / len(angka)
    return Nilai

rata_rata = MenghitungNilai()
print("Nilai rata-rata : ", rata_rata)
