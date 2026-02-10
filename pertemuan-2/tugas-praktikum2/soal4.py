'''
Soal 4 (Rekursi dan Deret)

Buat sebuah fungsi rekursif bernama pangkat rekursif(a, b) yang:
1. Menghitung nilai a^b
2. Tidak boleh menggunakan operator pangkat (**)
3. Harus menggunakan rekursi
Contoh:
Input: a = 2, b = 5
Output: 32
'''

def pangkat_rekursif(a, b): #deklarasi fungsi bernama pangkat_rekursif dengan parameter (a, b)
    if b == 0: #berperan sebagai case base, semua bilangan yang dipangkatkan 0 menghasilkan 1
        return 1
    else:
        return a * pangkat_rekursif(a, b - 1) #konsep rekursif digunakan dimana a^b dapat diubah menjadi a * a^b-1, sehingga fungsinya akan dipanggil kembali didalam fungsi tersebut
    
hasil = pangkat_rekursif(2, 5)
print('Hasil 2 pangkat 5 adalah', hasil)