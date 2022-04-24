import cv2


i = 0
video_capture = cv2.VideoCapture('E:\photos\phone photos\VID_20190724_211546.mp4')
while True:
    ret, frame = video_capture.read()
    filename = 'image' + str(i) + '.jpg'
    if i%100 == 0:
        cv2.imwrite(filename,frame)
        cv2.imshow('frame',frame)
    i = i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()

cv2.destroyAllWindows()