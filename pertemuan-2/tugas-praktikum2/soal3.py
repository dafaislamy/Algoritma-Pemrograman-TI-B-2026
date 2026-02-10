'''
Soal 3 (Rekursi - Penjumlahan Digit)

Buat sebuah fungsi rekursif bernama jumlah digit(n) yang:
1. Menghitung jumlah seluruh digit dari sebuah bilangan
2. Menggunakan konsep rekursi
Contoh:
Input: 1234
Output: 10
'''

def jumlah_digit(n): #deklarasi fungsi dengan nama jumlah_digit dengan parameter n
    if n == 0: #berperan sebagai case base, jika angka sudah 0, berhenti
        return 0
    else:
        return (n % 10) + jumlah_digit(n // 10) #(n % 10) berguna untuk mengambil digit terakhir, langkah rekursif terdapat pada jumlah_digit(n // 10) dimana fungsi memanggil dirinya sendiri, (n // 10) akan memproses sisa angka didepannya
    
input_angka = 1234
hasil = jumlah_digit(input_angka)
print('Jumlah seluruh digit dari bilangan 1234 adalah', hasil)