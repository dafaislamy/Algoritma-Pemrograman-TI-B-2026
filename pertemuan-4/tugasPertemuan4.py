'''Sumber : w3school.com
1.	Try Exception
Struktur Try Exception biasanya terdiri dari fungsi-fungsi berikut :

try: berguna untuk menguji blok kode untuk mencari kesalahan
except: berguna untuk menangani kesalahan
else: berguna untuk menjalankan kode ketika tidak ada kesalahan
finally: berguna untuk mengeksekusi kode, terlepas dari hasil blok try dan except

	Ketika terjadi kesalahan, atau yang biasa disebut Exception, Python biasanya akan berhenti dan menghasilkan pesan kesalahan. Tetapi Exception ini dapat ditangani dengan menggunakan try statement. Sebagai contoh :
'''

try:
	print(x)
except:
	print("An exception occurred")

'''
Blok kode try akan menghasilkan exception karena x tidak didefinisikan. Karena blok try menimbulkan kesalahan (error), maka blok except akan dieksekusi atau dijalankan. Tanpa menggunakan blok try, program akan mengalami crash dan menampilkan kesalahan (error).
Print(x)

Output :
Traceback (most recent call last):
  File "demo_try_except_error.py", line 3, in <module>
    print(x)
NameError: name 'x' is not defined
	Exception blok dapat didefinisikan sebanyak mungkin, jika ingin menjalankan blok kode khusus untuk jenis kesalahan (error) tertentu. Sebagai contoh :
'''

try:
	print(x)
except NameError:
	print("Variable x is not defined")
except:
	print("Something else went wrong")

'''
Output dari program diatas yaitu menampilkan pesan “Variable x is not defined” karena jenis kesalahan (error) pada program berupa NameError. Jadi, output akan menghasilkan satu pesan jika blok try menimbulkan kesalahan (error) NameError dan pesan lain untuk kesalahan (error) lainnya.
Else keyword dapat digunakan dalam Try Exception jika blok kode yang dijalankan tidak terdapat kesalahan (error) didalamnya. Sebagai contoh :
'''

try:
	print("Hello")
except:
	print("Semothing went wrong")
else:
	print("Nothing went wrong")
'''
Output program tersebut akan menampilkan pesan “Nothing went wrong” pada blok else statement karena tidak terdapat pada blok kode try statement.
Selanjutnya adalah blok finally, jika ditentukan, maka blok ini akan dijalankan baik terdapat kesalahan (error) atau tidak. Sebagai contoh :
'''

try:
	print(x)
except:
	print("Something went wrong")
finally:
	print("The ‘try except’ is finished")
	
'''
Sebagai Python developer, kita dapat memilih untuk melempar exception jika suatu kondisi diperlukan, untuk melakukannya dapat menggunakan raise keyword. Sebagai contoh :
'''

x = -1
if x < 0:
	raise Exception("Sorry, no numbers below zero")

'''
Output akan menampilkan pesan “Sorry, no numbers below zero” karena pada kode ditetapkan jika x < 0 maka terjadi exception.
'''

'''
2.	User Input
Python memungkinkan input dari pengguna (user), yang berarti pengguna dapat memberikan masukan (input) pada program. Sebagai contoh, program meminta input dari pengguna untuk memasukkan nama, setelah pengguna memasukkan nama, nama tersebut akan dicetak ke layar.
'''

print("Enter your name: ")
name = input()
print(f"Hello {name}")

'''
Python akan berhenti mengeksekusi program ketika sampai pada fungsi input() dan akan melanjutkan eksekusi ketika pengguna telah memberikan input.
Pada contoh sebelumnya, pengguna harus memasukkan nama pada baris baru, tetapi fungsi input() memiliki prompt parameter yang berfungsi sebagai pesan yang dapat diletakkan didepan input pengguna pada baris yang sama. Sebagai contoh :
'''

name = input("Enter your name:")
print(f"Hello {name}")

'''
Program dapat memiliki fungsi input sebanyak mungkin dan akan berhenti mengeksekusi pada setiap input tersebut, menunggu input dari pengguna. Sebagai contoh :
'''

name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite food:")
fav2 = input("What is your favorite drink:")
print(f"Hei {name}, do you want {fav1} and {fav2}?")

'''
Input dari user dianggap sebagai string. Walaupun input dari user terdapat angka didalamnya, tetapi angka tersebut tetap dianggap string. Tetapi input tersebut dapat diubah menjadi angka (number) dengan fungsi float(). Sebagai contoh :
'''

