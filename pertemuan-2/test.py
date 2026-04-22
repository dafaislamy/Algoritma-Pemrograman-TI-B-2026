# def cariNilaiMax(arr):
#     max_val = arr[0]
#     for x in arr:
#         if x > max_val:
#             max_val = x
#     return max_val

# print(cariNilaiMax([0,2,6,3]))


# # #Menghitung jumlah seluruh bilangan genap
# n = int(input("Masukkan sebuah bilangan positif (n) : "))
# hasil = 0

# for i in range(1, n+1):
#     if i % 2 == 0:
#         hasil += i

# print(f"Jumlah seluruh bilangan genap dari 1 sampai {n} adalah {hasil}")


# # #Menghitung jumlah seluruh bilangan ganjil
# n = int(input("Masukkan sebuah bilangan positif (n) : "))
# hasil = 0

# for i in range(1, n+1):
#     if i % 2 != 0:
#         hasil += i

# print(f"Jumlah seluruh bilangan ganjil dari 1 sampai {n} adalah {hasil}")


# #Menghitung nilai terbesar (max)
# n = int(input("Masukkan banyak bilangan : "))
# nilai = []

# for i in range(n):
#     bil = int(input(f"Masukkan bilangan ke-{i+1} : "))
#     nilai.append(bil)

# maks = nilai[0]
# for i in nilai:
#     if i > maks:
#         maks = i

# print(f"Nilai terbesar diantara {nilai} adalah {maks}")


# a = [1,2,3]
# b = a
# print(a is b) #True
# print(a == b) #True
# b.append(4)
# print(a) #[1,2,3,4], karena a dan b menunjuk referensi objek yang sama

# a = [1,2,3]
# b = [1,2,3]
# print(a == b) #True
# print(a is b) #False


#Menghitung banyak bilangan yang bernilai positif

#Input pengguna
# n = int(input("Masukkan jumlah bilangan : "))
# jumlah_positif = 0

# for i in range(n):
#      nilai = int(input(f"Masukkan bilangan ke-{i+1} : "))
    
#      if nilai > 0:
#         jumlah_positif += 1

#Input langsung
# nilai = [6,1,-2,7,-4,5]
# jumlah_positif = 0

# for i in nilai:
#     if i > 0:
#         jumlah_positif += 1
        

# print(f"Banyak bilangan positif adalah : {jumlah_positif}")


#Rata-rata dari bilangan genap
# n = 5
# data = [2,3,4,7,8]
# total_genap = 0
# hitung_genap = 0

# for i in data:
#     if i % 2 == 0:
#         total_genap += i
#         hitung_genap += 1

# if hitung_genap > 0:
#     rata_rata = total_genap / hitung_genap
#     print(f"Rata-rata bilangan genap adalah :{rata_rata : .2f}")
# else:
#     print("Rata-rata adalah 0 (tidak ada bilangan genap)")
        

# def hitung_skor(poin_dasar, bonus):
#     """Menghitung total skor berdasarkan poin dan bonus."""
#     return poin_dasar + bonus

# def main_game():
#     """Fungsi utama untuk menjalankan logika permainan per ronde."""
#     riwayat_skor = []
#     bermain = True
    
#     while bermain:
#         nama = input("Masukkan nama: ")
#         skor = int(input("Masukkan skor: "))
#         # Memanggil fungsi lain di dalam fungsi
#         total = hitung_skor(skor, 10) 
#         riwayat_skor.append([nama, total])
        
#         opsi = input("Main lagi? (y/n): ")
#         if opsi.lower() != 'y':
#             bermain = False
            
#     return riwayat_skor



# def tampilkan_tabel(data_matrix):
#     """Menampilkan data matrix dalam format tabel di terminal."""
#     if not data_matrix:
#         print("Data kosong!")
#         return

#     print(f"{'No':<4} | {'Nama':<15} | {'Skor':<10}")
#     print("-" * 35)
    
#     for i in range(len(data_matrix)):
#         nama = data_matrix[i][0]
#         skor = data_matrix[i][1]
#         print(f"{i+1:<4} | {nama:<15} | {skor:<10}")



# def selection_sort_leaderboard(data):
#     """Mengurutkan data berdasarkan skor secara descending (terbesar ke terkecil)."""
#     # Salin data agar data asli tidak berubah
#     hasil = data[:] 
#     n = len(hasil)
    
