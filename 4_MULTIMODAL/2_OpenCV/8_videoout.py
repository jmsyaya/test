import cv2
import sys

cap1 = cv2.VideoCapture("./movies/232538_tiny.mp4")
cap2 = cv2.VideoCapture("./movies/276624_tiny.mp4")

if not cap1.isOpened() or not cap2.isOpened():
    print('입력 동영상 중 하나 이상을 열 수 없습니다.')
    sys.exit()

# 출력 영상의 크기와 cap1, cap2 해상도는 같아야 함
# FPS가 일정해야 함
width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap1.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30.0

print('출력 크기: ', width, "x", height)
print("출력 FPS: ", fps)

# fourcc: 동영상 압축 코덱을 지정하는 4개의 문자 코드
# AVI 파일 
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("mix.avi", fourcc, fps, (width, height))

if not out.isOpened():
    cap1.release()
    cap2.release()
    raise RuntimeError("출력 동영상 파일을 생성할 수 없습니다.")

delay = max(1, round(1000 / fps))
stop = False

for cap in (cap1, cap2):
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame.shape[1] != width or frame.shape[0] != height:
            frame = cv2.resize(frame, (width, height))

        out.write(frame)
        cv2.imshow("output", frame)

        if cv2.waitKey(delay) == 27:
            stop = True
            break

    if stop:
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()


