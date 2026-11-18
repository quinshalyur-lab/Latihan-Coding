# TR-3: KALKULATOR KEUNTUNGAN UMKM

# 1. Input: nama produk, harga modal, harga jual, dan jumlah terjual.
nama_produk = input("Nama produk : ")
harga_modal = int(input("Harga modal: "))
harga_jual = int(input("harga jual: "))
jumlah_terjual = int(input("jumlah terjual:"))
print(nama_produk)

# 2. Perhitungan
omzet = harga_jual * jumlah_terjual
total_modal  = harga_modal * jumlah_terjual
laba = omzet - total_modal
margin= laba / omzet * 100
print("omzet    :", omzet)
print("total modal :", total_modal)
print("laba       :", laba)
print("margin      :", margin)

# 3. Tampilkan True/False: apakah laba ≥ Rp1.000.000 dan margin ≥ 20% ?
target_tercapai = laba >= 1000000 and margin >= 20
print("Target Tercapai", target_tercapai)

# 4. Hitung berapa lusin produk terjual dan sisa satuannya (pakai// dan %).
lusin = jumlah_terjual // 12
sisa_satuan = jumlah_terjual % 12
print("lusin :", lusin)
print("sisa satuan :", sisa_satuan)