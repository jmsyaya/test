import cv2
import numpy as np

img = cv2.imread("./images/dog.bmp")

h, w = img.shape[:2]
print(h, w)

# 1. 이동
# 변환 행렬
"""
[ 1 0 tx ] tx: x축 이동 거리
[ 0 1 ty ] ty: y축 이동 거리
"""
aff_translate = np.array([
    [1, 0, 150],
    [0, 1, 100]
], dtype=np.float32)

dst_translate = cv2.warpAffine(img, aff_translate, (w, h))

# 2. 크기 변경
# interpolation(보간법): 크기를 변경하면서 새 픽셀 값을 어떻게 계산할지 결정
# INTER_NEAREST: 가장 가까운 픽셀 값을 그대로 사용. 속도는 빠르지만 확대 시 계단 현상이 있을 수 있음
# 일반적인 축소에는 INTER_AREA가 자주 사용되고, 확대에는 INTER_NEAREST 또는 INTER_CUBIC을 많이 사용함
dst_nearest = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_NEAREST)
dst_cubic = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_CUBIC)

# 3. 회전
center = (w / 2, h / 2)
# center: 회전 중심
# angle: 회전 각도(양수는 반시계 방향)
# scale: 확대/축소 비율
rot_matrix = cv2.getRotationMatrix2D(center, 30, 0.7)
dst_rotate = cv2.warpAffine(img, rot_matrix, (w, h))


cv2.imshow("original", img)
cv2.imshow("translate", dst_translate)
cv2.imshow("resize nearest", dst_nearest)
cv2.imshow("resize cubic", dst_cubic)
cv2.imshow('rotate', dst_rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()