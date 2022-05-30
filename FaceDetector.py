import cv2

face_cascade = cv2.CascadeClassifier('face_detector.xml')

#Specify image
img = cv2.imread('people.png')

#Detect Face(s)
faces = face_cascade.detectMultiScale(img, 1.1, 4)

#Draw Rectangle(s) around face(s)
for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
cv2.imwrite("face_detected.png", img)
print('Successfully saved.')