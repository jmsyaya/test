"""
HSV 색 공간
색상 추출과 색 기반 객체 분리에 자주 사용하는 색 공간

HSV 범위
H(Hue): 0 ~ 179, 무슨 색인가?
S(Saturation): 0 ~ 255 색이 얼마나 진한가?, 255일 때 매우 선명함
V(Value): 0 ~ 255 얼마나 밝은가?, 255일 때 매우 밝음

H
0 < 빨강
약 30 < 노랑
약 60 < 초록
약 90 < 청록
약 120 < 파랑
약 150 < 보라 계열
179 다시 빨강 근처
"""
import cv2

img = cv2.imread("./images/candies.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 파란색에 해당하는 HSV 범위를 지정
# 실제 영상에서는 조명과 카메라에 따라 범위를 적절하게 조정
lower_blue = (90, 150, 0)
upper_blue = (130, 255, 255)

# 범위 안에 있는 픽셀은 255(흰색), 범위 밖에 픽셀은 0(검정)인 마스크를 만듦
blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)


airplane = cv2.imread("./images/airplane.bmp")
field = cv2.imread("./images/field.bmp")
mask = cv2.imread("./images/mask_plane.bmp", cv2.IMREAD_GRAYSCALE)

airplane_only = cv2.copyTo(airplane, mask)
composite = field.copy()
cv2.copyTo(airplane, mask, composite)

cv2.imshow("original", img)
cv2.imshow("blue mask", blue_mask)
cv2.imshow("airplane only", airplane_only)
cv2.imshow("composite", composite)

cv2.waitKey(0)
cv2.destroyAllWindows()