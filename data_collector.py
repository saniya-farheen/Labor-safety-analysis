import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImage" #path to collect the images

labels = ['Vest', 'Helmet','gloves'] # collecting diffrent images for diffrent folder

number_of_images = 63
#for collecting images from the folder
for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)


    #open camera
    cap =cv2.VideoCapture(0)
    print("collecting images for {label}")
    time.sleep(5)

    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGE_PATH, label,label +'.' +' {}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)
        #to close the camera condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #release the camera
    cap.release()
    cv2.destroyAllWindows()