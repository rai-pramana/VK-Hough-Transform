import cv2
import numpy as np

# Fungsi untuk mendeteksi garis
def detect_lines(frame):
    # Preprocessing: Ubah citra ke grayscale
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Preprocessing: Terapkan Gaussian Blur untuk mengurangi noise
    blur_image = cv2.GaussianBlur(gray_image, (9, 9), 0)

    # Preprocessing: Deteksi tepi
    edge_image = cv2.Canny(blur_image, 50, 150, apertureSize=3)
    
    # Deteksi garis menggunakan Hough Line Transform
    lines = cv2.HoughLinesP(edge_image, rho=1, theta=np.pi / 180, threshold=80,
                            minLineLength=5, maxLineGap=20)
    
    # Gambar garis-garis yang terdeteksi pada citra
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            # Gambar garis merah
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    return frame, edge_image, blur_image, gray_image

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Deteksi garis lurus pada setiap frame
    result_frame, edge_image, blur_image, gray_image = detect_lines(frame)

    # Tampilkan frame hasil grayscale
    cv2.imshow('Grayscale', gray_image)
    
    # Tampilkan frame hasil Gaussian Blur
    cv2.imshow('Gaussian Blur', blur_image)

    # Tampilkan frame hasil deteksi tepi
    cv2.imshow('Edge Detection', edge_image)
    
    # Tampilkan frame hasil deteksi garis
    cv2.imshow('Real-time Line Detection', result_frame)
    
    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bebaskan sumber daya dan tutup semua jendela OpenCV
cap.release()
cv2.destroyAllWindows()
