# Face Recognition
This is a python script for Face Recognition with multiporocessing

# Prerequisites
- A Computer
- A Camera
- The appropriate Driver of the Camera
- [Python3.x](http://python.org/)
- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
    - for *face_recognition*, you need `dlib` install on your system
        if the recognition takes too much time, you should consider compile dlib by yourself
- [dlib](https://github.com/davisking/dlib)
    - [The installation guide of dlib](./dlib_installation.md)

# Tools for checking pipeline size on your system:
The *nix platform use pipeline for different process to exchange information.
However, pipeline should not use for large file, so if your resolution so high that cause a performance issue, you may want to change the code from passing frame to pipeline to passing multiprocessing.Array to pipeline (which I don't have time to implement right now). 
To check your pipeline size: 
```shell
/bin/bash -c 'for p in {0..18}; do ./test_pipe_size.sh $((2 ** $p)) 0.5; done'
```
