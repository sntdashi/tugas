saldo = 1000000

while True:
   print("\n=== Simulasi ATM ===")
   print("1. Cek Saldo")
   print("2. Setor Tunai")
   print("3. Tarik Tunai")
   print("4. Keluar")

   pilihan=input("Pilih menu (1-4): ")
   
   if pilihan == '1':
    print (f"Saldo Anda: Rp{saldo:,.2f}")
    
    elif pilihan == '2':
        setor=float(input("Masukkan jumlah setor: "))
        saldo += setor
        print ("Setor berhasil!")
        elif pilihan =='3':
        tari=float (input("Masukkan jumlah tarik: "))
        if tarik <= saldo:
        saldo == tarik
        print ("Penarikan berhasil!")
        else:
        print("Saldo tidak cukup!")
        elif pilihan == '4':
       print("Terima kasih telah menggunakan layanan ATM.")
       break
    else:
        print("Input Valid")
        total = 0
        jumlah = 0
while True:

nilai ")) float (input ("Masukkan nilai (-1 untuk berhenti):

if nilai break == -1: total += nilai jumlah + 1

if jumlah > 0:

total rata rata jumlah print (f"Rata-rata nilai: (rata rata:.2f)")

else:

print("Tidak ada nilai yang dimasukkan.")