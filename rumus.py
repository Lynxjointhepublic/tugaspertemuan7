def tampil(daftar_kontak):
    for kontak in daftar_kontak:
        print(10*"=")
        print(f"Nama: {kontak['nama']}")
        print(f"Email: {kontak['email']}")
        print(f"Alamat: {kontak['alamat']}")

def cari(daftar_kontak):
    cari_nama = input("Masukan Nama Kontak: ")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(cari_nama.lower()) !=-1:
            print(10*"=")
            print(f"Nama: {kontak['nama']}")
            print(f"Email: {kontak['email']}")
            print(f"Alamat: {kontak['alamat']}")

def kontak_baru():
    print(10*"=")
    nama = input("Nama : ")
    email = input("Email : ")
    alamat = input("Alamat : ")
    kontak = {
        "nama" : nama,
        "email" : email,
        "alamat" : alamat
    }
    return kontak

def hapus(daftar_kontak):
    nama = input("Masukan Nama Kontak Yang Akana Di Hapus: ")

    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if nama == kontak["nama"]:
            index = i 
            break

    if index == -1:
        print("Kontak Tidak Di Temukan!")
    else:
        del daftar_kontak[index]
        print("Kontak Berhasil Di Hapus!")
