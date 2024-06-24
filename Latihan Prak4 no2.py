# program 1: perhitungan sederhana
BilanganPertama = 15
BilanganKedua = 8
BilanganKetiga = 100
RumusPengjumlahan = BilanganPertama + BilanganKedua + BilanganKetiga
RumusPengurangan = BilanganPertama - BilanganKedua - BilanganKetiga
RumusPerkalian = BilanganPertama * BilanganKedua * BilanganKetiga
print("Pengjumlahan = ", BilanganPertama, "+", BilanganKedua, "+", BilanganKetiga, "=", RumusPengjumlahan)
print("Pengurangan = ", BilanganPertama, "-", BilanganKedua, "-", BilanganKetiga, "=", RumusPengurangan)
print("Perkalian = ", BilanganPertama, "x", BilanganKedua, "x", BilanganKetiga, "=", RumusPerkalian)

# program 2: menghitung luas bangun datar
# 1. Luas Persegi
panjang_sisi = 20
luas_persegi = panjang_sisi * panjang_sisi
print("Luas persegi : ", panjang_sisi, "x", panjang_sisi, "=", luas_persegi)

# 2. Luas Persegi Panjang
panjang_pp = 50
lebar_pp = 25.5
luas_pp = panjang_pp * lebar_pp
print("Luas persegi panjang : ", panjang_pp, "x", lebar_pp, "=", luas_pp)

# 3. Luas Segitiga
alas_segitiga = 40
tinggi_segitiga = 60
luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
print("Luas segitiga : 0.5", "x", alas_segitiga, "x", tinggi_segitiga, "=", luas_segitiga)

# Luas lingkaran
jari_jari = 10
luas_lingkaran = 3.14 * jari_jari * jari_jari
print("Luas lingkaran : 3.14", "x", jari_jari, "x", jari_jari, "=", luas_lingkaran)

# Luas jajar genjang
alas_jajargenjang = 12
tinggi_jajargenjang = 25
luas_jajargenjang = alas_jajargenjang * tinggi_jajargenjang
print("Luas jajar genjang : ", alas_jajargenjang, "x", tinggi_jajargenjang, "=", luas_jajargenjang)

# Luas trapesium
sisi_sejajar = 15
tinggi_trapesium = 25
luas_trapesium = 0.5 * (sisi_sejajar + sisi_sejajar) * tinggi_trapesium
print("Luas trapesium : 0.5", "x(", sisi_sejajar, "+", sisi_sejajar, ")x", tinggi_trapesium, "=", luas_trapesium)
