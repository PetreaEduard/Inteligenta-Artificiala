import cv2
import keyboard as k
face_cascade = cv2.CascadeClassifier(r'C:\Users\Ed\Desktop\facescan\trained.xml')
#img = cv2.imread(r'C:\Users\Ed\Desktop\facescan\image.jpg')
cap = cv2.VideoCapture(0)
while not k.is_pressed('esc'):
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    cv2.imshow('Imagine: ', img)
    cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release(0)


