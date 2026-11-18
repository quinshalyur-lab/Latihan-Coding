total = 0
terbesar = 0
nilai = int(input("Nilai Transaksi(0 = selesai):    "))
while nilai != 0:
    total += nilai
    if nilai > terbesar:
         terbesar = nilai
    nilai = int(input("Nilai transaksi (0 = selesai):   "))
print("total:", total)
print("terbesar:", terbesar)