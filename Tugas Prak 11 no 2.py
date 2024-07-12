class Person:
    person = 'Person'

    def __init__(self, rambut, warna):
        self.rambut = rambut
        self.warna = warna

Budi = Person("Ikal", "Hitam")
Michael = Person("Lurus", "Pirang")

print('Budi details:')
print('Rambut:', Budi.rambut)
print('Warna:', Budi.warna)

print('\nMichael details:')
print('Rambut:', Michael.rambut)
print('Warna:', Michael.warna)
