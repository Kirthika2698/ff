import json
import cv2
import pandas as pd
import matplotlib.pyplot as plt
image1= cv2.imread("train_0.png")
cv2.imshow('ImageWindow',image1)
gray1= cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
point1 = {"x1":0.19876868953386104,"y1":0.23148148148148148}
point2 = {"x2":0.3245382585751979,"y2":0.45987654320987653}
newx1 = int(point1["x1"]* 806)
newx2 = int(point2["x2"]* 806)
