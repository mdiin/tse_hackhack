import cv2
import time
import detectors

#udpStream = "udp://192.168.1.25:11111"
udpStream = 2

try:
    cap = cv2.VideoCapture(udpStream)
except:
    print("Uh oh...")

time.sleep(5)

print("Now we're going to see... something!")

frames_recorded = 0

while frames_recorded < 10:
    try:
        ret, frame = cap.read()

        qr_code = detectors.qr_code_detector(frame)
        #boxes, img = detectors.barcode_detector(frame)
        #print(boxes)
        print(f'QR code: {qr_code}')
        cv2.imshow("preview", frame)
        #frames_recorded += 1
        #time.sleep(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        #print("Oh, I have a problem!")
        continue


cap.release() # When everything done, release the capture
cv2.destroyAllWindows()
