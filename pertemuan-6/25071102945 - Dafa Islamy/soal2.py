# Soal 2. Menghitung Total Pembelian Tiket 
# Topik: While Loop, For Loop  |  Estimasi waktu: 20 menit 

# Deskripsi: 
# Berdasarkan Soal 1 kembangan kode agar pelanggan dapat membeli tiket untuk lebih dari 
# satu film (atau lebih dari satu jenis tiket) dan program menghitung total harga seluruh 
# pembelian. 

# Ketentuan Program: 
# 1. Gunakan while loop agar pelanggan dapat terus menambah pembelian tiket. Loop berhenti 
# ketika pelanggan memasukkan angka 0. 
# 2. Simpan setiap pembelian ke dalam sebuah list berisi judul film dan jumlah tiket. 
# 3. Setelah selesai, tampilkan daftar pembelian menggunakan for loop beserta subtotal tiap 
# item (harga tiket × jumlah tiket). 
# 4. Tampilkan total harga keseluruhan di bagian akhir.

list_film = [["Danur", 50000],
             ['Inside Out', 45000],
             ["Doraemon", 60000],
             ["Spongbob", 55000],
             ["Boboiboy", 40000]]

daftar_film_dipilih = []
total_film = 0

while True:
    for i in range(len(list_film)):
        print(f"{i+1}. {list_film[i][0]} dengan harga Rp.{list_film[i][1]}")
    
    print("Masukkan 0 jika sudah selesai")
    pilihan = int(input("Masukkan film yang ingin dipilih : "))

    if pilihan == 0:
        break
    elif 1 <= pilihan <= len(list_film):
        jumlah = int(input("Jumlah tiket : "))
        film = list_film[pilihan-1]

        daftar_film_dipilih.append([film[0], jumlah, film[1] * jumlah])
        total_film += film[1] * jumlah
    else:
        print("Error")

for item in daftar_film_dipilih:
    print(f"{item[0]} x {item[1]} = Rp{item[2]}")

print(f"Total Harga : Rp{total_film}")