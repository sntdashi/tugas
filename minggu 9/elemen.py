nat = [
    [3, 5, 7],
    [2, 4, 6],
    [8, 1, 9]
]

total = 0
for i in range(len(nat)):
    for j in range(len(nat[0])):
        total += nat [i][j]

print("total semua elemwn:", total)

jumlah_elemen = len(nat) * len(nat[0])
rata_rata = total / jumlah_elemen
print("rata-rata elemewn matriks:", rata_rata)

dicari = 6
found = False

for i in range(len(nat)):
    for j in range(len(nat[0])):
        if nat [i][j] == dicari:
            print(f"angka {dicari} ditemukan pada posisi ({i}, {j})")
            found = True

if not found:
    print(f"Angka {dicari} tidak ditemukan dalam matriks")