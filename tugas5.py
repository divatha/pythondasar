print("SEGITIGA BINTANG SIKU")
x = int(input("\nMasukkan baris: "))
print()

for i in range (x):
    for j in range (i+1):
        print('*', end='')
    print()