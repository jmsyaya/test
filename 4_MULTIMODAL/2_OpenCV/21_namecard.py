import cv2
import numpy as np

img = cv2.imread("./images/namecard.jpg")

if img is None:
    raise FileNotFoundError("./images/namecard.jpg를 불러오지 못했습니다.")

h, w = img.shape[:2]

# 출력 이미지 높이
dst_h = 500

# 원본 예제의 비율을 그대로 유지합니다.
# 297 : 210 비율을 이용한 가로 크기 계산
dst_w = round(dst_h * 297 / 210)

# ------------------------------------------------------------
# 초기 네 꼭짓점
# ------------------------------------------------------------
# 순서:
# 0 = 왼쪽 위
# 1 = 왼쪽 아래
# 2 = 오른쪽 아래
# 3 = 오른쪽 위
src_quad = np.array([
    [30, 30],
    [30, h - 30],
    [w - 30, h - 30],
    [w - 30, 30]
], dtype=np.float32)

# 목적지 좌표도 동일한 꼭짓점 순서를 사용해야 합니다.
dst_quad = np.array([
    [0, 0],
    [0, dst_h - 1],
    [dst_w - 1, dst_h - 1],
    [dst_w - 1, 0]
], dtype=np.float32)

# 각 꼭짓점이 현재 드래그 중인지 저장
drag_src = [False, False, False, False]


def draw_roi(image, corners):
    """
    사용자가 선택한 네 꼭짓점과 연결선을 화면에 그립니다.
    원본 이미지를 직접 변경하지 않기 위해 copy()를 사용합니다.
    """
    preview = image.copy()

    point_color = (192, 192, 255)
    line_color = (128, 128, 255)

    # 꼭짓점 표시
    for pt in corners:
        cv2.circle(
            preview,
            tuple(pt.astype(int)),
            12,
            point_color,
            -1
        )

    # 사각형 연결
    for i in range(4):
        pt1 = tuple(corners[i].astype(int))
        pt2 = tuple(corners[(i + 1) % 4].astype(int))

        cv2.line(
            preview,
            pt1,
            pt2,
            line_color,
            2
        )

    return preview


def on_mouse(event, x, y, flags, param):
    """
    마우스로 네 꼭짓점을 드래그하는 콜백 함수
    """
    global src_quad, drag_src

    # --------------------------------------------------------
    # 왼쪽 버튼 DOWN
    # --------------------------------------------------------
    if event == cv2.EVENT_LBUTTONDOWN:

        for i in range(4):

            # 현재 클릭 위치와 꼭짓점 사이의 유클리드 거리
            distance = cv2.norm(
                src_quad[i] - np.array([x, y], dtype=np.float32)
            )

            if distance < 20:
                drag_src[i] = True
                break

    # --------------------------------------------------------
    # 마우스 이동
    # --------------------------------------------------------
    elif event == cv2.EVENT_MOUSEMOVE:

        for i in range(4):

            if drag_src[i]:

                # 좌표가 이미지 바깥으로 나가지 않도록 제한합니다.
                new_x = np.clip(x, 0, w - 1)
                new_y = np.clip(y, 0, h - 1)

                src_quad[i] = (new_x, new_y)

                preview = draw_roi(img, src_quad)
                cv2.imshow("img", preview)

                break

    # --------------------------------------------------------
    # 왼쪽 버튼 UP
    # --------------------------------------------------------
    elif event == cv2.EVENT_LBUTTONUP:

        # 모든 드래그 상태를 False로 되돌립니다.
        drag_src = [False, False, False, False]


# 초기 선택 영역 표시
display = draw_roi(img, src_quad)

cv2.namedWindow("img")
cv2.setMouseCallback("img", on_mouse)
cv2.imshow("img", display)

print("네 꼭짓점을 드래그하여 영역을 맞추세요.")
print("Enter: 투시 변환")
print("ESC  : 종료")

while True:
    key = cv2.waitKey(0)

    if key == 27:
        cv2.destroyAllWindows()
        raise SystemExit

    elif key in (10, 13):
        # 운영체제에 따라 Enter 키 값이 10 또는 13일 수 있습니다.
        break

# ------------------------------------------------------------
# 투시 변환
# ------------------------------------------------------------
perspective_matrix = cv2.getPerspectiveTransform(
    src_quad,
    dst_quad
)

dst = cv2.warpPerspective(
    img,
    perspective_matrix,
    (dst_w, dst_h),
    flags=cv2.INTER_CUBIC
)

cv2.imshow("perspective result", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
