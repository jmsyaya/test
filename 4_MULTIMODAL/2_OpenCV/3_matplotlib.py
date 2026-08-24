import cv2
import matplotlib.pyplot as plt

img_gray = cv2.imread("./images/dog.bmp", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("./images/dog.bmp", cv2.IMREAD_COLOR)

"""
OpenCV와 Maplotlib의 색상 채널 순서 차이

OpenCV: BGR 순서
Matplotlib: RGB 순서

> 따라서 OpenCV로 읽은 컬러 이미지를 Matplotlib에 바로 표시하면 빨강과 파랑이 뒤바뀐 것처럼 보임
"""

img_color_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

# 1행 2열의 그래프 영역 중 첫 번째 위치
plt.subplot(1, 2, 1)
plt.axis("off")
plt.title("Grayscale")
plt.imshow(img_gray, cmap="gray")

# 1행 2열의 그래프 영역 중 두 번째 위치
plt.subplot(1, 2, 2)
plt.axis("off")
plt.title("Color")
plt.imshow(img_color_rgb)

plt.tight_layout()
plt.show()

