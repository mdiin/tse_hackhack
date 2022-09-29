from djitellopy import Tello
import cv2

def drone_info(drone):
    print(f'Capture URL: {drone.get_udp_video_address()}')

def drone_zone(drone):
    drone.connect()
    drone.streamon()
    while True:
        asdf = 42

def initiate_tello(drone):
    tello.enable_mission_pads()
    tello.set_mission_pad_detection_direction(2)  # forward detection only

    tello.takeoff()

    pad = tello.get_mission_pad_id()

    print(pad)
    # # detect and react to pads until we see pad #1
    while pad != 2:
        tello.move_forward(20)
        pad = tello.get_mission_pad_id()
        pad_dx = tello.get_mission_pad_distance_x()
        pad_dy = tello.get_mission_pad_distance_y()
        pad_dz = tello.get_mission_pad_distance_z()
        print(f'Pad ID: {pad}. dX = {pad_dx} | dY = {pad_dy} | dZ = {pad_dz}')
        if pad == 2:
            tello.go_xyz_speed(pad_dx, pad_dy, pad_dz, 10)
            print("Stopping now. I'm done.")
            break


    # graceful termination
    tello.disable_mission_pads()
    tello.land()
    tello.end()

tello = Tello("192.168.1.25")
#tello.connect()

#initiate_tello(tello)
drone_zone(tello)
