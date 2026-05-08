# 🚲 Bike Sharing Analytics Dashboard ✨

Ini adalah dashboard interaktif yang dibangun menggunakan **Streamlit** untuk menganalisis tren penyewaan sepeda berdasarkan faktor waktu, musim, dan kondisi cuaca. Proyek ini merupakan bagian dari submission untuk kelas **Belajar Analisis Data dengan Python** di Dicoding.

## 👤 Identitas Pengguna
- **Nama:** Bingky
- **Email:** [Isi Email Anda]
- **ID Dicoding:** [Isi ID Dicoding Anda]

## 🌟 Fitur Dashboard
* **Metrics Summary:** Menampilkan total rental, rata-rata harian, dan angka penyewaan tertinggi secara real-time.
* **Monthly Trends:** Visualisasi fluktuasi penyewaan sepeda dari bulan ke bulan.
* **Season Analysis:** Membandingkan total penyewaan dan korelasi suhu terhadap jumlah rental di tiap musim.
* **Day Distribution:** Analisis perbedaan jumlah penyewaan pada hari kerja vs hari libur.

---

## 💻 Setup Environment - Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

```

## 💻 Setup Environment - Shell/Terminal

```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

```

## 🚀 Run Streamlit App

```bash
streamlit run dashboard.py

```

---

## 📂 Struktur Proyek

* `dashboard/`: Direktori utama aplikasi dashboard.
* `dashboard.py`: File utama aplikasi Streamlit.
* `day.csv` / `hour.csv`: Dataset yang digunakan.


* `data/`: Direktori penyimpan dataset mentah.
* `notebook.ipynb`: File analisis data (Data Wrangling, EDA, Visualization).
* `requirements.txt`: Daftar library Python yang dibutuhkan.
* `README.md`: Dokumentasi proyek ini.

```

```
