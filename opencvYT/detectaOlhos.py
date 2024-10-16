import cv2

carregaFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
carregaOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread('imagens/imagem6.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = carregaFace.detectMultiScale(imagemCinza)


for(x, y, l, a) in faces:
    leitura = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)
    localOlho = imagem[y:y + a, x:x + l]
    localOlhoCinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
    detectado = carregaOlho.detectMultiScale(localOlhoCinza)
    #scaleFactor, minNeighbors, minSize

    for(ox, oy, ol, oa) in detectado:
        cv2.rectangle(localOlho, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

cv2.imshow("Detecta rosto e olhos", imagem)
cv2.waitKey()