x = input("Enter a number: ")
y = math.sqrt(float(x)) #fungsi untuk mencari akar kuadrat
print(f"The square root of {x} is {y}")

'''
Untuk mencari akar kuadrat, input harus berupa number.
Merupakan praktik yang baik untuk memvalidasi setiap input dari pengguna. Pada contoh sebelumnya, akan terjadi kesalahan jika input tersebut tidak berupa angka. Maka untuk menghindarinya, input dapat diuji, jika input bukan angka, pengguna dapat menerima pesan seperti “Wrong input, please try again” dan dapat memasukkan input baru.
'''

y = True
while y == True:
    x = input("Enter a number:")
    try:
        x = float(y)
        y = False
    except:
        print("Wrong input, please try again.")

'''
Sumber : cisco.com
1.	Try Exception
Menangani kesalahan pemrograman memiliki dua sisi. Yang pertama muncul ketika kode yang tampaknya benar tetapi diberi data yang salah. Misalnya kode program mengaharapkan input dari pengguna berupa bilangan bulat tetapi pengguna malah memasukkan huruf. Yang kedua terungkap ketika perilaku kode yang tidak diinginkan disebabkan oleh kesalahan yang dibuat saat menulis kode program. Jenis kesalahan ini biasanya disebut “bug”.
'''

value = int(input('Enter a natural number: '))
print('The reciprocal of', value, 'is', 1/value)
'''
Kode diatas merupakan sebuah kode program yang akan membaca bilangan bulat dan mencetak kebalikannya. Kode ini sangat singkat dan ringkas sehingga sepertinya tidak akan menemukan masalah. Tetapi jika pengguna memasukkan data yang bukan bilangan bulat (termasuk tidak memasukkan apapun) akan sepenuhnya merusak eksekusi program dan akan menampilkan pesan berikut.
Traceback (most recent call last):
   File "code.py", line 1, in
    value = int(input('Enter a natural number: '))
ValueError: invalid literal for int() with base 10: ''
	Semua baris yan ditampilkan bermakna dan penting, tetapi baris terakhir merupakan yang paling berharga. Kata pertama dalam baris tersebut nama pengecualian (exception) yang menyebabkan kode berhenti. Namanya adalah “ValueError”, maka munculnya exception untuk menangani masalah ini. Exception terdiri dari try dan except dimana kode try berguna untuk menandai tempat dimana mencoba melakukan sesuatu tanpa izin dan kode except mengawali sebuah lokasi dimana dapat memamerkan bakat minta maaf Anda. Pendekatan ini menerima kesalahan (memperlakukan kesalahan sebagai bagia normal dari siklus kehidupan progam) alih-alih meningkatkan upaya untuk menghindari kesalahan sama sekali.
'''
	
try:
	nilai = int(input("Masukkan bilangan asli: "))
	print(f"Kebalikan dari {nilai} adalah 1/{nilai}")
except:
	print("Saya tidak tahu harus berbuat apa.")
'''
Pada kode program diatas, jika input dari pengguna tidak berupa bilangan asli, maka except akan dijalankan dan akan menampilkan pesan “Saya tidak tahu harus berbuat apa”, tetapi jika input berupa bilangan asli, maka try akan dijalankan dan program berjalan dengan lancar.
'''

try:
    nilai = int(input("Masukkan bilangan asli: "))
    print(f"Kebalikan dari {nilai} adalah 1/{nilai}")        
except ValueError:
    	print("Saya tidak tahu harus berbuat apa.")    
except ZeroDivisionError:
    	print("Pembagian dengan nol tidak diperbolehkan.")

'''
Try-except dapat ditulis bercabang dengan menjelaskan setiap nama except, seperti pada contoh diatas, jika input pengguna berupa huruf atau input selain bilangan asli, termasuk pada except ValueError dan akan menampilkan pesan “Saya tidak tahu harus berbuat apa”, tetapi jika input pengguna berupa bilangan 0, termasuk pada except ZeroDivisonError dan akan menampilkan pesan “Pembagian dengan nol tidak diperbolehkan.
Terdapat beberapa jenis dari exception, diantaranya ZeroDivisonError, ValueError, TypeError, AttributeError, dan SyntaxError. Terdapat tips untuk membantu menemukan dan menghilangkan bug, seperti cobalah untuk menjelaskan kode tersebut kepada seseorang, coba untuk mengisolasi masalahnya, jika bug muncul baru-baru ini dan tidak muncul sebelumnya, analisislah semua perubahan yang telah dilakukan pada kode, beristirahatlah dan tetap optimis.
'''

