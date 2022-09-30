from djitellopy import Tello
import uuid
import cv2
import detectors
import re

def drone_init(drone):
    drone.connect()
    drone.streamon()
    drone.enable_mission_pads()
    drone.set_mission_pad_detection_direction(0)
    drone.takeoff()
    drone.move_down(40)

def drone_stop(drone):
    drone.streamoff()
    drone.land()
    drone.disable_mission_pads()
    drone.end()

def find_qr(drone):
    frame_read = drone.get_frame_read()
    detector = cv2.QRCodeDetector()
    frame = frame_read.frame
    text, points, _ = detector.detectAndDecode(frame)
    image_name = f'pic_{uuid.uuid4()}.png'
    if text != "":
        cv2.imwrite(image_name, frame)
    print(f'[{image_name}] QR Code: {text}')

def find_barcodes(drone):
    frame_read = drone.get_frame_read()
    frame = frame_read.frame
    barcodes = detectors.barcode_scanner(frame)
    image_name = f'pic_{uuid.uuid4()}.png'
    if len(barcodes) != 0:
        cv2.imwrite(image_name, frame)
    print(f'[{image_name}] Barcodes: {barcodes}')
    return barcodes

barcode_regex = re.compile(r'CODE')

def scan_updown(drone):
    rows = [set([])]
    anus = 0

    # if all else fails, go with this
    drone_init(drone)
    while drone.get_height() < 210:
        barcodes = []

        #find_qr(drone)
        barcodes = find_barcodes(drone)
        # QR code found?
        newest_row_idx = len(rows) - 1
        for barcode in barcodes:
            if barcode.type == "QRCODE":
                rows[newest_row_idx].add(barcode.data.decode("utf-8"))
                rows.append(set([]))

        # Barcodes found?
        newest_row_idx = len(rows) - 1
        for barcode in barcodes:
            if barcode_regex.search(barcode.type):
                rows[newest_row_idx].add(barcode.data.decode("utf-8"))
        drone.move_up(40)

    print(f'Rows: {rows}')
    drone_stop(drone)

def drone_zone(drone):
    drone.connect()
    drone.streamon()
    frame_read = drone.get_frame_read()
    cv2.imwrite("picture.png", frame_read.frame)
    print("Wrote image.")
    drone.end()

def start_the_drone():
    tello = Tello("192.168.1.25")
    scan_updown(tello)
