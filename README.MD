# 🚲 Bike Sharing Analytics Dashboard

Ini adalah dashboard interaktif yang dibangun menggunakan **Streamlit** untuk menganalisis tren penyewaan sepeda berdasarkan faktor waktu, musim, dan kondisi cuaca. Project ini merupakan bagian dari submission untuk kelas **Belajar Analisis Data dengan Python** di Dicoding.

## 🌟 Fitur Dashboard
*   **Metrics Summary:** Menampilkan total rental, rata-rata harian, dan angka penyewaan tertinggi.
*   **Monthly Trends:** Visualisasi fluktuasi penyewaan sepeda dari bulan ke bulan.
*   **Season Analysis:** Membandingkan total penyewaan dan hubungan suhu (temperature) terhadap jumlah rental di tiap musim.
*   **Day Distribution:** Analisis perbedaan jumlah penyewaan pada hari kerja (*working day*) vs hari libur (*holiday*).

---

## 💻 Setup Environment - Shell/Terminal
Project ini menggunakan **Virtual Environment (`.venv`)**. Ikuti langkah-langkah berikut untuk setup di komputer lokal:

1.  **Buka Terminal** dan masuk ke direktori project:
    ```bash
    cd "Y:\Web Profil"
    ```

2.  **Aktivasi Virtual Environment:**
    *   **Windows (PowerShell):**
        ```powershell
        .\.venv\Scripts\activate
        ```
    *   **Windows (CMD):**
        ```cmd
        .venv\Scripts\activate
        ```

3.  **Instalasi Dependencies:**
    Setelah environment aktif, instal library yang dibutuhkan:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Menjalankan Aplikasi
Untuk menjalankan dashboard Streamlit, jalankan perintah berikut:
```bash
streamlit run dashboard.py