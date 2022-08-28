import cv2
trained_face_data= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_detector=cv2.CascadeClassifier('haarcascade_smile.xml')
webcam=cv2.VideoCapture(0)

while True:
    read_successful,frame=webcam.read()
    if not read_successful:
        break
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cooridnate = trained_face_data.detectMultiScale(gray_scale)
    smile=smile_detector.detectMultiScale(gray_scale,scaleFactor=1.7,minNeighbors=20)

    for (x, y, w, h) in face_cooridnate:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        the_face=frame[x:x+w,y:y+h]
        face_scale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
        smile = smile_detector.detectMultiScale(face_scale, scaleFactor=1.7, minNeighbors=20)
        if len(smile)>0:
            cv2.putText(frame,'Smiling',(x,y+h+40),fontScale=3,fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255,255,0))




    cv2.imshow("Hello SmilemPlease", frame)

    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break


print("Code Completed")