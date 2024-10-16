import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer()
fisherface = cv2.face.FisherFaceRecognizer()
lbph = cv2.face.LBPHFaceRecognizer()

def getImagemComId():
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    #print(caminhos)
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem) [-1].split('.')[1])
        #print(id)
        ids.append(id)
        faces.append(imagemFace)
        #cv2.imshow("Faces", imagemFace)
        #cv2.waitKey(10)
    return np.array(ids), faces

ids, faces = getImagemComId()
print(ids)
#print(faces)