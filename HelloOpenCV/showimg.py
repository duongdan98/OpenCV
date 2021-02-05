import cv2
import sys
img=cv2.imread("./HelloOpenCV/rick-morty.png",0)

if img is None:
    sys.exit("Could not read the image.")
cv2.imshow("Hinh anh demo",img)
cv2.imwrite("./HelloOpenCV/rick1.png",img)
cv2.waitKey()
cv2.destroyAllWindows()