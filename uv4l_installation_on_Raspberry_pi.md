```shell
sudo apt-get update
sudo apt-get install -y uv4l uv4l-raspicam uv4l-raspicam-extras
uv4l --driver raspicam --auto-video_nr --encoding yuv420
sudo echo "/usr/lib/uv4l/uv4lext/armv6l/libuv4lext.so" >> /etc/ld.so.preload  # notice that armv6l is your architecture platform, you may need to change it
```