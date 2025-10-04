# VK-Hough-Transform

Proyek Computer Vision untuk deteksi garis dan lingkaran menggunakan Hough Transform dengan OpenCV dan Python.

## 📝 Deskripsi

Proyek ini mengimplementasikan algoritma Hough Transform untuk mendeteksi garis dan lingkaran pada citra digital. Implementasi tersedia dalam dua mode:

-   **Computer Sample (CS)**: Deteksi pada gambar statis
-   **Real-time (RT)**: Deteksi secara real-time menggunakan kamera webcam

## 🚀 Fitur

### Deteksi Garis

-   ✅ Deteksi garis lurus pada gambar statis (`line_detection_cs.py`)
-   ✅ Deteksi garis real-time dari webcam (`line_detection_rt.py`)
-   ✅ Perhitungan panjang garis dengan formula jarak Euclidean
-   ✅ Visualisasi hasil deteksi dengan overlay pada gambar asli

### Deteksi Lingkaran

-   ✅ Deteksi lingkaran pada gambar medis (`circle_detection_cs.py`)
-   ✅ Deteksi lingkaran real-time dari webcam (`circle_detection_rt.py`)
-   ✅ Perhitungan diameter lingkaran
-   ✅ Visualisasi pusat dan diameter lingkaran

## 🛠️ Teknologi

-   **Python 3.x**
-   **OpenCV (cv2)** - Computer Vision library
-   **NumPy** - Numerical computing

## 📁 Struktur Proyek

```
VK-Hough-Transform/
├── README.md
├── bandara.jpg                    # Sample image untuk deteksi garis
├── biparietal.jpg                 # Sample image untuk deteksi lingkaran
├── circle_detection_cs.py         # Deteksi lingkaran pada gambar statis
├── circle_detection_rt.py         # Deteksi lingkaran real-time
├── line_detection_cs.py           # Deteksi garis pada gambar statis
├── line_detection_rt.py           # Deteksi garis real-time
└── Hasil/                         # Folder hasil output
    ├── circle_detection_cs.png
    ├── circle_detection_rt.png
    ├── line_detection_cs.png
    └── line_detection_rt.png
```

## 🔧 Instalasi

1. **Clone repository:**

    ```bash
    git clone https://github.com/rai-pramana/VK-Hough-Transform.git
    cd VK-Hough-Transform
    ```

2. **Install dependencies:**
    ```bash
    pip install opencv-python numpy
    ```

## 🎯 Cara Penggunaan

### Deteksi Garis pada Gambar Statis

```bash
python line_detection_cs.py
```

-   Menggunakan gambar `bandara.jpg`
-   Menampilkan hasil preprocessing (grayscale, blur, edge detection)
-   Menghitung dan menampilkan panjang setiap garis yang terdeteksi

### Deteksi Garis Real-time

```bash
python line_detection_rt.py
```

-   Menggunakan kamera webcam
-   Tekan `q` untuk keluar

### Deteksi Lingkaran pada Gambar Statis

```bash
python circle_detection_cs.py
```

-   Menggunakan gambar medis `biparietal.jpg`
-   Menghitung dan menampilkan diameter lingkaran
-   Menggambar garis diameter pada hasil

### Deteksi Lingkaran Real-time

```bash
python circle_detection_rt.py
```

-   Menggunakan kamera webcam
-   Tekan `q` untuk keluar

## 🔍 Detail Algoritma

### Preprocessing

1. **Grayscale Conversion**: Mengubah citra RGB ke grayscale
2. **Gaussian Blur**: Mengurangi noise dengan kernel 9x9
3. **Canny Edge Detection**: Deteksi tepi untuk input Hough Transform

### Hough Transform Parameters

-   **Line Detection**: `HoughLinesP` dengan threshold yang dapat disesuaikan
-   **Circle Detection**: `HoughCircles` dengan parameter dp, minDist, param1, param2

## 📊 Hasil

Semua hasil deteksi disimpan dalam folder `Hasil/` dengan format:

-   Visualisasi setiap tahap preprocessing
-   Hasil final dengan overlay deteksi
-   Informasi numerik (panjang garis/diameter lingkaran)

## 🎓 Aplikasi

-   **Computer Vision Education**: Pembelajaran algoritma Hough Transform
-   **Medical Imaging**: Deteksi struktur circular pada citra medis
-   **Industrial Inspection**: Deteksi garis dan bentuk geometris
-   **Real-time Analysis**: Monitoring objek secara real-time

## 🤝 Kontribusi

Contributions are welcome! Feel free to submit pull requests atau open issues untuk perbaikan dan pengembangan fitur baru.

## 📄 Lisensi

Proyek ini dibuat untuk tujuan edukasi dan penelitian.

## 👨‍💻 Penulis

**Rai Pramana**

-   GitHub: [@rai-pramana](https://github.com/rai-pramana)

---

⭐ Jika proyek ini membantu, jangan lupa berikan star!
