#Asepsukandar
hargamotor = 15000000
bungaperbulan = 0.02
jangkawaktu = 3 *12
cicilanperbulan=(hargamotor * bungaperbulan) / (1 - (1+bungaperbulan)** -jangkawaktu)
print("Cicilan Perbulan : Rp",
      round(cicilanperbulan,2))