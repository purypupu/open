import cv2
import numpy as np
import random
import math

#이미지 경로
image_path = 'https://github.com/wnsrl3/TeamProject/blob/main/1.png?raw=true'


#이미지 로드 및 처리
img = cv2.imread(image_path)
if img is None:
    raise FileNotFoundError(f" {image_path}")

w_c = img.shape[0]/2
h_c = img.shape[1]/2

#회색조 변환 후 엣지 찾기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 50)

contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

rad = []

idx = 0
for i in range(62):
    idx_be = idx
    idx += 10 if i < 30 else 5
    img_zeros = np.zeros(img.shape).astype(np.uint8)
    img_zeros = img_zeros + 255
.