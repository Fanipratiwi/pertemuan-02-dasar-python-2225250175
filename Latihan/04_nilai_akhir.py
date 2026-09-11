

print("=== PROGRAM NILAI AKHIR ===")

nama = input("Fani Pratiwi Nur Indah       : ")
nim = input("2225250175        : ")

tugas = float(input("Masukkan nilai tugas : "))
uts = float(input("Masukkan nilai UTS   : "))
uas = float(input("Masukkan nilai UAS   : "))


nilai_akhir = (tugas * 0.20) + (uts * 0.30) + (uas * 0.50)


if nilai_akhir >= 85:
    nilai_huruf = "A"
elif nilai_akhir >= 70:
    nilai_huruf = "B"
elif nilai_akhir >= 60:
    nilai_huruf = "C"
elif nilai_akhir >= 50:
    nilai_huruf = "D"
else:
    nilai_huruf = "E"

print("\n=== HASIL NILAI ===")
print("Nama        :", nama)
print("NIM         :", nim)
print("Nilai Akhir :", nilai_akhir)
print("Nilai Huruf :", nilai_huruf)