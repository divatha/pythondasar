class Contact:
    def __init__(self, nama, nomor_telpon, email):
        self.nama = nama
        self.nomor_telpon = nomor_telpon
        self.email = email

    def tampilkan_info(self):
        print(f"nama: {self.nama}")
        print(f"nomor telpon {self.nomor_telpon}")
        print(f"email: {self.email}")
        print()

class AddressBook:
    def __init__(self):
        self.daftar_kontak = []

    def tambah_kontak(self, kontak):
        self.daftar_kontak.append(kontak)

    def tampilkan_semua_kontak(self):
        print("daftar kontak: ")
        for kontak in self.daftar_kontak:
            kontak.tampilkan_info()
        

if __name__ == "__main__":
    address_book = AddressBook()

    while True:
        print("menu:")
        print("1. Tambah kontak")
        print("2. tampilkan semua kontak")
        print("3. keluar")

        pilihan = input("pilih menu 1\2\3: ")

        if pilihan == "1":
            nama = input("nama: ")
            nomor_telpon = input("nomor telpon : ")
            email = input("email: ")
            kontak_baru = Contact(nama, nomor_telpon, email)
            address_book.tambah_kontak(kontak_baru)
        elif pilihan == "2":
            address_book.tampilkan_semua_kontak()
        elif pilihan == "3":
            break
        
        else: 
            print("pilihan tidak valid, silahkan pilih menu yang tersedia")