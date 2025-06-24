# proses.py
from produkroti import *

produk_list = []

def tambah_produk():
    print("\n-- Tambah Produk --")
    nama = input("Nama produk: ")
    kode = input("Kode produk: ")
    jenis = input("Jenis produk (roti manis / croissant / butter cookies / muffin): ").lower()
    bahan = {}
    while True:
        bhn = input("Nama bahan (ketik 'done' jika selesai): ")
        if bhn == "done": break
        jumlah = input(f"Jumlah {bhn}: ")
        bahan[bhn] = jumlah
    biaya = int(input("Biaya produksi untuk 100 pcs: "))
    harga = int(input("Harga jual untuk 100 pcs: "))

    produk = None
    if jenis == "roti manis":
        produk = RotiManis(nama, kode, bahan, biaya, harga)
    elif jenis == "croissant":
        produk = Croissant(nama, kode, bahan, biaya, harga)
    elif jenis == "butter cookies":
        produk = ButterCookies(nama, kode, bahan, biaya, harga)
    elif jenis == "muffin":
        produk = Muffin(nama, kode, bahan, biaya, harga)
    else:
        print("Jenis tidak dikenali.")
        return

    produk_list.append(produk)
    print("Produk berhasil ditambahkan!")

def tampilkan_produk():
    if not produk_list:
        print("Belum ada produk.")
    for p in produk_list:
        p.tampil_info()

def kalkulator_profit():
    kode = input("\nMasukkan kode produk untuk estimasi: ")
    jumlah = int(input("Jumlah pcs yang akan diproduksi: "))
    for p in produk_list:
        if p.kode == kode:
            profit = p.hitung_profit(jumlah)
            print(f"Estimasi profit: Rp{profit}")
            return
    print("Produk tidak ditemukan.")

def simulasi_produksi():
    kode = input("\nMasukkan kode produk untuk simulasi: ")
    for p in produk_list:
        if p.kode == kode:
            print("\n-- Simulasi Produksi --")
            p.pengadonan()
            p.pengembangan()
            p.pemanggangan()
            p.topping()
            p.bake()
            p.pack()
            p.label()
            return
    print("Produk tidak ditemukan.")
