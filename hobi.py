nama = raw_input("Masukkan nama Anda : ")
umur = input("Masukkan umur Anda : ")
hobi = []
stop = False

while not stop:
    print "=" * 15
    hobi_baru = raw_input("Masukkan hobi Anda : ")
    hobi.append(hobi_baru)

    tanya = raw_input("Tambah hobi lagi? (Y/t) : ")
    if tanya == "t":
        stop = True

print "=" * 15
print "Nama :",nama
print "Umur :",umur
print "Hobi :",hobi
