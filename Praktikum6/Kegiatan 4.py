Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Putra Weka Pratama'
>>> NIM = 175
>>> Tinggi = 1.63
>>> Berat = 50
>>> TahunLahir = 1999
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # karena data dari 'Aku' ditulis dalam tanda kurung
>>> Aku[0]
1999
>>> # karena objek pertama didalam data 'Aku' adalah 'TahunLahir', jadi nilai dari 'TahunLahir' adalah 1999
>>> a = NIM % 4; Aku[a]
175
>>> # karena sisa hasil bagi dari 175 dibagi 4 adalah 3, jadi hasil dari Aku[3] adalah 175
>>> type(Aku[a])
<class 'int'>
>>> # karena hasil dari 'NIM' adalah 3 dan 3 merupakan tipe data integer
>>> Aku[a:4]
(175,)
>>> # menampilkan elemen dari tuple Aku mulai dari indeks ke-3 hingga sebelum indeks ke-4 yang berarti hanya berisi NIM saja
>>> type(Aku[4])
<class 'str'>
>>> # elemen tuple Aku indeks ke-4 merupakan data string karena berisi Nama
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # terjadi tipe eror karena data tipe tuple tidak dapat diubah sedangkan program ingin mengubah elemen tuple indeks ke-0 dari TanggalLahir menjadi 'ok' maka terjadi tipe error
>>> type(Data)
<class 'list'>
>>> # variabel Data merupakan tipe list karena berisi sekumpulan data atau karakter dan data dalam list dapat diubah
>>> type(Data[4])
<class 'str'>
>>> # elemen list indeks ke-4 atau yang berisi Nama merupakan data yang bertipe string karena mengandung karakter
>>> Data[4][5]
' '
>>> # elemen list indeks ke-4 atau yang berisi Nama kemudian program akan menjadi Nama[5] atau indeks ke-5 dari data yang telah disimpan dalam variabel Nama yaitu spasi
>>> Data[4][a:6]
'ra '
>>> # elemen list Data indeks ke-4 yang berisi Nama kemudian program akan menjadi Nama[a:6] dimana a berisi data 0 maka akan menjadi Nama[0:6] yang akan meampilkan elemen list indeks ke-0 hingga sebelum indeks ke-6 yaitu ra
>>> Data[0] = 'ok'; Data
['ok', 50, 1.63, 175, 'Putra Weka Pratama']
>>> # elemen list Data indeks ke-0 diubah dari TanggalLahir menjadi 'ok' dan kemudian program menampilkan data dari list Data
>>> Data[-a]
1.63
>>> # variabel a berisi data 0 maka program menjadi Data[-0] yang akan menampilkan elemen list Data indeks ke-2
>>> range(a)
range(0, 3)
>>> # varibel a berisi data 0 maka program akan menjadi range(3) dan program akan menampilkan range dari 0 hingga 3 atau jika ditulis dalam program range(0, 3)
>>> 
