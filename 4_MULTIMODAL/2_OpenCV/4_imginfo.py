import cv2
import numpy as np

img_gray = cv2.imread("./images/dog.bmp", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("./images/dog.bmp", cv2.IMREAD_COLOR)

print('img_gray type: ', type(img_gray))
print('img_gray shape: ', img_gray.shape) # (높이, 너비)
print('img_gray dtype: ', img_gray.dtype) # uint8

print('img_color type: ', type(img_color))
print('img_color shape: ', img_color.shape)
print('img_color dtype: ', img_color.dtype)

h, w = img_color.shape[:2]
print(f'이미지 크기: {w} * {h}') # 이미지 크기: 548 * 364


# ndim: 배열의 차원 수를 반환
# 흑백 이미지: 2차원
# 컬러 이미지: 3차원
if img_color.ndim == 3:
    print('img_color는 컬러 이미지입니다.')
elif img_color.ndim == 2:
    print('img_color는 그레이스케일 이미지입니다.')


img1 = np.zeros((240, 320, 3), dtype=np.uint8) # 검은색 이미지
# np.empty()는 메모리 공간만 할당하고 예측할 수 없는 값을 저장함
img2 = np.empty((240, 320), dtype=np.uint8)
# 모든 픽셀 값이 120인 회색 이미지
img3 = np.full((240, 320), 120, dtype=np.uint8)
img4 = np.full((240, 320, 3), (255, 102, 255), dtype=np.uint8)

cv2.imshow('original', img_color)
cv2.imshow('zeros', img1)
cv2.imshow('empty', img2)
cv2.imshow('gray_120', img3)
cv2.imshow('full_color', img4)


# img1을 (255, 102, 255)로 색상을 변경
# img1.shape > (240, 320, 3)
'''
height, width = img1.shape[:2]
for y in range(height):
    for x in range(width):
        img1[y, x] = (255, 102, 255)
'''
img1[:, :] = (255, 102, 255)
cv2.imshow('change', img1)


while True:
    key = cv2.waitKey(0)
    if key in (ord("i"), ord("I")):
        # unit8 이미지에서 반전(~)은 각 픽셀에 대해 255-값과 같은 결과를 만듦
        img_color = ~img_color
        cv2.imshow("original", img_color)
    elif key == 27:
        break
    
cv2.destroyAllWindows()