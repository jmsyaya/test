import cv2
import sys

# 0은 일반적으로 기본 웹캠을 의미
# 카메라가 여러 개라면 환경에 따라 1, 2 등의 번호를 사용할 수 있음
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라를 열 수 없습니다.')
    sys.exit()

print('카메라 연결 성공')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print('가로: ', width)
print('세로: ', height)
print('카메라의 FPS: ', fps)

while True:
    ret, frame = cap.read()
    if not ret:
        print("카메라 프레임을 읽지 못했습니다.")
        break
    cv2.imshow("camera", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
