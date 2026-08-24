import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./images/man.jpg')
img2 = cv2.imread('./images/turkey.jpg')

if img1.shape != img2.shape:
    raise ValueError(f'두 이미지의 shape가 다릅니다: {img1.shape}, {img2.shape}')

"""
Numpy 덧셈과 OpenCV 덧셈의 차이
- OpenCV 이미지의 dtype은 일반적으로 uint8이며 표현 범위는 0~255
- Numpy에서 uint8 배열끼리 + 연산을 하면 255를 넘는 값은 256을 기준으로 다시 돌아오는 overflow가 발생할 수 있음
- 예) 200 + 100 = 300 -> uint8에서는 44
"""
dst_numpy = img1 + img2

# cv2.add()는 255를 초과하면 255로 제한
# 예) 200 + 100 = 255
dst_opencv = cv2.add(img1, img2)

images = {
    "img1": img1,
    "img2": img2,
    "Numpy": dst_numpy,
    "cv2.add": dst_opencv
}

plt.figure(figsize=(10, 8))

for i, (title, image) in enumerate(images.items(), start=1):
    plt.subplot(2, 2, i)

    # OpenCV는 BGR, Matplotlib은 RGB이므로 채널 순서를 변환합니다.
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image_rgb)
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()