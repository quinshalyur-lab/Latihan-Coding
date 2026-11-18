total = 0

uang_yang_di_input = int(input("Masukkan uang anda (jika 0 = selesai): "))

total += uang_yang_di_input #nambahin uang yang di input ke rekening

uang_terkecil = uang_yang_di_input


while uang_yang_di_input != 0: #kalau dia 0 programnya berhenti

    uang_yang_di_input = int(input("Masukkan uang anda (jika 0 = selesai): "))

    if uang_yang_di_input < uang_terkecil and uang_yang_di_input != 0:
        uang_terkecil = uang_yang_di_input
    
    total += uang_yang_di_input

print(f"\nUang terkecil = Rp{uang_terkecil}")
print(f"Total rekening anda = Rp{total}")