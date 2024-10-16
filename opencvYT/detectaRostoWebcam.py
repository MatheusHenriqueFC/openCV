import cv2

classificador = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
classificadorOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
webcam = cv2.VideoCapture(0)

while True:
    camera, frame = webcam.read()

    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detecta = classificador.detectMultiScale(imagemCinza)

    for(x, y, l, a) in detecta: 
        cv2.rectangle(frame, 
        (x, y), (x + l, y + a), (255, 0, 0), 2)
        pegaOlho = frame[y:y + a, x:x + l]
        pegaOlhoCinza = cv2.cvtColor(pegaOlho, cv2.COLOR_BGR2GRAY)
        olhoDetectado = classificadorOlho.detectMultiScale(pegaOlhoCinza)
        
        for (ox, oy, ol, oa) in olhoDetectado:
            cv2.rectangle(pegaOlho, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

webcam.release
cv2.destroyAllWindows