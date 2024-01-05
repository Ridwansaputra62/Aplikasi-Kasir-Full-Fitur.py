import time
from datetime import datetime
import os
import getpass

now = datetime.now()
timestruk = now.strftime("%d %B %Y %H:%M:%S")
kodestruk = now.strftime("KSR%d%H%MKEL02")
timelaporanpenjualan = now.strftime("%d %B %Y")

def clear():
    os.system('cls')
clear()

buah = {
    "Apel": [21000,20,0],
    "Anggur": [28000,20,0],
    "Durian": [35000,20,0],
    "Jambu": [15000,20,0],
    "Jeruk": [12000,20,0],
    "Mangga": [18000,20,0],
    "Markisa": [15000,20,0],
    "Pepaya": [10000,20,0],
}
def head():
    print("\n     =======================================")
    print("     |==>    Program Kasir Versi  2.3   <==|")
    print("     |===>          KELOMPOK 2         <===|")
    print("     =======================================")
head()
laporan = {'laporan':[0,0]}
password = '123123'
username = 'kelompok2'

while True:
    print ("\n =============>  SILAHKAN  LOGIN  <=============")
    user = input("\n => Masukan Username : ")
    psw = input(" => Masukan Password : ")
    if user == username and psw == password:
        break
    else:
        clear()
        head()
        print("\n ===============================================")
        print(" |==>   Username dan Password tidak cocok   <==|")
        print(" ===============================================")

clear()
head()

def tabel():
    print("\n\t=================================")
    print("\t|===>    TOKO NUSA FRUIT    <===|")
    print("\t|===============================|")
    print("\t|  Buah          |  Harga     \t|")
    print("\t|-------------------------------|")
    for x in buah:
        print("\t| ", x, "\t "f"|  {buah[x][0]:,}"" /kg\t|")
    print("\t=================================")
tabel()

