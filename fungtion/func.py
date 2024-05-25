#function deskriptif
def ambilBiodata():
  nama= "asep sukandar"
  kelas = "TI2023B"
  return "Nama saya :"+nama+ "Kelas saya"+kelas

def ambilpendidikan():
  sd = "SDN NEGLASARI"
  smp = "SMPN 1 CIKAKAK"
  smk = "SMK DOA BANGSA"
  return "sd saya :"+sd + "smp saya "+smp + "smk saya "+smk

#function simple
def getBiodata(nama,kelas):
    return "Nama saya :"+nama+ "Kelas saya"+kelas
def getPendidikan(sd,smp,smk):
    return "sd saya :"+sd + "smp saya "+smp + "smk saya" +smk


biodata = ambilBiodata()
riwayatpendidikan = ambilpendidikan()
print(biodata)
print(riwayatpendidikan)
print("==================================")
getbiodata = getBiodata("asep sukandar","TI2023B")
getriwayatpendidikan = getPendidikan("SDN NEGLASARI","SMPN 1 CIKAKAK","SMK DOA BANGSA")
print(getbiodata)
print(getriwayatpendidikan)