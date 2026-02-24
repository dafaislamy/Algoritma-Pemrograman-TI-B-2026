class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.__nilai = 0

    def get_nilai(self):
        return self.__nilai

    def set_nilai(self, nilai):
        if  nilai > 0 and nilai < 100:
            self.__nilai = nilai
        else:
            print('Nilai tidak valid')

mhs = Mahasiswa('Dafa')

mhs.set_nilai(96)
print(f"Nilai {mhs.nama}: {mhs.get_nilai()}")

mhs.set_nilai(106)