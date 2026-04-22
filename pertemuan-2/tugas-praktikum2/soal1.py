'''
Soal 1 (Function dan Validasi Data)

Buat sebuah fungsi bernama rata rata(nilai) yang:
1. Menerima sebuah list berisi nilai mahasiswa
2. Menghitung rata-rata nilai
3. Jika list kosong, kembalikan pesan: "Data kosong"
Kemudian:
1. Panggil fungsi dengan list: [80, 75, 90, 60, 85]
2. Tampilkan hasilnya
'''

def RataRata(nilai): #deklarasi fungsi bernama RataRata dengan parameter nilai
    if not nilai:
        return 'Data kosong' #jika data nilai kosong, akan mengembalikan pesan 'Data kosong'
    
    total = sum(nilai) #menghitung total data
    rata_rata = total / len(nilai) #menghitung rata-rata data
    return rata_rata #mengembalikan hasil rata-rata

data_nilai = [80, 75, 90, 60, 85] #menyiapkan data nilai mahasiswa
hasil = RataRata(data_nilai) #memanggil fungsi untuk menghitung rata-rata
print('Rata-rata dari data nilai mahasiswa adalah =', hasil) #menampilkan hasil perhitungan rata-rata