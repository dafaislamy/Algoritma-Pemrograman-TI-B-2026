# Buatlah program python (tanpa NumPy) yang:
# a. Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah
# b. Mengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
# c. Mengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam C_skalar
# d. Menampilkan ketiga hasil dengan format rapi baris per baris

A = [[5, 3, 1],
     [2, 8, 4],
     [6, 0, 7]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


#penambahan dua matriks
def tambah(A, B): 
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Error, ukuran matriks tidak sama")
        return None
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil
 
C_tambah = tambah(A, B)


#pengurangan dua matriks
def kurang(A, B): 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)] 
    return hasil
 
C_kurang = kurang(A, B)


#perkalian skalar
def kali_skalar(matriks, k): 
    hasil = [] 
    for baris in matriks: 
        baris_baru = [elemen * k for elemen in baris] 
        hasil.append(baris_baru) 
    return hasil 
 
C_skalar = kali_skalar(A, 4)


print("a. Menambahkan dua matriks")
for baris in C_tambah:
    print(baris)
print("")

print("b. Mengurangi dua matriks")
for baris in C_kurang:
    print(baris)
print("")

print("c. Perkalian skalar")
for baris in C_skalar:
    print(baris)