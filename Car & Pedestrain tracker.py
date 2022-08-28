import cv2
img_file='front car.jpg'
img_read=cv2.imread(img_file)
video=cv2.VideoCapture("car-and-pedestrian-video0.mp4")
car_tracker_file = 'car_detector.xml'
pedestrain='haarcascade_fullbody.xml'
car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrain_tracker=cv2.CascadeClassifier(pedestrain)

while True:
    read_successful,frame= video.read()
    if read_successful:
        grayscale_d=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break
    cars = car_tracker.detectMultiScale(grayscale_d)
    ped=pedestrain_tracker.detectMultiScale(grayscale_d)
    for x, y, w, h in cars:
        cv2.rectangle(frame, (x, y), (x + h, y + w), (0, 255, 0), 2)

    for x, y, w, h in ped:
        cv2.rectangle(frame, (x, y), (x + h, y + w), (0, 255, 255 ), 2)

    cv2.imshow("Hello", frame)
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break

video.release()
print("Completed")
