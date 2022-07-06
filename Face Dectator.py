import cv2
trained_face_data= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#img=cv2.imread('salman.jpg')
webcam=cv2.VideoCapture(0)
while True:
    successful_frame_read,frame=webcam.read()
    gray_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_cooridnate = trained_face_data.detectMultiScale(gray_scale)
    for (x, y, w, h) in face_cooridnate:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Hello', frame)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break

print("Code Completed")

