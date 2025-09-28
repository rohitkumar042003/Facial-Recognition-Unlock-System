# from tkinter import *
# from tkinter import messagebox
import cv2
# import numpy as np

# win = Tk()
list = []
for i in range(1,20+1):
    list.append('Dataset/User' + str(i) + '.jpg')

print(list)

for i in list:
    img = cv2.imread(i)
    img = cv2.resize(img,(150,150))
    cv2.imshow('User', img)
    cv2.waitKey(300)

# cv2.waitKey(0)
cv2.destroyAllWindows()
print('Showing samples!!!')
