# Soal 3. Proses Pembayaran dan Kembalian 
# Topik: While Loop, If-Else |  Estimasi waktu: 20 menit 

# Deskripsi: 
# Setelah total pembelian diketahui, kasir perlu memproses pembayaran dari pelanggan dan 
# memberikan kembalian. 

# Ketentuan Program: 
# 1. Minta pengguna menginput total pembelian, kemudian masukkan jumlah uang yang 
# dibayarkan. 
# 2. Gunakan while loop untuk memastikan uang yang dibayarkan tidak kurang dari total 
# pembelian. Tampilkan pesan error dan minta input ulang jika kurang. 
# 3. Hitung kembalian dan tampilkan ringkasan transaksi: total pembelian, uang dibayar, dan 
# kembalian. 
# 4. Gunakan if-else untuk menampilkan pesan:  
# • “Uang pas, tidak ada kembalian” jika kembalian = 0, atau
# • “Kembalian Anda: Rp…” jika ada kembalian

total_bayar = int((input("Masukkan total belanja : ")))

while True:
    uang_masuk = int(input(f"Total pembayaran Rp{total_bayar}. Masukkan uang Anda : "))

    if uang_masuk >= total_bayar:
        break
    else:
        print("Uang Anda kurang, Silahkan masukkan jumlah uang baru")

kembalian = uang_masuk - total_bayar

print(f"Total bayar : Rp.{total_bayar}")
print(f"Dibayar : Rp.{uang_masuk}")

if kembalian == 0:
    print("Uang pas, tidak ada kembalian")
else:
    print(f"Kembalian Anda adalah Rp.{kembalian}")