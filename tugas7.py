print('Menghitung Gaji')

Nama = input('Masukan Nama:') 
Gaji_pokok = int(input('Masukan Gaji:'))
Tunjangan = (20/100) * Gaji_pokok 
pajak = (15/100) * (Gaji_pokok + Tunjangan)
gaji_bersih = Gaji_pokok + Tunjangan - pajak

print('Nama:', Nama, '\nGajiPokok:', Gaji_pokok, '\nGajibersih:', gaji_bersih)