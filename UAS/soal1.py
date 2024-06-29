buku1 = input("Masukkan nama buku: ")
nama_peminjam1 = input("Masukkan nama peminjam: ")
durasi1 = int(input("Masukkan jumlah hari peminjaman: "))

print("=======================================")
print("=============SOAL NO.1==================")
print("\nDetail Peminjaman Buku:")
print(f"Nama Buku: {buku1}")
print(f"Nama Peminjam: {nama_peminjam1}")
print(f"Jumlah Hari Peminjaman: {durasi1} hari")
print("==================================")
print("==================================")
print("==================================")


namabuku2 = input("Masukkan nama buku: ")
peminjam2 = input("Masukkan nama peminjam: ")
durasi2 = int(input("Masukkan jumlah hari peminjaman: "))

print("==================================")
print("=============SOAL NO.2==================")
print("\nDetail Peminjaman Buku:")
print(f"Nama Buku: {namabuku2}")
print(f"Nama Peminjam: {peminjam2}")
print(f"Jumlah Hari Peminjaman: {durasi2} hari")

for i in range(1, durasi2 + 1):
  print(f"Hari ke {i} : {namabuku2}, {peminjam2}")
print("==================================")
print("==================================")
print("==================================")
