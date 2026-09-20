daftar_buku = ["audit", "tata kelola", "si kancil", "si kancil dan buaya", "si kancil dan harimau", "si kancil dan gajah"]

print("===LIST BUKU===")
print ("0", daftar_buku[0])
print ("1", daftar_buku[1])
print ("2", daftar_buku[2])
print ("3", daftar_buku[3])
print ("4", daftar_buku[4])

nama = input ("masukkan nama: ")
umur = int(input("masukkan umur: "))
status_aktif = input("apakah kamu mahasswa aktif? (iya/tidak): ") == "iya"

pilihan1 = int(input("pilih buku ke 1 :"))
pilihan2 = int(input("pilih buku ke 2 :"))

syarat_umur = status_aktif and umur>=17

hari_sekarang =0
lama_pinjam =4
batas_pengembalian = hari_sekarang + lama_pinjam

print ("\n===hasil pinjaman===")
if not syarat_umur:
    print (f"maaf{nama}, peminjaman di tolak.")
    if not status_aktif:
        print ("anda bukan mahasiswa aktif")
else:
    buku_dipinjam =[daftar_buku[pilihan1]]
    print (f" selamat{nama}, peminjaman berhasil")
    print (" buku yang dipinjam: ", buku_dipinjam)
    print (" batas pengembalian: ", {batas_pengembalian})
     