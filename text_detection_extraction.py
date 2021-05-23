import cv2
import pytesseract
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
    
img = cv2.imread("input.jpeg")
imshow(img)
plt.show()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (26, 26))
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 2)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                 cv2.CHAIN_APPROX_NONE)
imshow( dilation)

  
pytesseract_connfigs = "".join(["-c tessedit_char_whitelist= ",
                               "0123456789",
                               "abcdefghijklmnopqrstuvwxyz", 
                               "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                               " --psm 6"])
file = open("output.txt", "w")
file.write("")
file.close()

print("Detected Text:")

for i,cnt in enumerate(contours):
    x, y, w, h = cv2.boundingRect(cnt)
    cropped = img[y:y + h, x:x + w]
      
    file = open("output.txt", "a")

    text = pytesseract.image_to_string(cropped, config=pytesseract_connfigs)[:-2]
    print(text)

    file.write(text)
    file.write(" ")
    file.close()
    