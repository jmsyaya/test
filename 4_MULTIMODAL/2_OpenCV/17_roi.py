'''
ROI(Region of Interest)
이미지 전체가 아니라 특정 관심 영역만 선택해서 처리할 때 사용
'''
import cv2

img = cv2.imread("./images/sun.jpg")

x = 182
y = 23
w = 120
h = 108

roi = img[y:y+h, x:x+w]
roi_copy = roi.copy()

dst_x1 = x + w
dst_x2 = dst_x1 + w

# 복사할 공간이 실제 이미지 범위 안에 있는지 확인
if y + h <= img.shape[0] and dst_x2 <= img.shape[1]:
    img[y:y+h, dst_x1:dst_x2] = roi_copy
else:
    raise ValueError("ROI를 복사할 위치가 이미지 범위를 벗어남")

# 원본 ROI와 복사된 ROI를 한 번에 감싸는 사각형
cv2.rectangle(img, (x, y), (dst_x2, y+h), (0, 255, 0), 3)

cv2.imshow("original", img)
cv2.imshow("ROI result", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
