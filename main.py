import numpy as np
import myfunctions as myf
from CalculateFPS import CalculateFPS, DoEach
from multiprocessing import Pool
print("Importing OpenCV")
import cv2
print("OpenCV imported")


def convert_BGR_to_RGB(BGR_frame):
    return BGR_frame[:, :, ::-1]


def set_width_height(cap):
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height
    return cap


def config_capture():
    cap = cv2.VideoCapture(0)
    cap = set_width_height(cap)
    return cap


def fix_camera_direction(frame):
    return cv2.flip(frame, 1)


def capture_read(cap):
    _, frame = cap.read()
    frame = fix_camera_direction(frame)
    return frame


def get_face_locations(frame):
    return myf.face_r.face_locations(frame)


def get_face_encodings(frame):
    return myf.face_r.face_encodings(frame, get_face_locations(frame))


def recognize(frame):
    rgb_frame = convert_BGR_to_RGB(frame)
    face = get_face_encodings(rgb_frame)
    return myf.is_face_in_white_list(face)


def async_recognize(pool, frame):
    pool.apply_async(recognize(frame))


def wait(key='q'):
    if cv2.waitKey(1) & 0xFF == ord(key):
        exit(0)


def capturing(cap):
    calculate_fps = CalculateFPS()
    doeach = DoEach(times=5)
    with Pool(processes=3) as pool:
        while True:
            frame = capture_read(cap)
            cv2.imshow('frame', frame)
            doeach.do_async(pool, recognize, args=[frame])
            print("FPS: {0}".format(calculate_fps.calculte()))
            wait()  # Hit 'q' on the keyboard to quit!

def release_resources(cap):
    print("Releasing Video Capture")
    cap.release()
    print("Video Capture Released")
    cv2.destroyAllWindows()


def main():
    print("Capturing Video")
    cap = config_capture()
    try:
        capturing(cap)
    except KeyboardInterrupt:
        print("OK, Retrieving resources before quit")
        release_resources(cap)
        print("Resources is all retrieved. Will now quit.")
    except Exception as e:
        print("An error occured: {0}".format(e))
        release_resources(cap)


if __name__ == "__main__":
    main()
