print('umur')

umur = int(input('Masukan umur:'))
if umur <= 10:
    print('Anda anak-anak')
elif umur <= 18:
    print('Anda Remaja')
elif umur <= 35:
    print('Anda Dewasa')
elif umur <= 65:
    print('Parubaya')
else:
    print('Tua')