def MenghitungNilai(angka):
    total = sum(angka)
    nilai = total / len(angka)
    return nilai

angka = [18, 25, 3, 41, 5]
rata_rata = MenghitungNilai(angka)
print("Nilai : ", angka)
print("Nilai rata-rata : ", rata_rata)
