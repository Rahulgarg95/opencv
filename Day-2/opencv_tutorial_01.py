import imutils
import cv2
import os

#Load input image and show its dimensions
image=cv2.imread('images/jp.png')

(h,w,d)=image.shape

print("width={}, height={}, depth={}".format(w, h, d))

cv2.imshow("Image", image)
cv2.waitKey(0)

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

#Resize the image
resized = cv2.resize(image, (200, 200))
cv2.imshow("Resized image", resized)
cv2.waitKey(0)

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h*r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)

#Resizing using imutils library
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resized", resized)
cv2.waitKey(0)

#Rotating an Image
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

#Rotation using imutils
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)


# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

#Blurring an Image
# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11,11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)


#Drawing on an image
output = image.copy()
cv2.rectangle(output, (320,60), (420,160), (0,0,255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)


#Drawing a circle
output = image.copy()
cv2.circle(output, (300,150), 20, (255,0,0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)


#Drawing a line on the image
output = image.copy()
cv2.line(output, (60,20), (400,200), (0,0,255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)


#Draw text on the image
output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!", (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)