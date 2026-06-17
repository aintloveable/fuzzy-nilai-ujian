import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="Sistem Fuzzy Penilaian Mahasiswa",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Sistem Fuzzy Penilaian Mahasiswa")
st.write("Masukkan nilai ujian untuk mengetahui kategori nilai menggunakan Logika Fuzzy.")

# Input nilai
nilai = st.slider(
    "Masukkan Nilai Ujian",
    min_value=0,
    max_value=100,
    value=60
)

# Fungsi keanggotaan
def rendah(x):
    if x <= 40:
        return 1
    elif 40 < x < 60:
        return (60 - x) / 20
    else:
        return 0

def sedang(x):
    if x <= 40 or x >= 80:
        return 0
    elif 40 < x <= 60:
        return (x - 40) / 20
    elif 60 < x < 80:
        return (80 - x) / 20

def tinggi(x):
    if x <= 60:
        return 0
    elif 60 < x < 80:
        return (x - 60) / 20
    else:
        return 1

# Fuzzifikasi
mu_rendah = rendah(nilai)
mu_sedang = sedang(nilai)
mu_tinggi = tinggi(nilai)

# Tampilkan hasil
st.subheader("Hasil Fuzzifikasi")

st.write(f"**Rendah :** {mu_rendah:.2f}")
st.write(f"**Sedang :** {mu_sedang:.2f}")
st.write(f"**Tinggi :** {mu_tinggi:.2f}")

# Menentukan kategori
hasil = max(
    {
        "Rendah": mu_rendah,
        "Sedang": mu_sedang,
        "Tinggi": mu_tinggi
    },
    key=lambda x: {
        "Rendah": mu_rendah,
        "Sedang": mu_sedang,
        "Tinggi": mu_tinggi
    }[x]
)

st.success(f"Kategori Nilai: {hasil}")

# Grafik fungsi keanggotaan
x = np.linspace(0, 100, 500)

y_rendah = [rendah(i) for i in x]
y_sedang = [sedang(i) for i in x]
y_tinggi = [tinggi(i) for i in x]

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(x, y_rendah, label="Rendah", linewidth=2)
ax.plot(x, y_sedang, label="Sedang", linewidth=2)
ax.plot(x, y_tinggi, label="Tinggi", linewidth=2)

# Garis nilai input
ax.axvline(
    x=nilai,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'Nilai = {nilai}'
)

# Titik hasil fuzzifikasi
ax.scatter(nilai, mu_rendah, s=80)
ax.scatter(nilai, mu_sedang, s=80)
ax.scatter(nilai, mu_tinggi, s=80)

ax.set_title("Grafik Fungsi Keanggotaan")
ax.set_xlabel("Nilai Ujian")
ax.set_ylabel("Derajat Keanggotaan")
ax.set_xlim(0, 100)
ax.set_ylim(0, 1.1)

ax.grid(True)
ax.legend()

st.pyplot(fig)

# Kesimpulan
st.subheader("Kesimpulan")

st.info(
    f"Nilai ujian {nilai} termasuk kategori **{hasil}** "
    f"dengan derajat keanggotaan tertinggi sebesar "
    f"{max(mu_rendah, mu_sedang, mu_tinggi):.2f}"
)
