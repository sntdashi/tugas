class Lingkaran:
    def __init__(self, jari_jari):
        self.r = jari_jari
    def luas(self):
        return 3.14 * self.r * self.r
    def keliling(self):
        return 2 * 3.14 * self.r
bola = Lingkaran(7)
print("Luas Lingkaran:", bola.luas()) #memanggil method luas() pada objek bola
print("Keliling Lingkaran:", bola.keliling()) #memanggil method keliling() pada objek bola