print("========== SELAMAT DATANG DI TOKO MANIS ==========")

menu_1 = "mochi coklat"
harga_menu_1 = 10000
menu_2 = "cookie matcha"
harga_menu_2 = 7000
menu_3 = "brownies fudgy"
harga_menu_3 = 45000

print(f"1. {menu_1} = Rp.{harga_menu_1}")
print(f"2. {menu_2} = Rp.{harga_menu_2}")
print(f"3. {menu_3} = Rp.{harga_menu_3}")

pesanan = input("Masukkan nama produk yang anda pilih = ")

if pesanan == menu_1:
    print(f"harga pesanan anda adalah = RP.{harga_menu_1}")
elif pesanan == menu_2:
    print(f"harga pesanan anda adalah = RP.{harga_menu_2}")
elif pesanan == menu_3:
    print(f"harga pesanan anda adalah = RP.{harga_menu_3}")
else:
    print("MAAF PESANAN ANDA TIDAK ADA DI DAFTAR")
    