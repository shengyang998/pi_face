from Controllers import *
from EachEvents import CalculateFPS, DoEach
from multiprocessing import Pool, Array


def recognize(frame):
    # frame = frame.reshape(cls.shape_of_frame)
    rgb_frame = CVController.convert_BGR_to_RGB(frame)
    face = CVController.get_face_encodings(rgb_frame)
    return Recognition.is_in_white_list(face)


def capture_recognition(controller):
    calculate_fps = CalculateFPS()
    doeach = DoEach(times=20)
    with Pool(processes=4) as pool:
        while True:
            frame = controller.capture_read_show(name='frame')
            # MARK: Reshape is needed for multiprocessing.Array. However doing so will cause lock, to be continue...
            # frame = Array('i', frame.reshape(-1), lock=False)
            doeach.do_async(pool, recognize, arg=frame)
            # MARK: Status Checking
            # print("FPS: {0}".format(calculate_fps.calculte()))
            # print("Frame size: {0} KByte".format(sys.getsizeof(frame)/1024))
            CVController.wait()  # Hit 'q' on the keyboard to quit


def main():
    print("Capturing Video")
    cv = CVController()
    cv.config_capture(width=160, height=120, device_code=0, should_show=False)
    try:
        capture_recognition(cv)
    except KeyboardInterrupt:
        print("OK, Retrieving resources before quit")
    finally:
        cv.release_resources()


if __name__ == "__main__":
    main()
