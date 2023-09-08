class Vehice:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warma = warna

    def tampilkan_info(self):
        print(f"merk: {self.merk}")
        print(f"tahun: {self.tahun}")
        print(f"warna: {self.warna}")

class Car(Vehice):
    def __init__(self, merk, tahun, warna, model):
        super().__init__(merk, tahun, warna)
        self.model = model

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"model : {self.model}")

if __name__ == "__main__":
    car = Car("Toyota", 2022, "merah", "Camry")

    print("info kendaraan: ")
    car.tampilkan_info()
        