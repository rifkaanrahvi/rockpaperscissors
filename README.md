# ✋🧠 Aplikasi Web Klasifikasi Gambar Rock Paper Scissors

Aplikasi web sederhana berbasis Flask yang digunakan untuk mengklasifikasikan gambar tangan ke dalam tiga kategori: **Rock** (batu), **Paper** (kertas), dan **Scissors** (gunting). Aplikasi ini memanfaatkan model **Convolutional Neural Network (CNN)** yang telah dilatih sebelumnya, dan memberikan hasil klasifikasi secara real-time melalui antarmuka web yang ramah pengguna.

Model klasifikasi disimpan dalam format `.h5` dan dapat mengenali jenis gerakan tangan dari gambar yang diunggah pengguna, menjadikannya cocok untuk keperluan edukatif, demonstrasi machine learning, atau eksperimen pengembangan AI.

---

## 🔍 Fitur Utama

- 📷 **Upload Gambar**: Pengguna dapat mengunggah citra tangan langsung melalui browser.
- 🧠 **Prediksi Cerdas**: Hasil klasifikasi (Rock, Paper, atau Scissors) ditampilkan secara instan.
- 🌙 **Mode Gelap**: Antarmuka mendukung tampilan dark mode untuk kenyamanan visual.
- 📊 **Confidence Score**: Menampilkan tingkat keyakinan model dalam prediksi.
- 🖥️ **Penggunaan Lokal**: Aplikasi dapat dijalankan di komputer lokal dengan konfigurasi sederhana.

---

## 🗂️ Struktur Direktori

| Path / File                         | Deskripsi                                                                 |
|------------------------------------|--------------------------------------------------------------------------|
| `app.py`                           | Script utama backend Flask yang menangani routing dan prediksi           |
| `model_checkpoints/best_model.weights.h5` | File model CNN dalam format `.h5`                                        |
| `templates/index.html`             | Halaman utama untuk upload gambar                                        |
| `templates/result.html`            | Halaman hasil prediksi                                                   |
| `static/`                          | Berisi file CSS, ikon, dan file statis lainnya                           |
| `requirements.txt`                 | File dependensi Python                                                   |
| `README.md`                        | Dokumentasi proyek ini                                                   |

---

## ✅ Prasyarat Sistem

- Python 3.7 atau lebih baru
- pip (Python package manager)
- Flask
- (Opsional) Visual Studio Code atau editor lain

---

👨‍💻 Tim Pengembang

Rifka Anrahvi

Irma Fitriani

Rahma Devi

Intan Adha Maharani

Stevani




