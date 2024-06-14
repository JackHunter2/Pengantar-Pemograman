def hitung_karakter(s):
    jumlah_huruf = 0
    jumlah_angka = 0
    for char in s:
        if char.isalpha():
            jumlah_huruf += 1
        elif char.isdigit():
            jumlah_angka += 1
    return jumlah_huruf, jumlah_angka

string_input = input("Inputan : ")
jumlah_huruf, jumlah_angka = hitung_karakter(string_input)

print(f"kata : {jumlah_huruf}")
print(f"angka : {jumlah_angka}")
