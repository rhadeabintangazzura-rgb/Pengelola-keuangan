import json
import os

DATA_FILE = "data.json"

saldo = 0

def load_data():
    global saldo
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
            saldo = float(data.get("saldo", 0))
        except Exception:
            saldo = 0

def save_data():
    try:
        with open(DATA_FILE, "w") as f:
            json.dump({"saldo": saldo}, f, indent=2)
    except Exception as e:
        print("Gagal menyimpan data:", e)

def tambah_pemasukan():
    global saldo
    try:
        jumlah = input("Masukkan jumlah pemasukan: ")
        jumlah = float(jumlah)
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return

    saldo += jumlah
    save_data()
    print("Pemasukan berhasil ditambahkan.")
    print(f"Saldo sekarang: {saldo}")

def tambah_pengeluaran():
    global saldo
    try:
        jumlah = input("Masukkan jumlah pengeluaran: ")
        jumlah = float(jumlah)
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return

    if jumlah <= 0:
        print("Jumlah harus lebih dari 0.")
        return

    if jumlah > saldo:
        print("Saldo tidak cukup.")
        return

    saldo -= jumlah
    save_data()
    print("Pengeluaran berhasil dikurangi.")
    print(f"Saldo sekarang: {saldo}")

def lihat_saldo():
    global saldo
    print("=== Saldo Saat Ini ===")
    print(f"Saldo sekarang: Rp{saldo:,.2f}")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

load_data()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        save_data()
        print("Terima kasih! Data disimpan.")
        break
    else:
        print("Pilihan tidak valid")