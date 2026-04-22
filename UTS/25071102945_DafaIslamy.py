'''
Bagian A — Fungsi Inti Game (60 poin) 

Buat tiga fungsi berikut: 
1. tebak_angka(angka_rahasia, maks_percobaan) 
Minta input tebakan dari pemain secara berulang menggunakan loop. Cetak 
petunjuk "Terlalu kecil", "Terlalu besar", atau "Benar!" sesuai hasil perbandingan. 
Kembalikan True jika pemain berhasil menebak, atau False jika percobaan habis. 
2. hitung_skor(berhasil, sisa_percobaan) 
Jika pemain berhasil (berhasil = True), kembalikan nilai sisa_percobaan × 10 
sebagai skor. Jika tidak berhasil, kembalikan 0. 
3. main_satu_ronde(nama, nomor_ronde) 
Ambil angka rahasia dari DAFTAR_ANGKA berdasarkan nomor_ronde. 
Jalankan tebak_angka() untuk mendapatkan hasil, kemudian panggil 
hitung_skor() untuk menghitung skor. Kembalikan list [nama, skor]. 
'''

#=== BAGIAN A ===

daftar_angka = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]

data_final = []

def tebak_angka(angka_rahasia, maks_percobaan):
    #Fungsi untuk memeriksa inputan dari pemain
    global sisa_percobaan
    x = maks_percobaan
    while x:
        tebakan = int(input('Masukkan angka tebakan : '))
        if tebakan < angka_rahasia:
            print("Terlalu kecil")
        elif tebakan > angka_rahasia:
            print("Terlalu besar")
        else:
            print("Benar!")
            sisa_percobaan = x
            x = 0
            return True
        x -= 1
    sisa_percobaan = 0
    return False
        

def hitung_skor(berhasil, sisa_percobaan):
    #Fungsi untuk menghitung skor pemain
    if berhasil:
        return sisa_percobaan * 10
    else:
        return 0


def main_satu_ronde(nama, nomor_ronde):
    #Fungsi untuk membuat ronde untuk pemain
    global angka_rahasia
    global data_final
    angka_rahasia = daftar_angka[(nomor_ronde-1) % len(daftar_angka)]
    print(f"Ronde ke-{nomor_ronde}")
    berhasil = tebak_angka(angka_rahasia, 7)
    data = []
    data.append(nama)
    data.append(hitung_skor(berhasil, sisa_percobaan))
    data_final.append(data)



'''
Bagian B — Riwayat Skor dengan Matrix 2D (20 poin) 

Buat fungsi berikut: 
1. tampilkan_riwayat(riwayat) 
Cetak seluruh isi list riwayat dalam format tabel yang memuat kolom nomor, 
nama, dan skor. Jika list riwayat kosong, tampilkan pesan: "Belum ada riwayat." 
'''

#=== BAGIAN B ===

def tampilkan_riwayat(riwayat):
    #Fungsi untuk menampilkan riwayat permainan pemain
    if len(riwayat):
        print("Nomor | Nama | Skor")
        for i in range(len(riwayat)):
            print(f"{i+1}. | {data_final[i][0]} | {data_final[i][1]}")
    else:
        print("Belum ada riwayat")



'''
Bagian C — Leaderboard dengan Selection Sort (20 poin) 

Buat dua fungsi berikut: 
1. selection_sort_riwayat(riwayat) 
Buat salinan dari list riwayat, lalu urutkan salinan tersebut dari skor tertinggi ke 
terendah menggunakan algoritma Selection Sort. Data asli (parameter riwayat) 
tidak boleh berubah. Kembalikan salinan yang sudah terurut. 
2. tampilkan_leaderboard(riwayat) 
Panggil selection_sort_riwayat() untuk mendapatkan data yang terurut, kemudian 
cetak hasilnya beserta nomor peringkat. Berikan tanda bintang (*) pada entri 
dengan peringkat pertama.
'''

#=== BAGIAN C ===

def selection_sort_riwayat(riwayat):
    #Fungsi untuk mengurutkan skor pemain dari terbesar ke terkecil
    urut = []
    urut = riwayat.copy()
    n = len(urut)
    for i in range(n):
        maks_index = i
        for j in range(i+1, n):
            if urut[j][i] > urut[maks_index][i]:
                maks_index = j
        urut[i], urut[maks_index] = urut[maks_index], urut[i]
    return urut


def tampilkan_leaderboard(riwayat):
    #Fungsi untuk menampilkan riwayat permainan pemain setelah diurutkan
    print("Nomor | Nama | Skor")
    hasil = selection_sort_riwayat(riwayat)
    for i in range(len(hasil)):
        if i == 0:
            print(f"*{i+1}. | {hasil[i][0]} | {hasil[i][1]}")
        else:
            print(f"{i+1}.  | {hasil[i][0]} | {hasil[i][1]}")
    


'''
Program Utama 

Susun alur program utama sebagai berikut: 
1. Minta nama pemain menggunakan input() di awal program. 
2. Jalankan main_satu_ronde() untuk memulai satu ronde permainan, lalu simpan 
hasilnya ke dalam list riwayat. 
3. Setelah setiap ronde selesai, tanyakan kepada pemain apakah ingin bermain lagi. 
Gunakan loop while untuk mengulang selama pemain memilih ya. 
4. Saat sesi berakhir, panggil tampilkan_riwayat() untuk menampilkan semua ronde 
yang telah dimainkan, kemudian panggil tampilkan_leaderboard() untuk 
menampilkan peringkat akhir.
'''

#=== PROGRAM UTAMA ===

nama = input("Masukkan nama Anda: ")
ronde = 1
cek = "iya"
while cek.lower() == "iya":
    main_satu_ronde(nama, ronde)
    ronde += 1
    cek = input("Apakah ingin bermain lagi? (iya/tidak) : ")

tampilkan_riwayat(data_final)
print("")
tampilkan_leaderboard(data_final)