def transaksi():
    clear()
    totalbayar = 0
    grandtotal = 0
    barang = {}
    diskon = 10/100
    totaldiskon = 0
    
    def popup():
        if totalbayar < 100000:
            print("    =========================================")
            print("    | Belanja Diatas 100rb Dapat Diskon 10% |")
            print("    =========================================\n")
        else:
            print(" ===============================================")
            print(" |==> SELAMAT ! Anda Mendapatkan DISKON 10% <==|")
            print(" ===============================================\n")

    def daftar_belanja():
        if len(barang) == 0:
            #exit untuk keluar dari fungsi transaksi
            exit
        else:
            print("\t=================================")
            print("\t|===>    DAFTAR  BELANJA    <===|")
            print("\t|===============================|")
            print("\t|  Nama Buah\t | Jumlah Beli\t|")
            print("\t|-------------------------------|")
        for x in barang:
            print("\t| ", x, "\t |   ", barang[x][0],"kg\t|")
        if len(barang) == 0:
            exit
        else:
            print("\t=================================\n")

    while True:
        clear()
        print("\n\t    =========================")
        print("\t====|    MENU  TRANSAKSI    |====")
        print("\t    =========================")
        tabel()
        popup()
        daftar_belanja()
        print("   ===========================================")
        print("   |> Ketik Nama Buah Yang Akan Dibeli Atau <|")  
        print("   |> Ketik 'X' Untuk Mengakhiri Belanja    <|")
        print("   ===========================================")
        namabuah = input("\n==>  Masukan Pilihan Anda  : ").title()
        if namabuah not in barang:
            if namabuah in buah:
                clear()
                print("\n\t    =========================")
                print("\t====|    MENU  TRANSAKSI    |====")
                print("\t    =========================")
                tabel()
                popup()
                daftar_belanja()
                while True:
                    print("        =================================")
                    print("        |> Masukan Jumlah Pesanan Anda <|")  
                    print("        =================================")
                    item = input("\n==>  Masukan Pilihan Anda  : ")
                    if item.isdigit():
                        if int(item) > buah[namabuah][1] and buah[namabuah][1] > 0:
                            clear()
                            print("\n\t    =========================")
                            print("\t====|    MENU  TRANSAKSI    |====")
                            print("\t    =========================")
                            tabel()
                            popup()
                            daftar_belanja()
                            print("        =================================")
                            print("        |====> Stok hanya ",buah[namabuah][1],"\tkg <====|")  
                            print("        =================================\n")
                            continue
                        elif int(item) == 0 and buah[namabuah][1] > 0:
                            clear()
                            print("\n\t    =========================")
                            print("\t====|    MENU  TRANSAKSI    |====")
                            print("\t    =========================")
                            tabel()
                            popup()
                            daftar_belanja()
                            print("        =================================")
                            print("        |==> Pembelian Minimal  1 kg <==|")  
                            print("        =================================\n")
                            continue
                        else:
                            break 
                    else:
                        clear()
                        print("\n\t    =========================")
                        print("\t====|    MENU  TRANSAKSI    |====")
                        print("\t    =========================")
                        tabel()
                        popup()
                        print("\t=================================")
                        print("\t==>  Cukup Masukan Angka Cuy  <==")
                        print("\t=================================\n")
                buah[namabuah][1] = buah[namabuah][1] - int(item)
                buah[namabuah][2] = buah[namabuah][2] + int(item)
                harga = buah[namabuah][0]
                bayar = int(item) * harga
                barang.update({namabuah:[item,harga,bayar]})
                totalbayar += bayar
                if totalbayar > 100000:
                    grandtotal = totalbayar - (diskon*totalbayar)
                    totaldiskon = diskon * totalbayar
                else:
                    grandtotal = totalbayar
            elif namabuah == "X":
                break
            else:
                while True:
                    clear()
                    print("\n\t    =========================")
                    print("\t====|    MENU  TRANSAKSI    |====")
                    print("\t    =========================")
                    tabel()
                    popup()
                    daftar_belanja()
                    print("     =======================================")
                    print("     ==>   Buah Tidak Ada Dalam Daftar   <==")
                    print("     =======================================\n")
                    print("   ===========================================")
                    print("   |> Ketik Nama Buah Yang Akan Dibeli Atau <|")  
                    print("   |> Ketik 'X' Untuk Mengakhiri Belanja    <|")
                    print("   ===========================================")
                    namabuah = input("\n==>  Masukan Pilihan Anda  : ").title()
                    if namabuah not in barang:
                        if namabuah in buah:
                            clear()
                            print("\n\t    =========================")
                            print("\t====|    MENU  TRANSAKSI    |====")
                            print("\t    =========================")
                            tabel()
                            popup()
                            daftar_belanja()
                            while True:
                                print("        =================================")
                                print("        |> Masukan Jumlah Pesanan Anda <|")  
                                print("        =================================")
                                item = input("\n==>  Masukan Pilihan Anda  : ")
                                if item.isdigit():
                                    if int(item) > buah[namabuah][1] and buah[namabuah][1] > 0:
                                        clear()
                                        print("\n\t    =========================")
                                        print("\t====|    MENU  TRANSAKSI    |====")
                                        print("\t    =========================")
                                        tabel()
                                        popup()
                                        daftar_belanja()
                                        print("        =================================")
                                        print("        |====> Stok hanya ",buah[namabuah][1],"\tkg <====|")  
                                        print("        =================================\n")
                                        continue
                                    elif int(item) == 0 and buah[namabuah][1] > 0:
                                        clear()
                                        print("\n\t    =========================")
                                        print("\t====|    MENU  TRANSAKSI    |====")
                                        print("\t    =========================")
                                        tabel()
                                        popup()
                                        daftar_belanja()
                                        print("        =================================")
                                        print("        |==> Pembelian Minimal  1 kg <==|")  
                                        print("        =================================\n")
                                        continue
                                    else:
                                        break
                                else:
                                    clear()
                                    print("\n\t    =========================")
                                    print("\t====|    MENU  TRANSAKSI    |====")
                                    print("\t    =========================")
                                    tabel()
                                    popup()
                                    print("\t=================================")
                                    print("\t==>  Cukup Masukan Angka Cuy  <==")
                                    print("\t=================================\n")
                            buah[namabuah][1] -= int(item)
                            buah[namabuah][2] += int(item)
                            harga = buah[namabuah][0]
                            bayar = int(item) * harga
                            barang.update({namabuah:[item,harga,bayar]})
                            totalbayar += bayar
                            if totalbayar > 100000:
                                grandtotal = totalbayar - (diskon*totalbayar)
                                totaldiskon = diskon * totalbayar
                            else:
                                grandtotal = totalbayar
                            break
                        elif namabuah == "X":
                            break
                        else:
                            continue

    laporan["laporan"][0] += grandtotal
    laporan["laporan"][1] += totaldiskon
        
    if len(barang) > 0:
        for x in range(3):
            print("\n ==> Transaksi Sedang Diproses ...")
            time.sleep(0.5)
        clear()
        def struk():
            print("\n\t=========================================================")
            print("\t|=================>  TOKO NUSA FRUIT  <=================|")
            print("\t|=================> DETAIL PEMBAYARAN <=================|")
            print("\t|=======================================================|")
            print("\t|>   NO Transaksi       | {}               <|".format(kodestruk))
            print("\t|>   Nama Kasir         |",username,"\t\t       <|")
            print("\t|>   Tanggal Transaksi  | {}    <|".format(timestruk))
            print("\t|=======================================================|")
            print("\t| BUAH\t\t| PESAN\t| HARGA\t\t| TOTAL\t\t|")
            print("\t|-------------------------------------------------------|")
            for x in barang:
                print ("\t|",x, " \t| ", barang[x][0],"\t| "f"Rp {barang[x][1]:,}"f"\t| Rp {barang[x][2]:,}""\t|")
            print("\t|=======================================================|")
            print(f"\t| Total Belanja\t\t\t\t| Rp {int(totalbayar):,}""\t|")
            if totalbayar > 100000:
                print("\t|-------------------------------------------------------|")
                print(f"\t| Diskon 10 %\t\t\t\t| Rp {int(diskon*totalbayar):,}""\t|")
            print("\t|-------------------------------------------------------|")
            print(f"\t| Total Pembayaran\t\t\t| Rp {int(grandtotal):,}""\t|")
            print("\t|-------------------------------------------------------|")
        struk()
        
        while True:
            uangmasuk = input("\t| Tunai\t\t\t\t\t| Rp ")
            if uangmasuk.isdigit():
                if int(uangmasuk) >= grandtotal:
                    break
                else:
                    print("\n\t\t\t==> Uang Anda Tidak Cukup <==\n")
            else:
                print("\n\t\t\t==> Harap Masukan Angka! <==\n")
        kembalian = int(uangmasuk) - grandtotal
        clear()
        struk()
        print(f"\t| Tunai\t\t\t\t\t| Rp {int(uangmasuk):,}""\t|")
        print("\t|-------------------------------------------------------|")
        print(f"\t| kembalian\t\t\t\t| Rp {int(kembalian):,}""\t|")
        print("\t|=======================================================|")
        print("\t|====================> TERIMAKASIH <====================|")
        print("\t=========================================================\n\n")
        time.sleep(2)
    else:
        clear()
        head()
        tabel()
        print("\n\t=================================")
        print("\t==> Anda belum memilih barang <==")
        print("\t=================================\n")

