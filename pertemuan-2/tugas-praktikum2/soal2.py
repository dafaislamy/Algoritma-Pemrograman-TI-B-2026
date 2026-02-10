'''
Soal 2 (Range dan Pola Bilangan)

Buat sebuah fungsi bernama bilangan prima(n) yang:
1. Menggunakan range()
2. Mengembalikan list bilangan prima dari 1 sampai n
Kemudian:
1. Panggil fungsi untuk n = 50
2. Tampilkan hasilnya
'''

def bilangan_prima(n): #deklarasi fungsi bernama bilangan_prima dengan parameter n
    daftar_prima = [] #deklari list kosong dengan nama daftar_prima untuk menyimpan data bilangan prima nantinya
    
    for num in range(2, n + 1): #menggunakan perulangan for dan range(2, n + 1), mulai dari 2 karena 1 tidak termasuk bilangan prima dan berakhir dengan n + 1 agar n termasuk dalam range
        bilPrima = True #asumsi awal seluruh angak yang akan dicek adalah prima dengan menggunakan nilai True
        for i in range(2, int(num**0.5) + 1): #perulangan for didalam for (nested loop) dan range(2, int(num**0.5) + 1), num**0.5 adalah perhitungan akar kuadrat, int berguna agar hasil hasil selalu bilangan bulat
            if num % i == 0: #jika num modulus i = 0,
                bilPrima = False #maka terdapat pembagi lain dari bilangan tersebut selain dirinya sendiri sehingga tidak memenuhi syarat untuk menjadi bilangan prima
                break #break, kode berhenti sehingga hasil akhir tidak digunakan
        if bilPrima: #jika bilPrima tetap bernilai True hingga tahap ini, maka bilangan tersebut memenuhi syarat untuk menjadi bilangan prima
            daftar_prima.append(num) #sehingga bilangan tersebut akan dimasukkan kedalam daftar_prima dengan append sebagai rumus bawaan list
            
    return daftar_prima #fungsi akan mengembalikan daftar_prima

# 1. Memanggil fungsi untuk n = 50
hasil = bilangan_prima(50)

# 2. Menampilkan hasilnya
print(f"Bilangan prima dari 1 sampai 50 adalah:")
print(hasil)