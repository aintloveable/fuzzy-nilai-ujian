import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Penilaian Mahasiswa", page_icon="🎓")

st.title("🎓 Sistem Fuzzy Penilaian Mahasiswa")

nilai = st.slider(
    "Masukkan Nilai Ujian",
    min_value=0,
    max_value=100,
    value=75
)

# Fungsi keanggotaan
def rendah(x):
    if x <= 40:
        return 1
    elif x < 60:
        return (60 - x) / 20
    return 0

def sedang(x):
    if x <= 40 or x >= 80:
        return 0
    elif x <= 60:
        return (x - 40) / 20
    else:
        return (80 - x) / 20

def tinggi(x):
    if x <= 60:
        return 0
    elif x < 80:
        return (x - 60) / 20
    return 1

# Fuzzifikasi
mu_rendah = rendah(nilai)
mu_sedang = sedang(nilai)
mu_tinggi = tinggi(nilai)

st.subheader("Hasil Fuzzifikasi")

st.write(f"Rendah : {mu_rendah:.2f}")
st.write(f"Sedang : {mu_sedang:.2f}")
st.write(f"Tinggi : {mu_tinggi:.2f}")

# Kesimpulan
hasil = max(
    {
        "Rendah": mu_rendah,
        "Sedang": mu_sedang,
        "Tinggi": mu_tinggi
    },
    key=lambda k: {
        "Rendah": mu_rendah,
        "Sedang": mu_sedang,
        "Tinggi": mu_tinggi
    }[k]
)

st.success(f"Kategori Nilai: {hasil}")

# Grafik
x = np.linspace(0, 100, 200)

y_rendah = [rendah(i) for i in x]
y_sedang = [sedang(i) for i in x]
y_tinggi = [tinggi(i) for i in x]

fig, ax = plt.subplots(figsize=(8,4))

ax.plot(x, y_rendah, label="Rendah")
ax.plot(x, y_sedang, label="Sedang")
ax.plot(x, y_tinggi, label="Tinggi")

ax.set_title("Grafik Fungsi Keanggotaan")
ax.set_xlabel("Nilai Ujian")
ax.set_ylabel("Derajat Keanggotaan")
ax.grid(True)
ax.legend()

st.pyplot(fig)
