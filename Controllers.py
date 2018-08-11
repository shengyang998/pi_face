import sys
import face_recognition as face_r
from os import listdir
from functools import lru_cache

print("Importing OpenCV")
import cv2
print("OpenCV imported")


class CVController:

    cap = None
    shape_of_frame = None
    should_show = None
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            # cls.instance = object.__new__(cls, *args)
            cls._instance = super(CVController, cls).__new__(cls, *args, **kw)
        return cls._instance

    def show_frame_with_name(self, frame, name):
        if self.should_show is True:
            cv2.imshow(name, frame)

    def convert_BGR_to_RGB(self, BGR_frame):
        return BGR_frame[:, :, ::-1]

    def set_width_height(self, width, height):
        self.cap.set(3, width)  # set Width
        self.cap.set(4, height)  # set Height

    def config_capture(self, width, height, should_show=True):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.should_show = should_show
        self.set_width_height(width, height)

    @staticmethod
    def fix_camera_direction(frame):
        return cv2.flip(frame, 1)

    def capture_read_show(self, name):
        _, frame = self.cap.read()
        frame = self.fix_camera_direction(frame)
        self.show_frame_with_name(frame, name=name)
        # self.set_shape(frame)
        return frame

    def set_shape(self, frame):
        if self.shape_of_frame is None:
            self.shape_of_frame = frame.shape

    def get_face_locations(self, frame):
        return face_r.face_locations(frame)

    def get_face_encodings(self, frame):
        return face_r.face_encodings(frame, self.get_face_locations(frame))

    @staticmethod
    def wait(key='q'):
        if cv2.waitKey(1) & 0xFF == ord(key):
            exit(0)

    def release_resources(self):
        print("Releasing Video Capture")
        self.cap.release()
        print("Video Capture Released")
        cv2.destroyAllWindows()
        print("All resources are retrieved. Will now quit.")


class Recognition:

    @classmethod
    def load_images(cls, path="."):
        pictures = []
        image_file_names = [ f for f in listdir(path) if f.endswith(".jpg") ]
        for img_name in image_file_names:
            face_image = face_r.load_image_file("{0}/{1}".format(path, img_name))
            img_name = " ".join(img_name.split('.')[:-1])
            pictures.append( (img_name, face_image) )
        return pictures

    @classmethod
    @lru_cache(maxsize=32)
    def get_whitelist_faces(cls, whitelist_dir="./WhiteList"):
        pictures = cls.load_images(whitelist_dir)
        faces = []
        for i in pictures:
            faces.append( (i[0], face_r.face_encodings(i[1])[0]) )
        return faces

    @classmethod
    def get_faces(cls, image):
        return face_r.face_encodings(image)

    @classmethod
    def get_name_from_result(cls, results):
        return cls.get_whitelist_faces()[results.index(True)][0]

    @classmethod
    def is_in_white_list(cls, face):
        if face is None or face == []:
            return
        results = face_r.compare_faces([ f[1] for f in cls.get_whitelist_faces() ], face[0])
        if True not in results:
            print("Attention: face not in white list")
            sys.stdout.flush()
            return False
        else:
            name = cls.get_name_from_result(results)
            print("This is {0}'s face.".format(name))
            print("Welcome back, {0}!".format(name))
            sys.stdout.flush()
            return True
