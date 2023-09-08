import tkinter as tk
from datetime import datetime

# Dictionary untuk menyimpan data parkir
parking_data = {}

def hitung_biaya(waktu_masuk, waktu_keluar):
    jam_masuk = datetime.strptime(waktu_masuk, '%H:%M')
    jam_keluar = datetime.strptime(waktu_keluar, '%H:%M')
    selisih = jam_keluar - jam_masuk
    biaya = selisih.total_seconds() / 3600 * 2000  # Biaya per jam
    return biaya

def catat_parkir():
    nopol = entry_nopol.get()
    
    waktu_masuk = entry_masuk.get()
    waktu_keluar = entry_keluar.get()
    biaya = hitung_biaya(waktu_masuk, waktu_keluar)

    parking_data[nopol] = {
        'Waktu Masuk': waktu_masuk,
        'Waktu Keluar': waktu_keluar,
        'Biaya Parkir': biaya
    }

    listbox_parkir.insert(tk.END, f"{nopol} - Diam atas: {waktu_masuk} - Biaya: Rp {biaya:.2f}")

root = tk.Tk()
root.title("Program Parkir")

label_nopol = tk.Label(root, text="Nomor Polisi:")
label_nopol.pack()
entry_nopol = tk.Entry(root)
entry_nopol.pack()

label_masuk = tk.Label(root, text="Waktu Masuk (HH:MM):")
label_masuk.pack()
entry_masuk = tk.Entry(root)
entry_masuk.pack()


label_keluar = tk.Label(root, text="Waktu Keluar (HH:MM):")
label_keluar.pack()
entry_keluar = tk.Entry(root)
entry_keluar.pack()

tombol_parkir = tk.Button(root, text="Catat Parkir", command=catat_parkir)
tombol_parkir.pack()


listbox_parkir = tk.Listbox(root)
listbox_parkir.pack()

root.mainloop()