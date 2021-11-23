import rumus

daftar_kontak = []

while True:
    print("====DAFTAR MENU====")
    print("|1. Daftar Kontak |")
    print("|2. Cari Kontak   |")
    print("|3. Tambah Kontak |")
    print("|4. Hapus Kontak  |")
    print("|5. Keluar Program|")
    print("===================")
    pilih = input("Silakan Pilih Menu: ")

    if pilih == "5":
        break
    elif pilih == "1":
        rumus.tampil(daftar_kontak)
    elif pilih == "2":
        rumus.cari(daftar_kontak)
    elif pilih == "3":
        kontak = rumus.kontak_baru()
        daftar_kontak.append(kontak)
    elif pilih == "4":
        rumus.hapus(daftar_kontak)
    else:
        print(10*"=")
        print("Menu Tidak Tersedia!")

print("Anda Keluar Dari Program! \nSampai Jumpa Lagi! <3")
