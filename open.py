import cv2
import requests
import numpy as np
import random
from google.colab.patches import cv2_imshow

def detect_circle_and_draw_line(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)
            cv2.line(image, (x - r, y), (x + r, y), (255, 0, 0), 3)
            break

def define_score_zones(image, target_x, target_y, radii):
    for radius in radii:
        cv2.circle(image, (target_x, target_y), radius, (255, 255, 255), 2)

image_path = 'https://github.com/wnsrl3/TeamProject/blob/main/1.png?raw=true'

try:
    response = requests.get(image_path)
    response.raise_for_status() # 요청 실패 시 오류 발생 (4xx 또는 5xx 상태 코드)
    img_array = np.frombuffer(response.content, dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        
cv2_imshow(edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("이미지 로드 실패.")
except requests.HTTPError as e:
    print(f"HTTP 오류 발생: {e}")
except requests.RequestException as e:
    print(f"요청 예외 발생: {e}")
except Exception as e:
    print(f"오류 발생: {e}")
