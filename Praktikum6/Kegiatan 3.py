Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Putra Weka Pratama'
>>> NIM = 'L200190175'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # karena data 'X' telah berubah menjadi tipe data integer
>>> type(b)
<class 'int'>
>>> # karena data 'Nama' memiliki instruksi 'len' yang mana 'len' adalah jumlah anggota dari suatu objek
>>> a / b
65.27777777777777
>>> # karena hasil dari 1175 dibagi 18 adalah 65.27777777777777 dan merupakan bilangan float
>>> a // b
65
>>> # karena arti dari '//' adalah pembagian dengan pembulatan ke bawah
>>> 10 * (a - 999)
1760
>>> # merupakan data bertipe integer, karena data dari variabel a dikurang 999 adalah 176 dan kemudian dikalikan 10 menghasilkan data 1760
>>> b ** 2
324
>>> # karena data dari variabel b dipangkatkan 2 atau 18 pangkat 2 yang hasilnya 324
>>> a % b
5
>>> # karena arti dari '%" adalah sisa hasil bagi yang mana data variabel a dibagi data variabel b dari 1175 dibagi 18 yaitu 5
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # data 12.5 disimpan dalam variabel c dan merupakan nilai desimal
>>> a / c
94.0
>>> # karena hasil dari 1175 dibagi 12.5 adalah 94.0 dan merupakan bilangan float atau bernilai desimal
>>> a // c
94.0
>>> # karena arti dari '//' adalah pembagian dengan pembulatan ke bawah
>>> a % c
0.0
>>> # karena arti dari '%' adalah sisa hasil bagi yang mana data variabel a dibagi data variabel c dari 1175 dibagi 12.5 yaitu 0.0
>>> c > b
False
>>> # merupakan data yang bertipe boolean yang bernilai atau berkondisi False karena data variabel c (12.5) lebih kecil dari data variabel b (18) sedangkan dalam program ditulis data variabel c lebih besar daripada data variabel b maka menghasilkan kondisi atau nilai False
>>> type(c > b)
<class 'bool'>
>>> # merupakan data yang bertipe boolean yang memiliki 2 kondisi atau nilai yaitu True dan False yang mana merupakan operator logika
>>> a > b and b > c
True
>>> # karena a > b bernilai True dan b > c bernilai True juga, dalam operator 'and' apabila kedua data memiliki nilai True maka menghasilkan data bernilai True
>>> a > 1100 or b < 10
True
>>> # karena a > 1100 bernilai True dan b < 10 bernilai False, dalam operator 'or' apabila salah satu memiliki nilai True maka menghasilkan data bernilai True juga
>>> 
