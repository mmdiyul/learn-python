kota = ["Malang", "Surabaya", "Jombang", "Pasuruan", "Yogyakarta"]

# Menampilkan isi ke-index
print("Kota index ke-0 adalah : {} " . format(kota[0]))

# Menampilkan seluruh isi list
print("\nMenampilkan list")
for list in kota:
    print list

# Menambah data di list
## Di belakang
print("\nMenambah list di belakang")
kota.append("Pekanbaru")
for list in kota:
    print list