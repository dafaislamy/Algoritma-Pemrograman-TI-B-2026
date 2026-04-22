'''
Matriks merupakan salah satu struktur data fundamental dalam matematika dan ilmu komputer. 
Secara matematis, matriks didefinisikan sebagai susunan bilangan atau elemen yang 
diorganisasikan dalam baris dan kolom membentuk tabel dua dimensi. Dalam pemrograman 
Python, matriks dapat diimplementasikan menggunakan nested list (list bersarang) maupun library 
khusus seperti NumPy yang menawarkan performa komputasi jauh lebih tinggi.

Jenis-jenis Matriks
1. Matriks Pengukuran : jenis matriks yang setiap elemennya merepresentasikan hasil pengukuran
pada titik koordinat tertentu. Elemen-elemen dalam matriks ini bertipe data bilangan real (float).
2. Matriks Satuan (Identity Matrix) : matriks persegi yang elemen diagonal utamanya bernilai 1 dan seluruh 
elemen lainnya bernilai 0.
3. Matriks Nol : matriks yang seluruh elemennya bernilai 0. Matriks ini sering digunakan 
sebagai nilai awal (default) sebelum dilakukan pengisian data atau sebagai hasil dari operasi 
tertentu. 
'''

#Deklarasi dengan Inisialisasi Nilai
matriks_3x3 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

matriks_2x4 = [[10, 20, 30, 40],
               [50, 60, 70, 80]]
print("Matriks 3x3:", matriks_3x3)
print("Matriks 2x4:", matriks_2x4)

'''
output:
Matriks 3x3: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Matriks 2x4: [[10, 20, 30, 40], [50, 60, 70, 80]]
'''

#Matriks dengan Nilai Default
N, M = 4, 4
matriks_default = [[0 for j in range(M)] for i in range(N)]
print("Matriks default:", matriks_default)

#Mengakses elemen dengan indexing
matriks = [[10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]]
print(matriks[0][0]) #output 10 (baris 0, kolom 0)
print(matriks[1][2]) #output 60 (baris 1, kolom 2)
print(matriks[2]) #output [70, 80, 90] (seluruh baris 2)

#iterasi semua elemen
for i in range(len(matriks)):
    for j in range(len(matriks[i])):
        print(f"Matriks[{i}][{j}] = {matriks[i][j]}")

#Operasi pada Satu Matriks
#Menghitung total semua elemen
def total_elemen(matriks):
    total = 0
    for baris in matriks:
        for elemen in baris:
            total += elemen
    return total

matriks = [[1,2,3],
           [4,5,6],
           [7,8,9]]
print("Total elemen matriks :", total_elemen(matriks))

#Cara singkat dengan menggunakan fungsi bawaan Python
total_singkat = sum(sum(baris) for baris in matriks)
print("Total singkat : ", total_singkat)


#Perkalian Skalar
def kali_skalar(matriks, k):
    hasil = []
    for baris in matriks:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru)
    return hasil

E = [[1,2,3],
     [4,5,6]]
hasil = kali_skalar(E, 6)
for baris in hasil:
    print(baris)


#Transpose Matriks
def transpose(matriks):
    baris = len(matriks)
    kolom = len(matriks[0])

    hasil = [[0 for j in range(baris)] for i in range(kolom)]
    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = matriks[i][j]
    return hasil

K = [[1,2,3],
     [4,5,6]]
T = transpose(K)
for baris in T:
    print(baris)


#Determinan

#Determinan 2x2
def determinan_2x2(matriks):
    a, b = matriks[0][0], matriks[0][1]
    c, d = matriks[1][0], matriks[1][1]
    return (a * d) - (b * c)

A = [[1, 2],
     [3, 4]]
print("det (A) :", determinan_2x2(A))

#Determinan 3x3
def determinan_3x3(M):
    d1 = M[0][0] * M[1][1] * M[2][2]
    d2 = M[0][1] * M[1][2] * M[2][0] 
    d3 = M[0][2] * M[1][0] * M[2][1]  
    d4 = M[0][2] * M[1][1] * M[2][0] 
    d5 = M[0][0] * M[1][2] * M[2][1] 
    d6 = M[0][1] * M[1][0] * M[2][2] 
    return (d1 + d2 + d3) - (d4 + d5 + d6)

B = [[1,2,3],
     [4,5,6],
     [7,2,9]]
print("det (B) :", determinan_3x3(B))


#Inverse Matriks
def determinan_2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

def inverse_2x2(matriks):
    det = determinan_2x2(matriks)
    if det == 0:
        print("Matriks Singular: Inverse tidak ada (det = 0)")
        return 0
    a, b = matriks[0][0], matriks[0][1]
    c, d = matriks[1][0], matriks[1][1]
    return [[d/det],[-b/det],
            [-c/det],[a/det]]

A = [[4, 7],
     [2, 6]]

inv = inverse_2x2(A)
for baris in inv:
    print(baris)


#Operasi pada Dua Matriks
#Penjumlahan Dua Matriks
def tambah_matriks(A, B): 
    if len(A) != len(B) or len(A[0]) != len(B[0]): 
        print('Error: ukuran matriks tidak sama') 
        return None 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in 
range(baris)] 
    return hasil 
 
A = [[1, 2, 3], [4, 5, 6]] 
B = [[7, 8, 9], [1, 2, 3]] 
 
C = tambah_matriks(A, B) 
for baris in C: 
    print(baris) 
 
# Output: 
# [8, 10, 12] 
# [5, 7, 9]


#Pengurangan Dua Matriks
def kurang_matriks(A, B): 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in 
range(baris)] 
    return hasil 
 
A = [[10, 8, 6], [4,  2, 0]] 
B = [[1,  3, 5], [7,  9, 11]] 
 
D = kurang_matriks(A, B) 
for baris in D: 
    print(baris) 
 
# Output: 
# [9, 5, 1] 
# [-3, -7, -11]


#Perkalian Dua Matriks
def kali_matriks(A, B):
    baris_A, kolom_A = len(A), len(A[0])
    baris_B, kolom_B = len(B), len(B[0])
    if kolom_A != baris_B:
        print("Error : Kolom A harus sama dengan kolom B")
        return None
    hasil = [[0] * kolom_B for _ in range(baris_A)]
    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil

A = [[1,2], [3,4], [5,6]]
B = [[7,8,9], [10,11,12]]

C = kali_matriks(A, B)
for baris in C:
    print(baris)


#Pembagian Matriks (Elemen per Elemen)
def bagi_matriks_elementwise(A, B): 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[0.0]*kolom for _ in range(baris)] 
    for i in range(baris): 
        for j in range(kolom): 
            if B[i][j] == 0: 
                print(f'Error: pembagi 0 pada posisi [{i}][{j}]') 
                return None 
            hasil[i][j] = A[i][j] / B[i][j] 
    return hasil 

A = [[10, 20, 30], [40, 50, 60]] 
B = [[2,  4,  5],  [8,  10, 12]] 

E = bagi_matriks_elementwise(A, B) 

for baris in E: 
    print(baris) 

# Output: 
# [5.0, 5.0, 6.0] 
# [5.0, 5.0, 5.0]