def stok():
    while True:
        clear()
        def tabel_stok():
            print("\n\t    =========================")
            print("\t====|  MENU EDIT STOK BUAH  |====")
            print("\t    =========================")
            print("\n\t=================================")
            print("\t|===>    LIST TOTAL STOK    <===|")
            print("\t|===============================|")
            print("\t|  Nama Buah     |  Total Stok  |")
            print("\t|-------------------------------|")
            for x in buah:
                print("\t| ", x, "\t "f"|    {buah[x][1]:,}"" kg\t|")
            print("\t=================================\n")
        tabel_stok()
        print("   ===========================================")
        print("   |>  Ketik Nama Buah Yang Akan Diedit /   <|")  
        print("   |>  Ketik 'X' Untuk Kembali              <|")
        print("   ===========================================")
        editstok1 = input("\n==> Masukan pilihan anda  : ").title()
        if editstok1 in buah:
            clear()
            tabel_stok()
            print("        =================================")
            print("        |>   Masukan Total Stok Baru   <|")  
            print("        =================================")
            while True:
                stok_baru = input("\n==>  Masukan Pilihan Anda  : ")
                if stok_baru.isdigit():
                    buah[editstok1][1] = int(stok_baru)
                    tabel_stok()
                    break
                else:
                    clear()
                    tabel_stok()
                    print("\t=================================")
                    print("\t==>  Cukup Masukan Angka Cuy  <==")
                    print("\t=================================")
            
        elif editstok1 == 'X':
            clear()
            head()
            tabel()
            break
        else:
            while True:
                clear()
                tabel_stok()
                print("\t=================================")
                print("\t==> Nama Buah Tidak Tersedia  <==")
                print("\t=================================\n")
                print("   ===========================================")
                print("   |>  Ketik Nama Buah Yang Akan Diedit /   <|")  
                print("   |>  Ketik 'X' Untuk Kembali              <|")
                print("   ===========================================")
                editstok1 = input("\n==> Masukan pilihan anda  : ").title()
                if editstok1 in buah:
                    clear()
                    tabel_stok()
                    print("        =================================")
                    print("        |> Masukan Total Stok Terbaru  <|")  
                    print("        =================================")
                    while True:
                        stok_baru = input("\n==>  Masukan Pilihan Anda  : ")
                        if stok_baru.isdigit():
                            buah[editstok1][1] = int(stok_baru)
                            tabel_stok()
                            break
                        else:
                            clear()
                            tabel_stok()
                            print("\t=================================")
                            print("\t==>  Cukup Masukan Angka Cuy  <==")
                            print("\t=================================")
                    break
                elif editstok1 == 'X':
                    clear()
                    head()
                    tabel()
                    break
                else:
                    continue

