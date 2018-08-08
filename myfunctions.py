import face_recognition as face_r
from os import listdir
from functools import lru_cache


def load_images(path="."):
    pictures = []
    image_file_names = [ f for f in listdir(path) if f.endswith(".jpg") ]
    for img_name in image_file_names:
        pictures.append( (img_name, face_r.load_image_file("{0}/{1}".format(path, img_name))) )
    return pictures


@lru_cache(maxsize=None)
def get_whitelist_faces(whitelist_dir="./WhiteList"):
    pictures = load_images(whitelist_dir)
    faces = []
    for i in pictures:
        faces.append( (i[0], face_r.face_encodings(i[1])[0]) )
    return faces


def get_faces(image):
    return face_r.face_encodings(image)


def is_face_in_white_list(face):
    if face == None or face == []:
        return
    results = face_r.compare_faces([ f[1] for f in get_whitelist_faces() ], face[0])
    if not True in results:
        print("Attention: face not in white list")
    else:
        print("This is {0}'s face.".format(get_whitelist_faces()[results.index(True)][0]))






















