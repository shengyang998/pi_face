import myfunctions as myf
from CalculateFPS import CalculateFPS, DoEach
from multiprocessing import Pool, Array
print("Importing OpenCV")
import cv2
print("OpenCV imported")
import sys


def convert_BGR_to_RGB(BGR_frame):
    return BGR_frame[:, :, ::-1]


def set_width_height(cap):
    cap.set(3, 160)  # set Width
    cap.set(4, 120)  # set Height
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
    counter = 0
    doeach = DoEach(times=1)
    with Pool(processes=4) as pool:
        while True:
            counter += 1
            frame = capture_read(cap)
            cv2.imshow('frame', frame)
            # MARK: Reshape is needed, waiting to go on
            # frame = Array('i', frame.reshape(-1), lock=False)
            doeach.do_async(pool, recognize, arg=frame)
            print("FPS: {0}".format(calculate_fps.calculte()))
            print("Frame size: {0} KByte".format(sys.getsizeof(frame)/1024))
            wait()  # Hit 'q' on the keyboard to quit!


def release_resources(cap):
    print("Releasing Video Capture")
    cap.release()
    print("Video Capture Released")
    cv2.destroyAllWindows()
    print("Resources is all retrieved. Will now quit.")


def main():
    print("Capturing Video")
    cap = config_capture()
    try:
        capturing(cap)
    except KeyboardInterrupt:
        print("OK, Retrieving resources before quit")
    # except Exception as e:
    #     print("An error occurred: {0}".format(e))
    #     pass
    finally:
        release_resources(cap)


if __name__ == "__main__":
    main()
