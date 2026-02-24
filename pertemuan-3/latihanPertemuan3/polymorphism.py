class Notifikasi:
    def kirim(self):
        return "Mengirim notifikasi"
    
class Email(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui Email"
    
class SMS(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui SMS"

daftar_notifikasi = [Email(), SMS()]

for notif in daftar_notifikasi:
    print(notif.kirim())