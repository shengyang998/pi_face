# Face Recognition
This is a python script for Face Recognition with multiporocessing

# Usage
```shell
pip3 install -U face_recognition
git clone --depth=1 https://github.com/shengyang998/pi_face
python3 main.py
```

# Prerequisites
- A Computer
- A Camera
- The appropriate Driver of the Camera
- [Python3.x](http://python.org/)
- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
    - for *face_recognition*, you need `dlib` installed on your system
        if the recognition takes too much time, you should consider compile dlib by yourself
- [dlib](https://github.com/davisking/dlib)
    - [The installation guide of dlib](./dlib_installation.md)

# Tools for checking pipeline size on your system:
The *nix platform use pipeline to exchange information in different processes.
However, pipeline should not use for exchanging large file, so if your resolution so high that could cause a performance issue, you may want to change the code from passing frame to pipeline to passing multiprocessing.Array to pipeline (which I haven't implemented). 
To check your pipeline size: 
```shell
git clone --depth=1 https://github.com/shengyang998/pi_face
/bin/bash -c 'for p in {0..18}; do ./test_pipe_size.sh $((2 ** $p)) 0.5; done'
```
