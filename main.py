from __future__ import print_function
import cv2


def draw_detections(img, rects, thickness = 1): #draw rectangle
    for x, y, w, h in rects:
        print("Person found")
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)

def show_webcam(mirror=False):
  cam = cv2.VideoCapture(0)
  while True:
     ret_val, img = cam.read() #read frame
     if mirror:                     #optionally flippable video
        img = cv2.flip(img, 1)

     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     gray = cv2.equalizeHist(gray)
     hog = cv2.HOGDescriptor()
     hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )

     found, w = hog.detectMultiScale(gray, winStride=(4, 4),
		                  padding=(8, 8), scale=1.05)  #detect multi scale with given parameters
     draw_detections(img,found) #call function to draw rectangle on screen
     cv2.imshow('People Detector', img) #Show image
     ch = 0xFF & cv2.waitKey(1) #wait for ESC to quit
     if ch == 27:
        break
  cv2.destroyAllWindows()



def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()

