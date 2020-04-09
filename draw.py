# 根据像素点位置画框
#   如果小于两点会输出原图
#   如果是两点直接画矩形框
#   如果是三点及以上则依次连接，1->2->3->...->1
import cv2
import numpy as np

point = [
    {
        "vertices": {
            "x": 20,
            "y": 20
        }
    },
    {
        "vertices": {
            "x": 200,
            "y": 200
        }
    },
    {
        "vertices": {
            "x": 300,
            "y": 500
        }
    },
    {
        "vertices": {
            "x": 80,
            "y": 500
        }
    }
]

img = cv_img = cv2.imdecode(np.fromfile('SenseKeeper模拟.jpg', dtype=np.uint8), -1)
image = img
if len(point) == 2:
    x1 = point[0]["vertices"]["x"]
    y1 = point[0]["vertices"]["y"]
    x2 = point[1]["vertices"]["x"]
    y2 = point[1]["vertices"]["y"]
    image = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
elif len(point) > 2:
    for index, value in enumerate(point):
        x1 = point[index]["vertices"]["x"]
        y1 = point[index]["vertices"]["y"]
        if index == len(point) - 1:
            x2 = point[0]["vertices"]["x"]
            y2 = point[0]["vertices"]["y"]
        else:
            x2 = point[index + 1]["vertices"]["x"]
            y2 = point[index + 1]["vertices"]["y"]
        image = cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv2.imshow("img", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