def update():
    clear()
    print("\n\t    =========================")
    print("\t====| MENU UPDATE DATA BUAH |====")
    print("\t    =========================")
    tabel()
    while True:
        print("\n   ===========================================")
        print("   |>  Ketik '1' Untuk Menambahkan Data     <|")  
        print("   |>  Ketik '2' Untuk Menghapus Data       <|")
        print("   |>  Ketik '3' Untuk Update Harga         <|")
        print("   |>  Ketik 'X' Untuk Kembali              <|")
        print("   ===========================================")
        pilihan_update = input("\n==> Masukan pilihan anda  : ").title()
        if pilihan_update == '2':
            clear()
            def hapus_tabel():
                print("\n\t    =========================")
                print("\t====| TABEL HAPUS DATA BUAH |====")
                print("\t    =========================")
                tabel()
            hapus_tabel()
            while True:
                print("   ===========================================")
                print("   |>  Ketik Nama Buah Yang Akan Dihapus /  <|")  
                print("   |>  Ketik 'X' Untuk Mengakhiri Delete    <|")
                print("   ===========================================")
                hapus = input("\n==> Masukan pilihan anda  : ").title()
                if hapus in buah:
                    #.pop dibawah adalah atribute dictionari untuk menghapus value data beserta isinya
                    buah.pop(hapus)
                    clear()
                    hapus_tabel()
                elif hapus == 'X':
                    clear()
                    print("\n\t    =========================")
                    print("\t====| MENU UPDATE DATA BUAH |====")
                    print("\t    =========================")
                    tabel()
                    break
                else:
                    clear()
                    hapus_tabel()
                    print("\n\t=================================")
                    print("\t=> BUAH TIDAK ADA DALAM DAFTAR <=")
                    print("\t=================================\n")
        elif pilihan_update == '1':
            clear()
            def update_tabel():
                print("\n\t    =========================")
                print("\t====| MENU TAMBAH DATA BUAH |====")
                print("\t    =========================")
                print("\n\t=================================")
                print("\t|===>   MASUKAN DATA BARU   <===|")
                print("\t|===============================|")
                print("\t|  Buah          |  Harga     \t|")
                print("\t|-------------------------------|")
                for x in buah:
                    print("\t| ", x, "\t "f"|  {buah[x][0]:,}"" /kg\t|")
                print("\t=================================\n")
            update_tabel()
            while True:
                print("   ===========================================")
                print("   |>      Masukan Nama Buah Baru atau      <|")  
                print("   |>   Ketik 'X' Untuk Mengakhiri Update   <|")
                print("   ===========================================")
                buahupdate = input("\n==> Masukan pilihan anda    : ").title()
                if buahupdate == 'X':
                    clear()
                    print("\n\t    =========================")
                    print("\t====| MENU UPDATE DATA BUAH |====")
                    print("\t    =========================")
                    tabel()
                    break
                elif buahupdate not in buah:
                    while True:
                        harga = input("\n==> Masukan harga buah      : ")
                        if harga.isdigit():
                            while True:
                                stok_baru = input("\n==> Masukan Stok buah (kg)  : ")
                                if stok_baru.isdigit():
                                    buah.update({buahupdate:[int(harga),int(stok_baru),0]})
                                    clear()
                                    update_tabel()
                                    break
                                else:
                                    clear()
                                    update_tabel()
                                    print("\t  =============================")
                                    print("\t  ===> Harap masukan angka <===")
                                    print("\t  =============================")
                            break
                        else:
                            clear()
                            update_tabel()
                            print("\t  =============================")
                            print("\t  ===> Harap masukan angka <===")
                            print("\t  =============================")
                else:
                    clear()
                    update_tabel()
                    print("\t  =============================")
                    print("\t  ===> Buah Sudah Tersedia <===")
                    print("\t  =============================\n")
        elif pilihan_update == '3':
            while True:
                clear()
                print("\n\t    =========================")
                print("\t====|   MENU UPDATE HARGA   |====")
                print("\t    =========================")
                tabel()
                print("   ===========================================")
                print("   |>  Ketik Nama Buah Yang Akan diupdate / <|")  
                print("   |>  Ketik 'X' Untuk Mengakhiri Update    <|")
                print("   ===========================================")
                hargaupdate1 = input("\n==> Masukan pilihan anda  : ").title()
                if hargaupdate1 in buah:
                    while True:
                        harga_update = input("\n==> Masukan harga buah    : ")
                        if harga_update.isdigit():
                            buah[hargaupdate1][0] = int(harga_update)
                            break
                        else:
                            clear()
                            print("\n\t    =========================")
                            print("\t====|   MENU UPDATE HARGA   |====")
                            print("\t    =========================")
                            tabel()
                            print("\n\t  =============================")
                            print("\t  ===> Harap masukan angka <===")
                            print("\t  =============================")
                elif hargaupdate1 == 'X':
                    clear()
                    print("\n\t    =========================")
                    print("\t====| MENU UPDATE DATA BUAH |====")
                    print("\t    =========================")
                    tabel()
                    break
                else:
                    while True:
                        clear()
                        print("\n\t    =========================")
                        print("\t====|   MENU UPDATE HARGA   |====")
                        print("\t    =========================")
                        tabel()
                        print("\n\t=================================")
                        print("\t=> BUAH TIDAK ADA DALAM DAFTAR <=")
                        print("\t=================================\n")
                        print("   ===========================================")
                        print("   |>  Ketik Nama Buah Yang Akan diupdate / <|")  
                        print("   |>  Ketik 'X' Untuk Mengakhiri Update    <|")
                        print("   ===========================================")
                        hargaupdate1 = input("\n==> Masukan pilihan anda  : ").title()
                        if hargaupdate1 in buah:
                            while True:
                                harga_update = input("\n==> Masukan harga buah    : ")
                                if harga_update.isdigit():
                                    buah[hargaupdate1][0] = int(harga_update)
                                    break
                                else:
                                    clear()
                                    tabel()
                                    print("\t  =============================")
                                    print("\t  ===> Harap masukan angka <===")
                                    print("\t  =============================")
                            break
                        elif hargaupdate1 == 'X':
                            clear()
                            head()
                            tabel()
                            break
                        else:
                            continue
        elif pilihan_update.upper() == 'X':
            clear()
            head()
            tabel()
            break
        else:
            clear()
            print("\n\t    =========================")
            print("\t====| MENU UPDATE DATA BUAH |====")
            print("\t    =========================")
            tabel()
            print("\n       ===================================")
            print("       ===>   Pilihan tidak trsedia   <===")
            print("       ===================================")

