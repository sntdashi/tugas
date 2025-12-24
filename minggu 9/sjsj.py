# --- SESSION 2: PREDIKSI TAMBAHAN (BONUS) ---

# 1. MOTOR: Cek Harga Ekstrem (Baru banget & Tua banget)
X_motor_ronde2 = np.array([[0.2], [10.0]]) # 0.2 tahun (baru 2 bulan) & 10 tahun
prediksi_motor2 = model.predict(X_motor_ronde2)

print("\n===PREDIKSI MOTOR EKSTREM ===")
for i, val in enumerate(X_motor_ronde2):
    h = prediksi_motor2[i]
    if h < 0: h = 0 # Kalau minus anggap gratis
    print(f"Motor umur {val[0]} tahun -> Harga: {h:.2f} Juta")

# Visualisasi Motor (Silang Magenta)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(X, y, color='green', label='Data Asli')
plt.plot(X, model.predict(X), color='orange')
plt.scatter(X_motor_ronde2, prediksi_motor2, color='magenta', marker='X', s=200, edgecolor='black', zorder=5, label='Ronde 2')
plt.title('Motor Bekas: Ronde 2')
plt.legend()


# 2. BUAH: Cek Buah "Galau" (Ukuran Nanggung)
# Buah yang ukurannya di perbatasan antara Jeruk & Lemon
X_buah_ronde2 = [
    [5.5, 110], # Tengah-tengah Jeruk & Lemon
    [7.0, 145]  # Tengah-tengah Jeruk & Apel
]
prediksi_buah2 = knn.predict(X_buah_ronde2)

print("\n===KLASIFIKASI BUAH GALAU ===")
for i, d in enumerate(X_buah_ronde2):
    print(f"Buah ukuran {d} -> Diklasifikasikan: {prediksi_buah2[i]}")

# Visualisasi Buah Ronde 2 (Wajik Pink)
plt.subplot(1, 2, 2)
# Plot ulang data lama biar backgroundnya ada
colors = {'Apel': 'red', 'Jeruk': 'orange', 'Lemon': 'gold'}
for cat in ['Apel', 'Jeruk', 'Lemon']:
    x_pts = [x[0] for i, x in enumerate(X) if y[i] == cat]
    y_pts = [x[1] for i, x in enumerate(X) if y[i] == cat]
    plt.scatter(x_pts, y_pts, color=colors[cat], s=50, alpha=0.3) # Transparan dikit

# Plot Ronde 2
plt.scatter([x[0] for x in X_buah_ronde2], [x[1] for x in X_buah_ronde2], 
            color='hotpink', marker='D', s=200, edgecolor='black', label='Ronde 2 (Nanggung)')

plt.title('Klasifikasi Buah: Ronde 2')
plt.legend()
plt.tight_layout()
plt.show()