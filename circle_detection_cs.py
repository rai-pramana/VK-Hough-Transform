import cv2
import numpy as np

# Baca gambar
img = cv2.imread('biparietal.jpg')

# Mendapatkan resolusi gambar
height, width, channels = img.shape

# Output resolusi gambar
print("Resolusi gambar:")
print("Lebar:", width,"piksel")
print("Tinggi:", height,"piksel")
print()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (9, 9), 0)
edges = cv2.Canny(blurred, 90, 270)

# Deteksi lingkaran menggunakan Hough Transform
circles = cv2.HoughCircles(edges, 
                           cv2.HOUGH_GRADIENT, 
                           dp=1, 
                           minDist=500, 
                           param1=70, 
                           param2=70, 
                           minRadius=250, 
                           maxRadius=400)

# Jika lingkaran terdeteksi, gambar pada gambar asli
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Gambar lingkaran
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
        
        # Hitung diameter
        diameter = i[2] * 2
        # Tulis diameter pada gambar
        text = f"{diameter} px"
        
        # Tentukan posisi untuk menampilkan teks di tengah lingkaran
        text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        text_x = i[0] - text_size[0] // 2
        text_y = i[1] + text_size[1] // 2
        
        # Gambar teks di tengah lingkaran dengan warna hijau
        cv2.putText(img, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        # Gambar garis diameter dengan warna merah
        cv2.line(img, (i[0] - i[2], i[1]), (i[0] + i[2], i[1]), (0, 0, 255), 1)
        
        print(f"Diameter lingkaran yang terdeteksi: {diameter} piksel")

# Tampilkan hasil gambar
cv2.imshow('Grayscale', gray)
cv2.imshow('Gaussian Blur', blurred)
cv2.imshow('Edge Detection', edges)
cv2.imshow('Circle Detection', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
