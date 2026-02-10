'''
Soal 5 (Python Module dan Algoritma)

Buat sebuah program Python yang:
1. Menggunakan module math
2. Membuat fungsi jarak(x1, y1, x2, y2) untuk menghitung jarak dua titik pada bidang Kartesius
3. Menggunakan rumus:
d = ((x2 - x1)^2 + (y2 - y1)^2)^1/2

Contoh keluaran:
Jarak = 5.0
'''

import math #memakai modul math untuk menggunakan fungsi math.sqrt untuk menghitung akar kuadrat

def jarak(x1, y1, x2, y2): #deklarasi fungsi bernama jarak dengan parameter x1, y1, x2, y2
    hasil = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) #implementasi rumus menggunakan fungsi sqrt
    return hasil

titik_x1, titik_y1 = 0, 0
titik_x2, titik_y2 = 3, 4
hasil_jarak = jarak(titik_x1, titik_y1, titik_x2, titik_y2) #output hasil jarak adalah 5.0
print(hasil_jarak)