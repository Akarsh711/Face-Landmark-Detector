import cv2
import dlib
import numpy as np


cap = cv2.VideoCapture(0)#0 for front camera
#we'll detect face form cv2 frame using dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")# for landmark detection
#the file we use here is pretrained model 

while(True):

    _, frame = cap.read()#getting image from camera
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#it's convert image to gray frame
    
    faces = detector(gray)
    

    for face in faces:
        # print(face)# coordinate of faces [(left top)(right bottom)]
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        #drawing rectangle on face
        cv2.rectangle(frame , (x1,y1), (x2,y2), (0, 255, 0), 3)# last 2 arg is color and thickness of line
        landmarks = predictor(gray, face)
        
        #plotting points on single frame 
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            print(x,y)
            cv2.circle(frame, (x, y), 3, (255, 0, 0), -3)
        
        #displaying points
        cv2.circle(frame, (x,y), 3, (255,0,0), -1)# args : image, coordinates, radius, color, thikness
    cv2.imshow("Frame", frame)#showing the live footage


    key = cv2.waitKey(1)# not know yet type soon..
    if key == 27:
        break
