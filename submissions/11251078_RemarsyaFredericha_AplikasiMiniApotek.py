from datetime import datetime 

def tambah_obat(data):
    print("\n====== TAMBAH OBAT ========")

    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Tanggal transaksi otomatis: {tanggal}")
    
    nama = input("Nama obat : ")
    jenis = input("Jenis : ")
    
    while True:
        try:
            harga = int(input("Harga : "))
            break
        except:
            print("Harga harus angka! Coba lagi.")

    while True:
        try:
            jumlah = int(input("Jumlah : "))
            break
        except ValueError:
            print("Jumlah harus angka! Coba lagi.")

    exp = input("Exp : ")

    obat = [
        tanggal,           
        len(data) + 1,    
        nama,              
        jenis,            
        harga,             
        jumlah,            
        exp                
    ]

    data.append(obat)
    print("Obat berhasil ditambahkan!\n")

    return data


def read(data):
    print("\n============= DAFTAR OBAT =============")

    if len(data) == 0:
        print("Belum ada obat!\n")
        return

    print("\n=== Data Obat Tersimpan ===")
    print("No | Tanggal             | ID    | Nama            | Jenis     | Harga       | Jumlah  | Exp")
    print("---------------------------------------------------------------------------------------------------")

    for i, obat in enumerate(data):
        print(
            f"{i+1:<4} | {obat[0]:<19} | {obat[1]:<6} | {obat[2]:<15} | {obat[3]:<10} | Rp{obat[4]:<10} | {obat[5]:<8} | {obat[6]}"
        )

    print()



def search_obat(data):
    print("\n====== PENCARIAN OBAT ======")

    if len(data) == 0:
        print("Belum ada obat!\n")
        return

    key = input("Masukkan kata yang dicari (Nama): ").lower()

    hasil = [obat for obat in data if key in obat[2].lower()]

    if len(hasil) == 0:
        print("\nData yang anda cari tidak ditemukan!\n")
        return

    print("\n=== Hasil Pencarian ===")
    print("No | Tanggal             | ID    | Nama            | Jenis     | Harga       | Jumlah  | Exp")
    print("---------------------------------------------------------------------------------------------------")

    for i, obat in enumerate(hasil):
        print(
            f"{i+1:<4} | {obat[0]:<19} | {obat[1]:<6} | {obat[2]:<15} | {obat[3]:<10} | Rp{obat[4]:<10} | {obat[5]:<8} | {obat[6]}"
        )

    print()



def update(data):
    print("\n========UBAH DATA OBAT==========")

    try:
        id_obat = int(input("Masukkan ID obat yang akan diubah: "))
    except:
        print("ID harus angka! Coba lagi.")
        return data
    
    for obat in data:
        if obat[1] == id_obat:

            print("Data telah ditemukan. Silahkan isi data terbaru.")

            nama_baru = input("Nama baru: ")
            jenis_baru = input("Jenis baru: ")

            while True:
                try:
                    harga_baru = int(input("Harga baru : "))
                    break
                except:
                    print("Harga harus angka! Coba lagi.")

            while True:
                try:
                    jumlah_baru = int(input("Jumlah baru : "))
                    break
                except ValueError:
                    print("Jumlah harus angka! Coba lagi.")

            exp_baru = input("Exp terbaru : ")

            obat[2] = nama_baru
            obat[3] = jenis_baru
            obat[4] = harga_baru
            obat[5] = jumlah_baru
            obat[6] = exp_baru

            print("Data berhasil diubah.\n")
            return data

    print("Data tidak ditemukan.\n")
    return data



def delete(data):
    print("\n========HAPUS DATA OBAT==========")

    try:
        id_obat = int(input("Masukkan ID obat yang akan dihapus: "))
    except:
        print("ID harus angka! Coba lagi.")
        return data
    
    for i, obat in enumerate(data):
        if obat[1] == id_obat:
            del data[i]
            print("Data berhasil dihapus.\n")
            return data
        
    print("Data tidak ditemukan.\n")
    return data



# ========== SORTING OBAT ==========
def sort_by_id(data):
    n = len(data)
    data_sorted = data[:]  

    for i in range(0, n):
        for j in range(0, n - 1):
            if data_sorted[j][1] > data_sorted[j+1][1]:
                temp = data_sorted[j]
                data_sorted[j] = data_sorted[j+1]
                data_sorted[j+1] = temp

    return data_sorted


def sort_by_tanggal(data):
    n = len(data)
    data_sorted = data[:]

    for i in range(0, n):
        for j in range(0, n - 1):
            t1 = datetime.strptime(data_sorted[j][0], "%Y-%m-%d %H:%M:%S")
            t2 = datetime.strptime(data_sorted[j+1][0], "%Y-%m-%d %H:%M:%S")

            if t1 > t2:
                temp = data_sorted[j]
                data_sorted[j] = data_sorted[j+1]
                data_sorted[j+1] = temp

    return data_sorted


def sort_by_nama(data):
    n = len(data)
    data_sorted = data[:]

    for i in range(0, n):
        for j in range(0, n - 1):
            if data_sorted[j][2].lower() > data_sorted[j+1][2].lower():
                temp = data_sorted[j]
                data_sorted[j] = data_sorted[j+1]
                data_sorted[j+1] = temp

    return data_sorted



def menu_sorting(data):
    print("\n======= MENU SORTING =======")
    print("1. Sort berdasarkan ID")
    print("2. Sort berdasarkan Tanggal")
    print("3. Sort berdasarkan Nama")
    print("4. Kembali")

    try:
        pilih = int(input("Pilih menu: "))
    except:
        print("Input harus angka!")
        return data

    if pilih == 1:
        print("\nData telah disortir berdasarkan ID.\n")
        return sort_by_id(data)

    elif pilih == 2:
        print("\nData telah disortir berdasarkan Tanggal.\n")
        return sort_by_tanggal(data)

    elif pilih == 3:
        print("\nData telah disortir berdasarkan Nama.\n")
        return sort_by_nama(data)

    elif pilih == 4:
        return data

    else:
        print("Pilihan tidak ada!")
        return data


def menuUtama():
    print("============================")
    print("===   Mini Apotek Green  ===")
    print("============================")
    print("1. Tambah Obat")
    print("2. Lihat Obat")
    print("3. Edit Obat")
    print("4. Hapus Obat")
    print("5. Keluar")
    print("6. Sorting Obat")
    print("7. Cari Obat")  

    try:
        pilihan = int(input("Masukkan pilihan [1 - 7]: "))
        if 1 <= pilihan <= 7:
            return pilihan
        else:
            print("Pilihan hanya 1 sampai 7.\n")
            return 0
    except:
        print("Input harus angka!\n")
        return 0


data = []   
pilihan = 0

while pilihan != 5:
    pilihan = menuUtama()

    if pilihan == 1:
        data = tambah_obat(data)

    elif pilihan == 2:
        read(data)
        input("Kembali tekan ENTER...")

    elif pilihan == 3:
        data = update(data)

    elif pilihan == 4:
        data = delete(data)

    elif pilihan == 6:
        data = menu_sorting(data)
        print("\nData setelah sorting:\n")
        read(data)
        input("Tekan ENTER untuk kembali...")

    elif pilihan == 7:
        search_obat(data)
        input("Tekan ENTER untuk kembali...")

print("Terima kasih! Silahkan datang kembali.")
