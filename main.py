# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

 #mjpg-streamerを動作させているPC・ポートを入力
URL = "http://raspberrypi.local:8080/?action=stream"
s_video = cv2.VideoCapture(URL)
#faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#(負荷がかかりすぎる)faceCascade = cv2.CascadeClassifier('cascade.xml')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')


while True:
    ret, img = s_video.read()
    img = cv2.resize(img, (640, 480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    #CV_HAAR_SCALE_IMAGE
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("camera", img)
    key = cv2.waitKey(1)
    if key == 27: #Esc入力時は終了
        break
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
