#Studi kasus cek grade kelulusan dari nilai yang diinputkan
#Grade Lulus : A, B+, B, C+, C
#Grade Tidak Lulus : D, E

nilai = input("Masukkan Nilai : ")

#Cek grade
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B+"
elif nilai >= 70:
    grade = "B"
elif nilai >= 60:
    grade = "C+"
elif nilai >= 50:
    grade = "C"
elif nilai >= 40:
    grade = "D"
else :
    grade = "E"

#cek kelulusan
if grade=="A" or grade=="B+" or grade=="B" or grade=="C+" or grade=="C":
    status = "Lulus"
else:
    status = "Tidak Lulus"

print("Grade : %s" % grade)
print("Status : %s" % status)