#     for i in range(n):
#         # Cari indeks dengan skor tertinggi dari sisa list
#         idx_max = i
#         for j in range(i + 1, n):
#             if hasil[j][1] > hasil[idx_max][1]: # Bandingkan elemen skor (indeks 1)
#                 idx_max = j
        
#         # Tukar posisi (Swap)
#         hasil[i], hasil[idx_max] = hasil[idx_max], hasil[i]
        
#     return hasil



# ==========================================
# BAGIAN A — FUNGSI DAN LOGIKA PROGRAM
# ==========================================

def hitung_skor_akhir(skor_mentah, bonus):
    """Menghitung skor akhir dengan tambahan bonus tertentu."""
    return skor_mentah + bonus

def jalankan_permainan():
    """Mengambil input user secara berulang dan mengembalikan list data pemain."""
    daftar_skor = []
    lagi = 'y'
    
    while lagi.lower() == 'y':
        nama = input("Masukkan Nama Pemain: ")
        skor = int(input(f"Masukkan Skor {nama}: "))
        
        # Memanggil fungsi lain untuk memproses nilai
        total_skor = hitung_skor_akhir(skor, 5) 
        
        # Menyimpan ke dalam list 2D [nama, skor]
        daftar_skor.append([nama, total_skor])
        
        lagi = input("Tambah pemain lagi? (y/n): ")
        print("-" * 20)
        
    return daftar_skor

# ==========================================
# BAGIAN C — ALGORITMA PENGURUTAN MANUAL
# ==========================================

def urutkan_skor(data):
    """Mengurutkan data menggunakan Selection Sort (descending) tanpa mengubah data asli."""
    # Membuat salinan agar data asli (in-place) tidak berubah
    data_urut = data[:] 
    n = len(data_urut)
    
    for i in range(n):
        # Asumsikan indeks saat ini adalah yang terbesar
        idx_maks = i
        for j in range(i + 1, n):
            # Bandingkan nilai skor (indeks 1 pada sub-list)
            if data_urut[j][1] > data_urut[idx_maks][1]:
                idx_maks = j
        
        # Tukar posisi secara manual (swap)
        data_urut[i], data_urut[idx_maks] = data_urut[idx_maks], data_urut[i]
        
    return data_urut

# ==========================================
# BAGIAN B — STRUKTUR DATA LIST DAN MATRIX 2D
# ==========================================

def tampilkan_leaderboard(matrix_data):
    """Menampilkan matrix 2D dalam bentuk tabel leaderboard."""
    if not matrix_data:
        print("\n[!] Leaderboard Kosong. Belum ada data pemain.")
    else:
        print("\n=== LEADERBOARD PERMAINAN ===")
        print(f"{'Rank':<5} | {'Nama':<15} | {'Skor':<10}")
        print("-" * 35)
        
        # Iterasi untuk menampilkan data
        for i in range(len(matrix_data)):
            peringkat = i + 1
            nama = matrix_data[i][0]
            skor = matrix_data[i][1]
            print(f"{peringkat:<5} | {nama:<15} | {skor:<10}")

# ==========================================
# PROGRAM UTAMA — ALUR DAN INTEGRASI
# ==========================================

def main():
    """Mengintegrasikan seluruh fungsi menjadi alur program yang utuh."""
    print("Selamat Datang di Program Pencatat Skor!")
    
    # 1. Ambil data melalui perulangan
    data_mentah = jalankan_permainan()
    
    # 2. Urutkan data secara manual (Selection Sort)
    data_terurut = urutkan_skor(data_mentah)
    
    # 3. Tampilkan hasil akhir dalam bentuk tabel
    tampilkan_leaderboard(data_terurut)
    
    print("\nProgram Selesai. Terima kasih!")

# Menjalankan program utama
if __name__ == "__main__":
    main()




# baris = int(input('Jumlah baris : '))
# kolom = int(input('Jumlah kolom : '))

# matriks = []

# for i in range(baris):
#     print(f"Masukkan baris ke-{i+1} ({kolom} angka, pisah spasi) : ")
#     data = list(map(int, input().split()))
#     matriks.append(data)

# print(matriks)


# matriks = [[1,2,3],
#            [4,5,6],
#            [7,8,9]
#            ]

# for i in range(len(matriks)):
#     for j in range(len(matriks[0])):
#         print(matriks[i][j], end=" ")
#     print()

# for row in matriks:
#     print(row)


# #Tentukan elemen terbesar dalam matriks berikut
# A = [[1,20,3],
#      [4,5,6],
#      [7,8,9]]

# bigger = A[0][0]
# rows = len(A)
# cols = len(A[0])

