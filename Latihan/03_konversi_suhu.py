

print("=== KONVERSI SUHU ===")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")
print("3. Celsius ke Kelvin")
print("4. Kelvin ke Celsius")

pilihan = input("Pilih konversi (1-4): ")
suhu = float(input("Masukkan suhu: "))

if pilihan == "1":
    hasil = (suhu * 9/5) + 32
    print("Hasil:", hasil, "°F")

elif pilihan == "2":
    hasil = (suhu - 32) * 5/9
    print("Hasil:", hasil, "°C")

elif pilihan == "3":
    hasil = suhu + 273.15
    print("Hasil:", hasil, "K")

elif pilihan == "4":
    hasil = suhu - 273.15
    print("Hasil:", hasil, "°C")

else:
    print("Pilihan tidak tersedia.")