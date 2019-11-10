## Program Akun
## Dibuat oleh Putra L200190175
import random
angka = random.randint(0,1000)

Nama = 'Putra Weka Pratama'
TanggalLahir = '04 Agustus 1999'
NamaSingkat = Nama[0] + '.' + Nama[6] + '.' + Nama[11:18]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[11:15]
Password = Nama[0:3] + str(angka)
