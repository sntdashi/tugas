# Program menghitung faktorial dari suatu bilangan

n = int(input("Masukkan bilangan: "))
faktorial = 1

for i in range(1, n + 1):
    faktorial *= i

print(f"Faktorial dari {n} adalah {faktorial}")
