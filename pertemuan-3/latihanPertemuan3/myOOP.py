#INHERITANCE

class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga
    
    def info_produk(self):
        return f"{self.nama_produk} seharga {self.harga:,})"

class ProdukElektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi

    def info_produk(self):
        return f"{self.nama_produk} seharga {self.harga} dengan garansi {self.garansi} tahun"

class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        super().__init__(nama_produk, harga)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def info_produk(self):
        return f"{self.nama_produk} seharga {self.harga} kadaluarsa {self.tanggal_kadaluarsa}"

elektronik = ProdukElektronik('TV', 3000000, 2)
makanan = ProdukMakanan('Roti', 15000, '12-12-2026')

print(elektronik.info_produk())
print(makanan.info_produk())


#POLYMORPHISM

class Notifikasi:
    def kirim(self):
        return "Mengirim notifikasi"
    
class Email(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui Email"
    
class SMS(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui SMS"

daftar_notifikasi = [Email(), SMS()]

for notif in daftar_notifikasi:
    print(notif.kirim())


#ENCAPSULATION

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