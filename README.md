# Face-Landmark-Detector
## Issues may occur while installing dlib
Often there is a problem while installing dlib. Mostly you found that on internet they show the way in which you have to install dlib and then have to create binary using cmake. This is the way in which you have to install source code and compiled by your own.

### The second way
The second way is to install using [pip](https://pip.pypa.io/en/stable/)
```bash
pip install dlib
``` 
but sometime this also won't work.
### The ninja technique
 So the ninja technic to install dlib is to go to this website https://pypi.org/simple/dlib
 Then install a wheel file according to your system and python version.
 Next fire up your terminal and goto directory in which that wheel file is installed.
 Now type 
 ```bash 
 pip install <file name.whl>
 ```
