"""
Nama  : Fani Pratiwi Nur Indah
NIM   : 2225250175
Kelas : 3B
""" 

import math

print("=== KALKULATOR KOORDINAT ===")

x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))

x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))


jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("\n=== HASIL ===")
print("Titik pertama :", f"({x1}, {y1})")
print("Titik kedua   :", f"({x2}, {y2})")
print("Jarak kedua titik =", jarak)