'''
2.	User Input
Terdapat fungsi baru yang merupakan cerminan dari fungsi lama yang sudah bagus, print(). print() mengirim data ke konsol dan fungsi baru mengambil data dari situ. print() tidak menghasilkan hasil yang bermanfaat. Fungsi baru ini merupakan fungsi yang berguna untuk mengambalikan hasil yang bermanfaat. Fungsi baru ini bernama input().
Fungsi ini mampu membaca data yang dimasukkan oleh pengguna dan mengembalikan data yang sama ke program yang sedang berjalan. Program ini dapat memanipulasi data, sehingga kode menjadi benar-benar interaktif. Umumnya semua program membaca dan memproses data, program yang tidak menerima input dari pengguna adalah program yang tuli. Contoh dari penggunaan fungsi input():
'''

print("Masukkan nama Anda : ")
nama = input()
print(f"Halo {nama}")

'''
Fungsi input() dapat meminta input dari pengguna tanpa menggunakan fungsi print(). Sebagai contoh :
'''

nama = input("Masukkan nama Anda :")
print(f"Halo {nama}")

'''
Hasil dari fungsi input() akan selalu berupa string. Jadi hasil tersebut tidak dapat digunakan untuk mencari akar kuadrat dari data, membagi data tersebut, ataupun mengoperasikan segala jenis operasi aritmetika. Sebagai contoh :
'''

angka = input("Masukkan sebuah angka: ")
hasil = angka ** 2.0
print(f"Akar kuadrat dari {angka} adalah {hasil}")

'''
Output dari program dihasilkan akan menghasilkan error sebagai berikut:
Traceback (most recent call last):
File ".main.py", line 4, in <module>
hasil = angka ** 2.0
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'

Baris terakhir menjelaskan bahwa program mencoba menerapkan operator ** pada string dan float. Hal ini dilarang, tetapi terdapat solusi untuk permasalahan ini. Hasil dari input dapat diubah menjadi integer atau float sehingga operasi aritmetika dapat dilakukan. Sebagai contoh :
'''

angka = float(input("Masukkan sebuah angka: "))
hasil = angka ** 2.0
print(f"Akat kuadrat dari {angka} adalah {hasil}")

'''
Dengan mengubah inputan menjadi float atau integer maka operasi aritmetika dapat dilakukan.
String dapat dioperasikan menggunakan operator aritmetika + dan *. Operator + dapat menggabungkan dua string dan menjadi operator concatenator. Sebagai contoh :
'''

fname = input("Masukkan nama depan Anda”")
lname = input("Masukkan nama belakang Anda”")
print("Nama Anda adalah" + fname + " " + lname + ".")

'''
Apabila operator * diopeasikan pada string dan angka akan menjadi operator replication. Fungsi ini akan mereplikasi string sebanyak jumlah yang ditentukan oleh angka. Sebagai contoh :
'''

print("Dafa" * 2)

'''
Output yang dihasilkan pada program tersebut adalah DafaDafa.
'''

'''
Sumber : dicoding.com
1.	Try Exception
Saat membuat sebuah program, seringkali menemukan setidaknya dua jenis kesalahan berdasarkan kejadiannya yaitu kesalahan sintaks (syntax errors) atau sering disebut juga sebagai kesalahan penguraian (parsing errors) dan pengecualian (exceptions) atau sering disebut juga sebagai kesalahan saat beroperasi (runtime errors).
Kesalahan sintaks (syntax errors) adalah jenis kesalahan yang terjadi ketika Python tidak mengerti suatu perintah. Ini mengakibatkan pesan kesalahan muncul sebelum program tersebut berjalan. Salah satu kesalahan yang sering terjadi adalah kesalahan indentasi (IndentationError), sebagai contoh :
'''

'''
if 9>10:
print("Hello World")
'''

'''
Output : 
File "/home/glot/main.py", line 2
    print("Hello World!")
    ^
IndentationError: expected an indented block
	Program akan memunculkan pesan error “IndentationError” karena seharusnya terdapat indentasi sebelum sintaks “print()”. Perhatikan bahwa secara langsung Python menunjukkan baris indentasi dengan memberi tanda panah ke atas atau dikenal dengan caret “^”.
	Pengecualian (exceptions) adalah kesalahan yang terjadi ketika Python mengerti suatu perintah, tetapi mendapatkan masalah saat mengikutinya. Umunya, pengecualian bisa terjadi ketika aplikasi sudah mulai beroperasi. Jenis kesalahan ini paling sering ditemui ketika membuat kode program yang kompleks. Meskipun kode atau ekspresi dari Python yang ditulis sudah benar, ada kemungkinan terjadi kesalahan ketika perintah tersebut dieksekusi. Sebagai contoh :
'''

