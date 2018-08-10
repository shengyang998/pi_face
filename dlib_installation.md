# The installation guide of dlib
If you meet performance problem with face recognition, you should consider compile dlib by yourself and reinstall it.
As the [website](http://dlib.net/compile.html) said, the compilation of dlib is simple.
However, I found it quiet annoying compiling on portable computer device like Raspberry Pi due to the insufficient capacity of physical memory.
Here's solution that I've found.

## On Usual *nix device

```shell
cd examples
mkdir build
cd build
cmake ..
cmake --build . --config Release
cd ../../
python setup.py install
```


## On Portable Computer (like Raspberry Pi)

You should run the same code like above. Before that, however, you should change your swap size setting:
```shell
sudo vi /etc/dphys-swapfile
```
change the `CONF_SWAPSIZE` from 100 to 2048. If you don't have 2048 MBytes, then 1024 also should work, just for in case.

Then, make sure you have enough space on your hard drive.
```shell
cd /var
sudo dd if=/dev/zero of=./swap2 bs=1024 count=2048000  # Will write 2G of zeros to file swap2, change the size if you want
sudo mkswap ./swap2
sudo swapon ./swap2
sudo /etc/init.d/dphys-swapfile restart
```

Now you can start building and leave for your coffee or something, it will take about 2 hours (at lease in my case).

:coffee:
:coffee:
:coffee:

If you finish the compilation procedure and you want to change your swap size back:
```shell
sudo vi /etc/dphys-swapfile
```
and change `CONF_SWAPSIZE` to whatever you need, default is 100
then
```shell
sudo swapoff /var/swap2
sudo rm /var/swap2
sudo /etc/init.d/dphys-swapfile restart
```
