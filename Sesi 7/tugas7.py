def hitung_luas_segitiga():
  """Fungsi untuk menghitung luas segitiga."""
  alas = float(input("Masukkan alas segitiga: "))
  tinggi = float(input("Masukkan tinggi segitiga: "))
  luas = 0.5 * alas * tinggi
  print(f"Luas segitiga: {luas}")

def hitung_luas_persegi_panjang():
  """Fungsi untuk menghitung luas persegi panjang."""
  panjang = float(input("Masukkan panjang persegi panjang: "))
  lebar = float(input("Masukkan lebar persegi panjang: "))
  luas = panjang * lebar
  print(f"Luas persegi panjang: {luas}")

def tentukan_ganjil_genap():
  """Fungsi untuk menentukan angka ganjil atau genap."""
  angka = int(input("Masukkan angka: "))
  if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap.")
  else:
    print(f"{angka} adalah bilangan ganjil.")

def main():
  """Fungsi utama untuk menjalankan program."""
  while True:
    print("\nMenu:")
    print("1. Hitung luas segitiga")
    print("2. Hitung luas persegi panjang")
    print("3. Menentukan angka ganjil dan genap")
    print("4. Quit")

    pilihan = input("Masukkan pilihan Anda (1-4): ")

    if pilihan == "1":
      hitung_luas_segitiga()
    elif pilihan == "2":
      hitung_luas_persegi_panjang()
    elif pilihan == "3":
      tentukan_ganjil_genap()
    elif pilihan == "4":
      break
    else:
      print("Pilihan tidak valid. Silakan masukkan angka 1-4.")