def rekap_penjualan():
    def tabel_rekap():
        clear()
        print("\n\t       ===========================")
        print("\t   ====| MENU  LAPORAN PENJUALAN |====")
        print("\t       ===========================")
        print("=========================================================")
        print("|==============>    LAPORAN PENJUALAN    <==============|")
        print("|=======================================================|")
        print("|>   Nama Toko          : NUSA FRUIT                   <|")
        print("|>   Nama Kasir         :",username,"                   <|")
        print("|>   Tanggal Transaksi  : {}             <|".format(timelaporanpenjualan))
        print("|=======================================================|")
        print("|  BUAH\t\t|   Penjualan\t|  Total Harga\t\t|")
        for x in buah:
            total_rekap = buah[x][0]*buah[x][2]
            print("|-------------------------------------------------------|")
            print("| ", x, "\t|    ", buah[x][2],f"Kg\t|  Rp  {total_rekap:,}""\t\t|")
        print("|-------------------------------------------------------|")
        print("|                                                       |")
        print("| Total Diskon Penjualan Hari ini  Rp  "f"{int(laporan['laporan'][1]):,}""\t\t|")
        print("|                                                       |")
        print("| Total Uang Yang Harus Di Setor   Rp  "f"{int(laporan['laporan'][0]):,}""\t\t|")
        print("|                                                       |")
        print("=========================================================\n")
    while True:   
        tabel_rekap()
        print("===============================") 
        print("|>  Ketik 'X' Untuk Kembali  <|")
        print("===============================\n")
        out = input(" Masukan Pilihan Anda : ").upper()
        if out == 'X':
            clear()
            head()
            tabel()
            break
        else:
            print("\n       ===================================")
            print("       ===>   Pilihan tidak trsedia   <===")
            print("       ===================================\n")

while True:
    print("\n   ===========================================")
    print("   |> Ketik '1' untuk Transaksi             <|")
    print("   |> Ketik '2' untuk Update data           <|")
    print("   |> Ketik '3' untuk Melihat \ Edit Stok   <|")
    print("   |> Ketik '4' untuk Lihat Rekap Penjualan <|")
    print("   |> Ketik 'X' untuk Logout                <|")
    print("   ===========================================")

    aksi = input("\n==>  Masukan pilihan anda : ")
    if aksi == "1":
        transaksi()
    elif aksi == "2":
        update()
    elif aksi == "3":
        stok()
    elif aksi == "4":
        rekap_penjualan()
    elif aksi.lower() == "x":
        clear()
        tabel()
        print("\n     =======================================")
        print("     |=>  Terimakasih Telah Menggunakan  <=|")
        print("     |==>    Program Kasir Versi  2.3   <==|")
        print("     |===>          KELOMPOK 2         <===|")
        print("     =======================================")
        print('\n\n')
        break
    else:
        clear()
        head()
        tabel()
        print("\n       ===================================")
        print("       ===>   Pilihan tidak trsedia   <===")
        print("       ===================================")