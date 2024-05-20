# Inisialisasi list produk
produk = []

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\nPilih Operasi:")
    print("1. List Produk")
    print("2. Tambah Produk")
    print("3. Hapus Produk")
    print("4. Hapus berdasarkan No Produk")
    print("5. Keluar")

# Fungsi untuk menampilkan list produk
def list_produk():
    print("\nDaftar Produk:")
    if not produk:
        print("Belum ada produk.")
    else:
        for i, item in enumerate(produk, 1):
            print(f"{i}. {item}")

# Fungsi untuk menambah produk
def tambah_produk():
    nama_produk = input("Masukkan nama produk: ")
    produk.append(nama_produk)
    print("Produk berhasil ditambahkan.")

# Fungsi untuk menghapus produk
def hapus_produk():
    list_produk()
    if produk:
        index = int(input("Masukkan nomor produk yang ingin dihapus: "))
        if 1 <= index <= len(produk):
            del produk[index - 1]
            print("Produk berhasil dihapus.")
        else:
            print("Nomor produk tidak valid.")
    else:
        print("Tidak ada produk untuk dihapus.")

# Fungsi untuk menghapus produk berdasarkan nomor produk
def hapus_berdasarkan_nomor():
    list_produk()
    if produk:
        nomor_produk = int(input("Masukkan nomor produk yang ingin dihapus: "))
        if 1 <= nomor_produk <= len(produk):
            del produk[nomor_produk - 1]
            print("Produk berhasil dihapus.")
        else:
            print("Nomor produk tidak valid.")
    else:
        print("Tidak ada produk untuk dihapus.")

# Main program
while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '1':
        list_produk()
    elif pilihan == '2':
        tambah_produk()
    elif pilihan == '3':
        hapus_produk()
    elif pilihan == '4':
        hapus_berdasarkan_nomor()
    elif pilihan == '5':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
