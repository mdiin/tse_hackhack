import cv2
import time

udpStream = "udp://192.168.1.25:11111"
#udpStream = 0

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
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        scale_percent = 80
        # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image

        cv2.imshow("preview", img)
        frames_recorded += 1
        time.sleep(1)
    except:
        print("Oh, I have a problem!")
        continue


    # for barcode in decode(img):
    #     (x, y, w, h) = barcode.rect
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #     barcodeData = barcode.data.decode('utf-8')
    #     barcodeType = barcode.type
    #     text = "{} ({})".format(barcodeData, barcodeType)
    #     cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    #     print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    #     cv2.imshow("preview", img)
    #     # Waits for a user input to quit the application
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

cap.release() # When everything done, release the capture
cv2.destroyAllWindows()
