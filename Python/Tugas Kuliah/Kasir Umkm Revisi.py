
from datetime import datetime

print("")
print("UMKM Kopi Jadi Kawan")
print("")
mulai = "ya"
riwayat = []   

while mulai == "ya" or mulai == "Ya":

    print("===== DAFTAR PRODUK =====")
    print("1. Risol Mayo            Rp 8000")
    print("2. Bakwan Mayo           Rp 10000")
    print("3. Pastel                Rp 8000")
    print("4. Tahu                  Rp 10000")
    print("5. Es Teh                Rp 12000")
    print("6. Tempe krispi          RP 8000")
    print("7. Kopi jadi kawan       RP 19000")
    print("8. Matcha                RP 25000")
    print("9. Sanger                RP 17000")
    print("10. Americano            RP 18000")
    print("=========================")

    nama_pelanggan = input("Nama pelanggan : ")
    print()

    total = 0
    pesanan = []   
    ulangi = "ya"

    while ulangi == "ya" or ulangi == "Ya":
        kode = input("Kode produk : ")

        
        if kode == "1":
            nama = "Risol Mayo"
            harga = 8000
        elif kode == "2":
            nama = "Bakwan Mayo"
            harga = 10000
        elif kode == "3":
            nama = "Pastel"
            harga = 8000
        elif kode == "4":
            nama = "Tahu"
            harga = 10000
        elif kode == "5":
            nama = "Es Teh"
            harga = 12000
        elif kode == "6":
            nama = "Tempe krispi"
            harga = 8000
        elif kode == "7":
            nama = "Kopi jadi kawan"
            harga = 19000
        elif kode == "8":
            nama = "Matcha"
            harga = 25000
        elif kode == "9":
            nama = "Sanger"
            harga = 17000
        elif kode == "10":
            nama = "Americano"
            harga = 18000
        else:
            nama = ""
            harga = 0

        
        if harga == 0:
            print("Kode produk tidak ada!")
        else:
            jumlah = int(input("Jumlah      : "))
            subtotal = harga * jumlah
            total = total + subtotal
            pesanan.append([nama, jumlah, harga, subtotal])
            print(nama, "x", jumlah, "= Rp", subtotal)

        ulangi = input("Ulangi (ya/tidak) : ")
        print()

    
    hapus = "tidak"
    if len(pesanan) > 0:
        hapus = input("Ada yang mau dihapus dari pesanan? (ya/tidak) : ")
        print()

    while (hapus == "ya" or hapus == "Ya") and len(pesanan) > 0:
        print("--- PESANAN SAAT INI ---")
        nomor = 1
        for item in pesanan:
            print(str(nomor) + ".", item[0], "x", item[1], "= Rp", item[3])
            nomor = nomor + 1

        pilih = int(input("Nomor yang dihapus : "))

        if pilih >= 1 and pilih <= len(pesanan):
            item_hapus = pesanan[pilih - 1]
            pesanan.remove(item_hapus)          
            total = total - item_hapus[3]       
            print(item_hapus[0], "dihapus dari pesanan")
        else:
            print("Nomor tidak ada!")

        if len(pesanan) > 0:
            hapus = input("Hapus lagi? (ya/tidak) : ")
        print()

    
    if total == 0:
        print("=========================")
        print("Belum ada produk yang dibeli.")
        mulai = input("Mulai belanja lagi? (ya/tidak) : ")
        print()
    else:
        
        print("=========================")
        print("Total belanja   :", total)

        if total >= 200000:
            persen = 10
        elif total >= 100000:
            persen = 5
        else:
            persen = 0

        diskon = total * persen // 100

        if persen == 0:
            print("Diskon          : tidak ada")
        else:
            print("Diskon", str(persen) + "%      :", diskon)

        total_setelah_diskon = total - diskon
        print("Setelah diskon  :", total_setelah_diskon)

    

       
        kirim = input("Dikirim? (ya/tidak) : ")
        medan_gratis = False

        if kirim == "ya" or kirim == "Ya":
            kota = input("Kota tujuan     : ")
            kota = kota.lower()
            if total_setelah_diskon >= 100000:
                ongkir = 0
            else:
                ongkir = 8000

            
            if total >= 30000 and kota == "medan":
                medan_gratis = True
                ongkir = 0
                print("Ongkir khusus kota Medan: GRATIS")
        else:
            
            ongkir = 0

       
        kupon = input("Kode kupon      : ")
        kupon = kupon.lower()
        cashback = 0

        if kupon == "free":
            cashback = total_setelah_diskon * 5 // 100
            print("Kupon benar, dapat cashback 5%")
        else:
            print("Kupon tidak ada")
            if total > 10000 and medan_gratis == False:
                cashback = total_setelah_diskon * 5 // 100
                print("dapat cashback 5%")

        if kirim != "ya" and kirim != "Ya":
            print("Ongkir          : - (ambil sendiri)")
        elif medan_gratis:
           
            pass
        elif ongkir == 0:
            print("Ongkir          : GRATIS")
        else:
            print("Ongkir          :", ongkir)

        
        total_transaksi = total_setelah_diskon + ongkir - cashback
        print("-------------------------")
        
        print("Total transaksi :", total_transaksi)

       
        bayar = int(input("Jumlah bayar    : "))

        
        while bayar < total_transaksi:
            kurang = total_transaksi - bayar
            print("Uang kurang Rp", kurang, "- silakan masukkan lagi")
            bayar = int(input("Jumlah bayar    : "))

        kembalian = bayar - total_transaksi

        if kembalian > 0:
            print("Sisa (kembalian):", kembalian)
        else:
            print("Uang pas, tidak ada kembalian")

       
        tanggal = datetime.now().strftime("%d-%m-%Y %H:%M")

        print()
        print("=" * 36)
        print("        UMKM Kopi Jadi Kawan")
        print("           STRUK PEMBELIAN")
        print("=" * 36)
        print("Tanggal   :", tanggal)
        print("Pelanggan :", nama_pelanggan)
        print("-" * 36)
        print("PESANAN")
        for item in pesanan:
            print(item[0])
            print("  " + str(item[1]) + " x " + str(item[2]) + "  = Rp " + str(item[3]))
        print("-" * 36)
        print("Total belanja   : Rp", total)
        if persen > 0:
            print("Diskon", str(persen) + "%      : Rp", diskon)
        if kirim == "ya" or kirim == "Ya":
            print("Ongkir          : Rp", ongkir)
        if cashback > 0:
            print("Cashback 5%     : Rp", cashback)
        print("-" * 36)
        print("Total bayar     : Rp", round (total_transaksi))
        print("Uang tunai      : Rp", bayar)
        print("Kembalian       : Rp", kembalian)
        print("=" * 36)
        print("   Terima kasih sudah berbelanja!")
        print("=" * 36)

        riwayat.append([tanggal, nama_pelanggan, total_transaksi])

        mulai = "tidak"


if len(riwayat) > 0:
    print()
    print("===== RIWAYAT TRANSAKSI =====")
    for r in riwayat:
        print(r[0], "|", r[1], "| Rp", r[2])