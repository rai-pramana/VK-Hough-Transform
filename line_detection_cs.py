import cv2
import numpy as np

# Membaca gambar
img = cv2.imread('bandara.jpg')

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

# Hough transform line
# Transformasi Hough untuk mendeteksi garis
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=130, minLineLength=340, maxLineGap=12)

# Gambar garis yang terdeteksi pada citra asli
if lines is not None:
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            # Hitung panjang garis menggunakan formula jarak Euclidean
            line_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            # Tampilkan panjang garis berdasarkan jumlah pixel pada gambar
            cv2.putText(img, f'{line_length:.0f} px', (int((x1 + x2) / 2), int((y1 + y2) / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            print(f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}, Panjang garis: {line_length} piksel")
            print(f"((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5")
            print(f"= (({x2} - {x1}) ** 2 + ({y2} - {y1}) ** 2) ** 0.5")
            print(f"= ({(x2 - x1)} ** 2 + {(y2 - y1)} ** 2) ** 0.5")
            print(f"= ({(x2 - x1) ** 2} + {(y2 - y1) ** 2}) ** 0.5")
            print(f"= {((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5}")
            print()

# Menampilkan citra dengan garis yang terdeteksi
cv2.imshow('Grayscale', gray)
cv2.imshow('Gaussian Blur', blurred)
cv2.imshow('Edge Detection', edges)
cv2.imshow('Line Detection', img)

cv2.waitKey(0)
cv2.destroyAllWindows()