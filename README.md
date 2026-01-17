# 🎮 Online Gaming Engagement Predictor

Aplikasi berbasis **Machine Learning** yang dirancang untuk memprediksi tingkat keterlibatan (_engagement level_) pemain dalam game online berdasarkan data perilaku mereka.

---

## ✨ Fitur Utama

-   **Prediksi Real-time**: Masukkan data perilaku pemain dan dapatkan hasil prediksi tingkat keterlibatan secara instan.
-   **Antarmuka Interaktif**: Dibangun menggunakan **Streamlit** untuk pengalaman pengguna yang intuitif.
-   **Analisis Data Terintegrasi**: Menyertakan notebook khusus untuk Exploratory Data Analysis (EDA) dan evaluasi model.
-   **Ready to Deploy**: Dilengkapi dengan konfigurasi **Docker** dan **GitHub Actions** untuk kebutuhan CI/CD.

---

## 🧠 Cara Kerja Model

Aplikasi ini menggunakan pipeline Machine Learning yang telah dioptimasi:

1. **Data Collection**: Menggunakan dataset `online_gaming_insights.csv` yang mencakup metrik seperti waktu bermain, skor, dan interaksi sosial.
2. **Preprocessing**: Data dibersihkan dan diproses menggunakan `StandardScaler` untuk memastikan performa model yang stabil.
3. **Modeling**: Menggunakan algoritma **XGBoost (Extreme Gradient Boosting)** yang telah di-tuning untuk memberikan akurasi prediksi terbaik.
4. **Inference**: Model yang telah dilatih disimpan dalam format `.pkl` dan dimuat oleh aplikasi Streamlit untuk melakukan prediksi pada data baru.

---

## 📂 Struktur Proyek

```text
GAME-ONLINE-ENGAGEMENT/
├── .github/workflows/      # Automasi Deployment (deploy.yml)
├── data/                   # Dataset (online_gaming_insights.csv)
├── models/                 # Model biner (XGBoost, Scaler, Feature Columns)
├── notebooks/              # Eksperimen & EDA (main.ipynb)
├── src/                    # Source code utama (app.py)
├── Dockerfile              # Konfigurasi Docker
├── requirements.txt        # Dependensi library
└── README.md               # Dokumentasi proyek

```

---

## 🚀 Memulai Proyek

### Instalasi Lokal

1. **Clone repository**:

```bash
git clone https://github.com/lutfialvarop/game-online-engagement.git
cd game-online-engagement

```

2. **Install dependencies**:

```bash
pip install -r requirements.txt

```

3. **Jalankan aplikasi**:

```bash
streamlit run src/app.py

```

### Menjalankan dengan Docker

```bash
docker-compose up --build

```

---
