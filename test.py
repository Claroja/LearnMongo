import pytesseract
import cv2
import matplotlib.pyplot as plt
img1=cv2.imread('1.png')
border = 10
replicate = cv2.copyMakeBorder(img1,border,border,border,border,cv2.BORDER_CONSTANT,value=[255,255,255])
plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.show()
plt.imshow(replicate,'gray'),plt.title('ORIGINAL')
plt.show()

pytesseract.image_to_string(replicate,lang='chi_sim_0',config='--psm 6 --oem 1')


import pandas as pd

se1 = pd.Series([True,True,False])
se2 = pd.Series([True,False,False])


se1 | se2
se1 & se2