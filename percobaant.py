class Contact:
    def __init__(self, nama, nomor_telpon, email):
        self.nama = nama
        self.nomor_telpon = nomor_telpon
        self.email = email

    def tampilkan_info(self):
        print(f"nama: {self.nama}")
        print(f"nomor telpon: {self.nomor_telpon}")
        print(f"email: {self.email}")
        print()

class AddressBook:
    def __init__(self):
        self.daftar_kontak = []

    def tambah_kontak(self, kontak):  # Perbaiki typo di sini, dari 'tamnbah_kontak' ke 'tambah_kontak'
        self.daftar_kontak.append(kontak)  # Perbaiki typo di sini, dari 'apppend' ke 'append'

    def tampilkan_semua_kontak(self):
        print("Daftar kontak:")
        for kontak in self.daftar_kontak:
            kontak.tampilkan_info()

if __name__ == "__main__":
    address_book = AddressBook()

    while True:
        print("Menu:")
        print("1. Tambah kontak")
        print("2. Tampilkan semua kontak")
        print("3. Keluar")

        pilihan = input("Pilih menu 1/2/3: ")

        if pilihan == "1":
            nama = input("Nama: ")
            nomor_telpon = input("Nomor telpon: ")
            email = input("Email: ")
            kontak_baru = Contact(nama, nomor_telpon, email)
            address_book.tambah_kontak(kontak_baru)
        elif pilihan == "2":
            address_book.tampilkan_semua_kontak()
        elif pilihan == "3":
            break  # Keluar dari loop
        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia")
