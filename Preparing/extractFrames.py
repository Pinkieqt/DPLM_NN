import os
import moviepy.editor as mp
import cv2


directory = "C:\DiplomkaData\VIDEOS/rados_anomal/"
directoryToSave = "C:\DiplomkaData\FRAMES/rados_anomal/"
fileName = "anomal_logi_face_rados.mp4"

video = cv2.VideoCapture(directory + fileName)

i = 0

while video.isOpened():
    ret, frame = video.read()
    if ret == False:
        break
    cv2.imwrite(directoryToSave + "img" + str(i) + ".jpg", frame)
    print("Snímek číslo: " + str(i))
    i += 1

video.release()
cv2.destroyAllWindows()
