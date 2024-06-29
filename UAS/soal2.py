# Get the book name, borrower's name, and loan duration from the user
book_name = input("Masukkan nama buku: ")
borrower_name = input("Masukkan nama peminjam: ")
loan_duration = int(input("Masukkan jumlah hari peminjaman: "))

# Print the loan details
print("\nDetail Peminjaman Buku:")
print(f"Nama Buku: {book_name}")
print(f"Nama Peminjam: {borrower_name}")
print(f"Jumlah Hari Peminjaman: {loan_duration} hari")

# Print the loan schedule
for i in range(1, loan_duration + 1):
  print(f"Hari ke {i} : {book_name}, {borrower_name}")




