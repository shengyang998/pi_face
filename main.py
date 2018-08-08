print("Importing OpenCV")
import cv2
print("OpenCV imported")
import numpy as np
import myfunctions as myf


def convert_BGR_to_RGB(BGR_frame):
    return BGR_frame[:, :, ::-1]


def config_capture():
    cap = cv2.VideoCapture(0)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height
    cap.set(cv2.CAP_PROP_FPS, 0.1)
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


def capturing(cap):
    while(True):
        frame = capture_read(cap)
        cv2.imshow('frame', frame)
        recognize(frame)


def main():
    print("Capturing Video")
    cap = config_capture()
    try:
        capturing(cap)
    except KeyboardInterrupt:
        print("OK, Retrieving resources before quit")
        print("Releasing Video Capture")
        cap.release()
        print("Video Capture Released")
        cv2.destroyAllWindows()
        print("Resources is all retrieved. Will now quit.")
    except Exception as e:
        print("An error occured: {0}".format(e))
        print("Releasing Video Capture")
        cap.release()
        print("Video Capture Released")
        cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
