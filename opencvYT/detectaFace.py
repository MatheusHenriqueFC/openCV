import cv2

classificador = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

while True:
    camera, frame = webcam.read()

    cv2.imshow("imagem webcamera", frame)

    if cv2.waitKey(1) == ord('f'):
        break

webcam.release()
cv2.destroyAllWindows()