'''Algoritma Insertion Sort menggunakan satu bagian dari
array untuk menyimpan nilai-nilai yang sudah diurutkan,
dan bagian lain dari array untuk menyimpan nilai-nilai yang belum diurutkan.

Algoritma ini mengambil satu nilai pada satu waktu dari bagian array yang belum
diurutkan dan menempatkannya di tempat yang tepat di bagian array yang sudah diurutkan,
hingga array tersebut menjadi terurut.

Cara kerjanya:
1. Ambil nilai pertama dari bagian array yang belum diurutkan.
2. Pindahkan nilai tersebut ke tempat yang tepat di bagian array yang sudah diurutkan.
3. Lakukan penelusuran ulang pada bagian array yang belum diurutkan sebanyak jumlah nilai yang ada.

Untuk mengimplementasikan algoritma Insertion Sort dalam program Python, kita membutuhkan:
1. Sebuah array berisi nilai-nilai yang akan diurutkan.
2. Sebuah loop luar yang memilih nilai untuk diurutkan. Untuk sebuah array dengan N nilai,
loop luar ini melewatkan nilai pertama, dan harus dijalankan N − 1 kali.
3. Sebuah loop dalam yang menelusuri bagian array yang sudah diurutkan,
untuk menemukan tempat memasukkan nilai. Jika nilai yang akan diurutkan berada di indeks i,
bagian array yang sudah diurutkan dimulai pada indeks 0 dan berakhir pada indeks i − 1.
'''

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
  insert_index = i
  current_value = mylist.pop(i)
  for j in range(i-1, -1, -1):
    if mylist[j] > current_value:
      insert_index = j
  mylist.insert(insert_index, current_value)

print(mylist)


#improvements
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
  insert_index = i
  current_value = mylist[i]
  for j in range(i-1, -1, -1):
     if mylist[j] > current_value:
       mylist[j+1] = mylist[j]
       insert_index = j
     else:
       break
  mylist[insert_index] = current_value

print(mylist)