import cv2

# Fungsi untuk mendeteksi lingkaran
def detect_circles(frame):
    # Preprocessing: Ubah citra ke grayscale
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Preprocessing: Terapkan Gaussian Blur untuk mengurangi noise
    blur_image = cv2.GaussianBlur(gray_image, (9, 9), 0)

    # Preprocessing: Deteksi tepi
    edge_image = cv2.Canny(blur_image, 20, 50, apertureSize=3)

    # Deteksi lingkaran menggunakan Hough Circle Transform
    circles = cv2.HoughCircles(edge_image, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                               param1=60, param2=50, minRadius=20, maxRadius=100)
    
    # Gambar lingkaran yang terdeteksi
    if circles is not None:
        circles = circles[0]  # Ambil lingkaran dari hasil deteksi
        for circle in circles:
            x, y, radius = circle
            # Ubah koordinat pusat menjadi tuple
            center = (int(x), int(y))
            # Gambar lingkaran merah di sekitar objek yang terdeteksi
            cv2.circle(frame, center, int(radius), (0, 0, 255), 2)
            # Gambar pusat lingkaran (titik) dalam warna merah
            cv2.circle(frame, center, 2, (0, 0, 255), 3)
    
    return frame, blur_image, edge_image, gray_image

# Buka kamera
cap = cv2.VideoCapture(0)

while True:
    # Ambil frame dari kamera
    ret, frame = cap.read()
    if not ret:
        break
    
    # Deteksi lingkaran pada setiap frame
    result_frame, blur_image, edge_image, gray_image = detect_circles(frame)

    # Tampilkan frame hasil grayscale
    cv2.imshow('Grayscale', gray_image)

    # Tampilkan frame hasil Gaussian Blur
    cv2.imshow('Gaussian Blur', blur_image)

    # Tampilkan frame hasil deteksi tepi
    cv2.imshow('Edge Detection', edge_image)
    
    # Tampilkan frame hasil deteksi lingkaran
    cv2.imshow('Real-time Circle Detection', result_frame)
    
    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bebaskan sumber daya dan tutup semua jendela OpenCV
cap.release()
cv2.destroyAllWindows()
