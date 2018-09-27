kota = ["Malang", "Surabaya", "Jombang", "Pasuruan", "Yogyakarta"]

# Menampilkan isi ke-index
print("Kota index ke-0 adalah : {} " . format(kota[0]))

# Menampilkan seluruh isi list
print("-\nMenampilkan list :")
print kota

# Menambah data di list
## Di belakang
print("-\nMenambah list di belakang :")
kota.append("Pekanbaru")
print kota

## Di depan
print("-\nMenambah list di depan :")
kota.insert(0,"Banjarmasin")
print kota

## Di index tertentu
print("-\nMenambah list di index tertentu :")
kota.insert(4,"Solo")
print kota

# Menghapus data di list
## di index tertentu
print "-\nMenghapus data di index tertentu :"
del kota[4]
print kota

## data tertentu
print "-\nMenghapus data tertentu :"
kota.remove("Pekanbaru")
print kota