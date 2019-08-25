import cv2

eye = cv2.VideoCapture(0)
face = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
while True:
    ret, frame = eye.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Find faces', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

eye.release()
cv2.destroyAllWindows()
