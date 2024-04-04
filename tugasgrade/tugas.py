nama = input("Masukkan Nama anda: ")
kelas = input("Masukkan Kelas anda: ")
score = int(input("Masukkan skor anda: "))

if score >= 90 and score <= 100:
    grade = 'A'
    predikat = 'Dengan Pujian'
elif score >= 80:
    grade = 'B'
    predikat = 'Sangat Memuaskan'
elif score >= 70:
    grade = 'C'
    predikat = 'Memuaskan'
elif score >= 60:
    grade = 'D'
    predikat = 'Tidak Memuaskan'
elif score >= 50:
    grade = 'E'
    predikat = 'Tidak LULUS'
else:
    grade = 'E'
    predikat = 'Tidak LULUS'
print("========Pengolahan Nilai Dan Grade=========")
print(f'Nama Kamu: {nama}\nKelas Kamu: {kelas}\nSkor: {score}\nNilai Huruf: {grade}\nPredikat: {predikat}')