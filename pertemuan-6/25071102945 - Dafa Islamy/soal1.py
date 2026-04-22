# Soal 1. Menampilkan Daftar Film 
# Topik: For Loop, If-Else  |  Estimasi waktu: 15 menit 

# Deskripsi: 
# Buatlah program untuk menampilkan daftar film yang tersedia dan meminta pelanggan 
# memilih satu film. 

# Ketentuan Program: 
# 1. Buat list film berisi 5 item film beserta harga tiketnya, contoh: [[ "Danur", 50000 ], [ 
# "Inside Out 2", 45000 ], ...]. 
# 2. Tampilkan seluruh daftar film beserta harga menggunakan for loop dengan penomoran. 
# 3. Minta pengguna memasukkan nomor film yang dipilih. 
# 4. Gunakan if-else untuk memvalidasi input: jika nomor tidak valid, tampilkan pesan error; 
# jika valid, tampilkan judul film dan harga tiket film yang dipilih.

list_film = [["Danur", 50000],
             ['Inside Out 2', 45000],
             ["Doraemon", 60000],
             ["Spongbob", 55000],
             ["Boboiboy", 40000]]

for i in range(len(list_film)):
    print(f"{i+1}. {list_film[i][0]} dengan harga Rp.{list_film[i][1]}")

pilihan = int(input("Masukkan nomor film yang ingin dipilih : "))
if 1 <= pilihan <= len(list_film):
    film_terpilih = list_film[pilihan-1]
    print(f"Film yang dipilih adalah {film_terpilih[0]} dengan harga {film_terpilih[1]}")
else:
    print("Error")