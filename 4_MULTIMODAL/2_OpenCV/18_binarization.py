"""
이진화(Binary Thresholding)
이진화는 픽셀 값을 두 그룹으로 나누는 영상 처리 기법

일반적인 8비트 이진 영상: 검정(0), 흰색(255)
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./images/cells.png", cv2.IMREAD_GRAYSCALE)

# 원본 이미지의 밝기 분포 확인
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# cv2.threshold()
# 반환값: 실제 사용된 임계값, 이진화 결과 이미지
# 100: 임계값, 255: 조건을 만족했을 때 사용할 최대값

# THRESH_BINARY
# 픽셀값 > threshold -> maxval
# 픽셀값 <= threshold -> 0
threshold1, dst1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
threshold2, dst2 = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)

# Otsu 자동 임계값
# THRESH_OTSH를 함께 사용하면 임계값을 사람이 직접 정하지 않고 영상의 히스토그램을 이용해 OpenCV가 임계값을 자동으로 선택
otsu_threshold, dst_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("수동 임계값 1: ", threshold1)
print("수동 임계값 2: ", threshold2)
print("otsu가 선택한 임계값: ", otsu_threshold)

cv2.imshow("original", img)
cv2.imshow("threshold 100", dst1)
cv2.imshow("threshold 210", dst2)

plt.plot(hist)
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Count")
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()