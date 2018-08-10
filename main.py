from Controllers import *
from EachEvents import CalculateFPS, DoEach
from multiprocessing import Pool, Array


def capture_recognition(cv):
    calculate_fps = CalculateFPS()
    counter = 0
    doeach = DoEach(times=5)
    with Pool(processes=4) as pool:
        while True:
            counter += 1
            frame = cv.capture_read()
            cv.show_frame_with_name(frame=frame, name='frame')
            # MARK: Reshape is needed for multiprocessing.Array
            frame = Array('i', frame.reshape(-1), lock=False)
            doeach.do_async(pool, cv.recognize, arg=frame)
            # MARK: Status Checking
            # print("FPS: {0}".format(calculate_fps.calculte()))
            # print("Frame size: {0} KByte".format(sys.getsizeof(frame)/1024))
            cv.wait()  # Hit 'q' on the keyboard to quit


def main():
    print("Capturing Video")
    cv = CVController()
    cv.config_capture(width=640, height=480)
    try:
        capture_recognition(cv)
    except KeyboardInterrupt:
        print("OK, Retrieving resources before quit")
    # except Exception as e:
    #     print("An error occurred: {0}".format(e))
    #     pass
    finally:
        cv.release_resources()


if __name__ == "__main__":
    main()