# for i in range(rows):
#     for j in range(cols):
#         if A[i][j] > bigger:
#             bigger = A[i][j]

# print("Elemen terbesar dari matriks A adalah :", bigger)


# #Jumlahkan seluruh elemen dalam matriks berikut
# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# jumlah = 0
# rows = len(A)
# cols = len(A[0])

# for i in range(rows):
#     for j in range(cols):
#         jumlah += A[i][j]

# print("Jumlah seluruh elemen dalam matriks A adalah :", jumlah)


# A = [[1,2,3],
#      [4,5,6]]
# B = [[7,8],
#      [9,10],
#      [11,12]]

# rows_A = len(A)
# cols_A = len(A[0])
# rows_B = len(B)
# cols_B = len(B[0])

# C = [[0 for j in range(cols_B)] for i in range(rows_A)]

# for i in range(rows_A):
#     for j in range(cols_B):
#         for k in range(cols_A):
#             C[i][j] += A[i][k] * B[k][j]

# for row in C:
#     print(row)


#Kesamaan dua matriks
# A = [[1,2],
#      [3,4]]
# B = [[1,2],
#      [3,4]]

# rows_A = len(A)
# cols_A = len(A[0])
# rows_B = len(B)
# cols_B = len(B[0])

# if rows_A != rows_B and cols_A != cols_B:
#     print("Matriks tidak sama")
# else:
#     for i in range(rows_A):
#         for j in range(cols_A):
#             if A[i][j] != B[i][j]:
#                 print("Matriks tidak sama")
#                 break
#         else:
#             continue
#         break
#     else:
#         print("Matriks sama")


#Matriks Simetri
# A = [[1,2,3],
#      [2,5,6],
#      [3,6,9]]

# simetri = True
# rows = len(A)
# cols = len(A[0])

# if rows != cols:
#     simetri = False
# else:
#     for i in range(rows):
#         for j in range(i+1, cols):
#             if A[i][j] != A[j][i]:
#                 simetri = False
#                 break
#         if not simetri:
#             break

# if simetri:
#     print("matriks simetri")
# else:
#     print("matriks tidak simetri")


# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# print('diagonal utama :')
# for i in range(len(A)):
#     print(A[i][i])

# print("diagonal samping :")
# n = len(A)
# for i in range(n):
#     print(A[i][n-1-i])


#Buat Matriks 3x3 menggunakan list python, lalu tampilkan jumlah baris, kolom, dan elemen tertentu
# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# print(f"Jumlah baris : {len(A)}")
# print(f"Jumlah kolom : {len(A[0])}")
# print(f"Elemen baris 1 kolom 1 : {A[0][0]}")


#Hitung A+B dan A-B dari dua matriks berikut tanpa library apapun
# A = [[1,2],
#      [3,4]]
# B = [[5,6],
#      [7,8]]

# rows = len(A)
# cols = len(A[0])

# C_tambah = [[0 for j in range(cols)] for i in range(rows)]
# C_kurang = [[0 for j in range(cols)] for i in range(rows)]


# for i in range(rows):
#     for j in range(cols):
#         C_tambah[i][j] = A[i][j] + B[i][j]
#         C_kurang[i][j] = A[i][j] - B[i][j]

# for row in C_tambah:
#     print(row)

# for row in C_kurang:
#     print(row)


#Buat program python untuk menghitung jumlah elemen diagonal utama dari matriks nxn
# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# jumlah = 0

# for i in range(len(A)):
#     jumlah += A[i][i]

# print(jumlah)


#Hitung jumlah setiap baris matriks dan kolom matriks
# A = [[2,3,4],
#      [5,6,7],
#      [8,9,1]]

# rows = len(A)
# cols = len(A[0])

# #jumlah baris
# for i in range(rows):
#     jumlah_baris = 0
#     for j in range(cols):
#         jumlah_baris += A[i][j]
#     print(f"Jumlah baris ke-{i+1} : {jumlah_baris}")

# #jumlah kolom
# for j in range(cols):
#     jumlah_kolom = 0
#     for i in range(rows):
#         jumlah_kolom += A[i][j]
#     print(f"Jumlah kolom ke-{j+1} : {jumlah_kolom}")


# Tukar baris pertama dengan baris terakhir matriks
# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# id_pertama = 0
# id_terakhir = len(A) - 1

# A[id_pertama], A[id_terakhir] = A[id_terakhir], A[id_pertama]

# for row in A:
#     print(row)