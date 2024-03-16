nama = "ASEP SUKANDAR"
alamat = "Kp. Pasirjati, Cikakak, Sukabumi"

print("Nama Saya",nama)
print("Alamat Saya",alamat)
print("Hurup Pertama Saya",nama[0])
print("Hurup Terakhir Saya",nama[-1])
print("Nama Depan Saya",nama[:4])
print("Nama Terakhir Saya",nama[-8:])

print("=============Split========")
#Spit
alamat_array = alamat.split(', ')
print("Alamat Saya array",alamat_array)
print("Alamat Kampung Saya",alamat_array[0])
print("Alamat Kecamatan Saya",alamat_array[1])
print("Alamat Kabupaten Saya",alamat_array[2])

print("=============Join String========")
#Join String
pemisah = "+"
print("Alamat Kabupaten Saya",pemisah.join(alamat_array))
