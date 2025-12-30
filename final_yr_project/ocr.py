# import easyocr
# import cv2
#
# # Load the image and create an EasyOCR reader
# image = cv2.imread('numberplate.jpg')
# reader = easyocr.Reader(['en'], gpu=False)
#
# # Perform text detection using EasyOCR
# result = reader.readtext(image)
# print(result[6])
#
# for i in range(len(result)):
#     if result[i][1] == 'numberplate':
#         print(True)
#
# # Extract the character from the first bounding box
# # bbox = result[0][0]
# # x1, y1, x2, y2 = map(int, bbox)
# character = image[532:536, 724:856]
#
# # # Display the extracted character
# # cv2.imshow('Character', character)
# # cv2.waitKey(0)
# print(character)

import easyocr
import cv2

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Read image using OpenCV
image = cv2.imread('numberplate.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Pass grayscale image to EasyOCR for OCR
results = reader.readtext(gray)

# Print OCR result
l = []
for result in results:
    print(result[1])
    # l.append(result[1])
# if 'numberplate' in l:
#         print(l[l.index('numberplate')+2])


