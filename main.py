# main.py
from proses import *

def menu():
    while True:
        print("\n====== HANARI BAKERY SYSTEM ======")
        print("1. Tambah Produk")
        print("2. Tampilkan Semua Produk")
        print("3. Kalkulator Estimasi Profit")
        print("4. Simulasi Produksi")
        print("0. Keluar")

        pilih = input("Pilih menu: ")
        if pilih == "1": tambah_produk()
        elif pilih == "2": tampilkan_produk()
        elif pilih == "3": kalkulator_profit()
        elif pilih == "4": simulasi_produksi()
        elif pilih == "0": print("Terima kasih!"); break
        else: print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
