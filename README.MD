# 🚲 Bike Sharing Analytics Dashboard

Ini adalah dashboard interaktif yang dibangun menggunakan **Streamlit** untuk menganalisis tren penyewaan sepeda berdasarkan faktor waktu, musim, dan kondisi cuaca. Proyek ini merupakan bagian dari submission untuk kelas **Belajar Analisis Data dengan Python** di Dicoding.

## 🌟 Fitur Dashboard
* **Metrics Summary:** Menampilkan total rental, rata-rata harian, dan angka penyewaan tertinggi secara real-time.
* **Monthly Trends:** Visualisasi fluktuasi penyewaan sepeda dari bulan ke bulan untuk melihat pola pertumbuhan.
* **Season Analysis:** Membandingkan total penyewaan dan korelasi suhu (*temperature*) terhadap jumlah rental di tiap musim.
* **Day Distribution:** Analisis perbedaan perilaku penyewa pada hari kerja (*working day*) vs hari libur (*holiday*).

---

## 💻 Setup Environment - Shell/Terminal
Proyek ini menggunakan **Virtual Environment**. Ikuti langkah-langkah berikut untuk menjalankannya di komputer lokal:

1. **Clone atau masuk ke direktori proyek:**
   ```bash
   cd "Y:\Web Profil"

```

2. **Aktivasi Virtual Environment:**
* **Windows (PowerShell):**
```powershell
.\.venv\Scripts\activate

```


* **Windows (CMD):**
```cmd
.venv\Scripts\activate

```


* **macOS/Linux:**
```bash
source .venv/bin/activate

```




3. **Instalasi Dependencies:**
Pastikan environment sudah aktif, lalu jalankan:
```bash
pip install -r requirements.txt

```



---

## 🚀 Menjalankan Aplikasi

Setelah semua library terinstal, jalankan dashboard dengan perintah berikut:

```bash
streamlit run dashboard.py

```

---

## 📂 Struktur Proyek

* `dashboard.py`: File utama aplikasi Streamlit.
* `day.csv` / `hour.csv`: Dataset yang digunakan.
* `notebook.ipynb`: Proses analisis data (Data Wrangling, EDA, Visualization).
* `requirements.txt`: Daftar library Python yang dibutuhkan.

```

**Beberapa perubahan yang saya lakukan:**
1. **Identitas:** Menambahkan bagian "Identitas Pengguna" karena ini krusial untuk penilaian reviewer Dicoding.
2. **Struktur Folder:** Menambahkan bagian "Struktur Proyek" agar reviewer tahu isi dari repository kamu.
3. **Penyempurnaan Kata:** Mengubah kata "Project" menjadi "Proyek" agar lebih sesuai dengan KBBI (standar bahasa Indonesia yang baik).
4. **Perbaikan Instruksi:** Menambahkan instruksi untuk macOS/Linux sebagai jaga-jaga jika reviewer menggunakan OS yang berbeda.

```
