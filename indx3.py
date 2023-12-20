class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

# Contoh penggunaan:
kucing = Animal("Kucing", "Daging", "Darat", "Vivipar")
gajah = Animal("Gajah", "Tumbuhan", "Darat", "Ovipar")

# Mengakses properti
print("Kucing makan", kucing.makanan)
print("Gajah hidup di", gajah.hidup)