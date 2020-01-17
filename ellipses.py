import cv2
import numpy as np
import random

img = np.zeros((800, 800, 3), np.uint8)
winName = "ellipses"

class ball:
    def __init__(self, pos, speed=[0, 0], baseSize=70, angle=0, color=(255, 255, 255)):
        self.pos = pos
        self.speed = speed
        self.xSize = baseSize
        self.ySize = baseSize
        self.baseSize = baseSize
        self.angle = angle
        self.color = color
        self.potential = [0, 0]
        self.elasticity = 0.01

    def draw(self, img):
        cv2.ellipse(img, (round(self.pos[0]), round(self.pos[1])), (round(self.xSize), round(self.ySize)),
         self.angle, 0, 360, self.color, -1)

    def update(self, limitx, limity):
        status = [0, 0]
        if self.pos[0] + self.baseSize > limitx:
            self.potential[0] += self.speed[0]*self.elasticity
            self.speed[0] -= self.potential[0]
            self.xSize -= self.speed[0]
            self.ySize += self.speed[0]

        elif self.pos[0] - self.baseSize < 0:
            self.potential[0] += self.speed[0]*self.elasticity
            self.speed[0] -= self.potential[0]
            self.xSize += self.speed[0]
            self.ySize -= self.speed[0]

        else:
            status[0] = 1

        if self.pos[1] + self.baseSize > limity:
            self.potential[1] += self.speed[1]*self.elasticity
            self.speed[1] -= self.potential[1]
            self.ySize -= self.speed[1]
            self.xSize += self.speed[1]

        elif self.pos[1] - self.baseSize < 0:
            self.potential[1] += self.speed[1]*self.elasticity
            self.speed[1] -= self.potential[1]
            self.ySize += self.speed[1]
            self.xSize -= self.speed[1]

        else:
            status[1] = 1

        if status[0] and status[1]: # Need for shape correction
            self.xSize = self.baseSize
            self.ySize = self.baseSize
            self.potential = [0, 0]

        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

cv2.namedWindow(winName)
ball0 = ball([200, 200], [2, 3])

frame = 0
while 1:
    img2 = img.copy()
    ball0.update(800, 800)
    ball0.draw(img2)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

    cv2.imshow(winName, img2)