bukan_angka = "1"
bukan_angka + 2

'''
Output :
Traceback (most recent call last):
  File "/home/glot/main.py", line 2, in <module>
    bukan_angka + 2
TypeError: can only concatenate str (not "int") to str
	Program memunculkan kesalahan karena variabel “bukan_angka” termasuk tipe data string. Di sisi lain, program berusaha melakukan operasi aritmetika yang mengharuskan kedua variabel atau operan bertipe data integer. Pesan tipe kesalahan yang dimunculkan adalah TypeError dengan keterangan atau pesan detailnya adalah "can only concatenate str (not "int") to str".
	Program Python yang  dibangun dapat dilengkapi penanganan terhadap pengecualian dari tipe kesalahan yang ditentukan. Konsep ini dikenal dengan exceptions handling yang menggunakan pernyataan try-except untuk menangani pengecualian tersebut. Sebagai contoh:
'''
	
z = 0
print(1/z)

'''
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 2, in <module>
    print(1/z)
ZeroDivisionError: division by zero
	 Program memunculkan error karena melakukan operasi aritmetika pembagian dengan nilai nol. Kita tahu bahwa pembagian dengan nilai nol tidak bisa dilakukan karena tidak terdefinisikan (undefined). Perhatikan bahwa tipe pengecualian yang terjadi adalah "ZeroDivisionError". Kita bisa lakukan penanganan terhadap pengecualian tersebut dengan menggunakan pernyataan try-except.
'''
	 
z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.")

'''
Output:
Anda tidak bisa membagi angka dengan nilai nol.
	 Program akan menjalankan try statement terlebih dahulu dengan mengeksekusi sintaks "print(1/z)". Kita tahu bahwa program tersebut akan mengalami error "ZeroDivisionError". Alih-alih program menampilkan pesan "ZeroDivisionError: division by zero", kita ingin program menampilkan teks "Anda tidak bisa membagi angka dengan nilai nol.” Kita simpan pernyataan "ZeroDivisionError" setelah except statement. Dengan begini, kita memerintahkan program untuk mengeksekusi kode dalam except jika pengecualian "ZeroDivisionError" terjadi. Kode dalam except tersebut menampilkan pesan "Anda tidak bisa membagi angka dengan nilai nol."
	Jika sebelumnya kita menangani kesalahan yang tidak disengaja, kali ini kita akan mempelajari cara menangani kesalahan yang disengaja. Umumnya, ketika membuat kode program kita ingin membatasi program tersebut dengan kondisi tertentu. Perlu diingat bahwa umumnya, raise digunakan bersamaan dengan if-else statement.
	Misalnya, Anda ingin membuat kode program untuk menampilkan angka dari 1 hingga 10 berdasarkan input atau masukan pengguna. Namun, dalam program tersebut kita ingin mengontrol dengan cara berikut: jika user memberikan input berupa bilangan negatif, program akan memunculkan pesan error dengan keterangan "Bilangan negatif tidak diperbolehkan". Asumsikan user memasukkan input berupa bilangan “-1”.
'''

var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)

'''
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 3, in <module>
    raise ValueError("Bilangan negatif tidak diperbolehkan")
ValueError: Bilangan negatif tidak diperbolehkan
	Pada contoh di atas, kita menggunakan percabangan untuk melakukan evaluasi jika nilai variabel "var" adalah bilangan negatif (kurang dari 0), program akan menampilkan error dengan teks "Bilangan negatif tidak diperbolehkan". Selain itu, program akan mengeksekusi else statement jika nilai dari variabel "var" bukanlah bilangan negatif (lebih besar atau sama dengan 0).
'''

'''	
2.	User Input
Untuk memungkinkan pengguna memberikan masukan, dapat menggunakan perintah input(). Sebagai contoh :
'''

nama = input("Masukkan nama Anda: ")

'''
	Ketika kode dijalankan, program akan meminta pengguna untuk memasukkan nilai. Jika menambahkan fungsi print() pada kode program diatas, maka program akan menampilkan output ke layar, berikut gabungan fungsi input() dan output().
'''

nama = input("Masukkan nama Anda: ")
print(nama)