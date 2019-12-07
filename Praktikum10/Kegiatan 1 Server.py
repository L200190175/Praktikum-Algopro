import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50005))
s.listen(5)
print "Program Komunikasi Tentang Data Diri"
data = ''
kamus = {'nama': 'Putra Weka Pratama',
         'NIM': 'L200190175',
         'angkatan': '2019',
         'keluar': 'Siap!!'}
while data.lower() != 'q':
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower() == 'q':
            s.close()
            break
        print 'Perintah: ', data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, Perintah Tidak Dimengerti!')
