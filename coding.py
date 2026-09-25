nama = input("masukkkan nama: ")
umur = int(input("masukkan umur: "))
angka_favorite = int(input("masukkan angka favorite: "))
tinggi_badan = float(input("masukkan tinggi badan (cm): "))

print("\n=== DATA DIRI ===")
print("nama: ", nama)
print("umur: ", umur)
print("angka favorite: ", angka_favorite)
print("tinggi badan: ", tinggi_badan)

harga_pensil = 2000
harga_buku = 5000

total_pensil = 4 * harga_pensil
total_buku =2 * harga_buku
total = total_pensil + total_buku

print("\n=== belanja alat tulis ===")
print("4 pensil", total_pensil )
print("2 buku", total_buku)
print("total harga =", total)

print("\n=== angka favorite ===")
if angka_favorite % 2 == 0:
    print("angka_genap")
else:
    print("angka_ganjil")







