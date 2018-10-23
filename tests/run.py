import time
import numpy as np
import cv2




expected = cv2.imread('C:\\Users\\ssoloshchenko\\job_control2018-09-24_11-41\\EN.png')
actual = cv2.imread('C:\\Users\\ssoloshchenko\\job_control\\Expected\\PL.png')
difference = cv2.subtract(expected, actual)
result = not np.any(difference)
if result is True:
    print("Images are same")

else:
    cv2.imwrite('C:\\Users\\ssoloshchenko\\job_control\\2018-09-04_12-39\\script_result.png', difference)
    print('Images are different')
m = actual.shape
n = actual.shape
print(n)
print(m)
print(difference)
