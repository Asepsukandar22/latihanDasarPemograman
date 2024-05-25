import modulbiodata
biodata = modulbiodata.ambilBiodata()
riwayatpendidikan = modulbiodata.ambilpendidikan()

getbiodata = modulbiodata.getBiodata("asep sukandar","TI2023B")
getriwayatpendidikan = modulbiodata.getPendidikan("SDN NEGLASARI","SMPN 1 CIKAKAK","SMK DOA BANGSA")

print(biodata)
print(riwayatpendidikan)
print("==================================")
print(getbiodata)
print(getriwayatpendidikan)
