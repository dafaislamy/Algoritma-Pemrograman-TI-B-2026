'''
Studi Kasus untuk menghitung jumlah patungan makan antar teman.
Program akan meminta dua input yaitu total tagihan belanja (harus berupa angka float) dan jumlah orang (harus berupa angka integer)
Jika pengguna memasukkan "Seratus ribu" bukannya "100000" pada total tagihan, atau memasukkan "0" pada jumlah orang,
Python akan melempar error dan meminta ulang input dari pengguna.
'''

def hitung_patungan():

    while True:
        #program meminta input user
        try:
            total_tagihan = float(input("Masukkan total tagihan: "))
            jumlah_orang = int(input("Masukkan jumlah orang: "))
        
            hasil = total_tagihan / jumlah_orang
        
        #ValueError akan ditampilkan jika input user bukan angka
        except ValueError:
            print("Input harus berupa angka! Jangan memasukkan huruf atau simbol.")
        
        #ZeroDivideError akan ditampilkan jika input user berupa angka 0
        except ZeroDivisionError:
            print("Jumlah orang tidak bisa nol. Siapa yang mau bayar?")
        
        #Akan menampilkan error lainnya yang tidak terduga
        except:
            print(f"Terjadi kesalahan yang tidak diketahui")
        
        #Else akan ditampilkan hanya jika tidak terdapat kesalahan pada kode
        else:
            print(f"\nSetiap orang harus membayar: Rp{hasil:,.2f}")
        
        #Finally akan selalu ditampilkan apa pun yang terjadi
        finally:
            print("Terima kasih telah menggunakan layanan kami.")

# Menjalankan fungsi
hitung_patungan()