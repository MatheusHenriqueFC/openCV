import cv2

classificador = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erro ao abrir a câmera")
    exit()

while True:
    conectado, imagem = camera.read()
    
    # Verifica se a imagem foi capturada corretamente
    if not conectado or imagem is None:
        print("Erro ao capturar imagem da câmera")
        break
    
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(100, 100))

    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

    cv2.imshow("Face", imagem)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
camera.release()
cv2.destroyAllWindows()
