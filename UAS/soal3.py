namabuku3 = input("Masukkan nama buku: ")
peminjam3 = input("Masukkan nama peminjam: ")
durasi3 = int(input("Masukkan jumlah hari peminjaman: "))

print("=======================================")
print("=============SOAcd L NO.3==================")
print("\nDetail Peminjaman Buku:")
print(f"Nama Buku: {namabuku3}")
print(f"Nama Peminjam: {peminjam3}")
print(f"Jumlah Hari Peminjaman: {durasi3} hari")

for i in range(1, durasi3 + 1):
  print(f"Hari ke {i} : {namabuku3}, {peminjam3}")

if durasi3 > 7:
    print("Anda Dikenai Denda")
else:
    print("Anda dalam masa tenggang")
print("==================================")
print("==================================")
print("==================================")
    


namabuku4 = input("Masukkan nama buku: ")
peminjam4 = input("Masukkan nama peminjam: ")
durasi4 = int(input("Masukkan jumlah hari peminjaman: "))


print("=======================================")
print("\n=============SOAL NO.4==================")
print("\nDetail Peminjaman Buku:")
print(f"Nama Buku: {namabuku4}")
print(f"Nama Peminjam: {peminjam4}")
print(f"Jumlah Hari Peminjaman: {durasi4} hari")

for i in range(1, durasi4 + 1):
  print(f"Hari ke {i} : {namabuku4}, {peminjam4}")

def cekdenda(jumlah_hari):
  if jumlah_hari > 7:
    print("Anda Dikenai Denda")
  else:
    print("Anda dalam masa tenggang")

cekdenda(durasi4)
print("==================================")
print("==================================")
print("==================================")