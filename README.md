# light_controller

Controller for the Luminoodle Professional Bias Lighting strip. Could easily be modified to work as controller for any RF remote, or with a bit more modification, for any IR remote.

Uses an Arduino and a 433MHz transmitter. In order to clone the codes from a different remote, you will need a 433MHz receiver.

A setup.py file is included so that you can use cx_Freeze to create a .exe to run the controller. To use it, make sure cx_Freeze is installed:
```
pip install cx_Freeze
```
Now run the following to create the .exe:
```
python setup.py build
```
