## How to Install MicroPython on ESP8266

Install UART Driver [here](http://www.silabs.com/products/mcu/pages/usbtouartbridgevcpdrivers.aspx)

Install Python and Pip [[Mac OS](https://github.com/jordy33/turbogears_tutorial/wiki/Installing-Python-and-pip-in-Mac-OSx)] [[Linux](https://github.com/jordy33/turbogears_tutorial/wiki/Installing-Python-and-pip-in-Ubuntu)] 

Install a virtual environment [[Mac OS](https://github.com/jordy33/turbogears_tutorial/wiki/Creating-Virtual-Environment-Mac-OS)] [[Linux](https://github.com/jordy33/turbogears_tutorial/wiki/Create-Virtual-Environment-(Linux))]

### Create Virtual Environment or activate it (if you have one):

```objc
mkvirtualenv esp8266
(if you already have created this environment before) activate with:
workon esp8266 
```
### Install ESPtool:

```objc
pip install esptool
```
Wire ESP8266 to enable Flash mode
![](https://github.com/jordy33/esp8266-Micropython/blob/master/x.images/ESPflashingmode.jpg?raw=true)

### Flash Micropython on the ESP8266

```objc
Go to the subdirectory from this repository: 1.FlashFirmware
execute shell files in this order:
erasechip.sh
<Turn off/on esp8266>
flash2mem.sh
```

### Put ESP8266 in normal operation mode
![](https://github.com/jordy33/esp8266-Micropython/blob/master/x.images/ESPoperationmode.png?raw=true)
```objc
It is better to use pull up resistor with GPIO0 in ESP8266 ESP-01
In ESP8266, GPIO0 has two two functionalities.

Low state: To keep the ESP8266 in firmware flash mode 
High state: To keep the ESP8266 in normal working mode
Open state: Works same as High state

Problem in keeping the GPIO0 in open state: Sometimes during boot, the device do not recognize GPIO0 as high/Low state and the device do not boot up properly.

Solution: while working in normal mode, use 1K resister with GPIO0 and make it high by connecting with power supply.
``` 

### Access Repl: (read-eval-print-loop)

On a Mac  

Search your serial port with: ls /dev/cu.*
Access the repl with 
```objc
screen /dev/cu.SLAB_USBtoUART 115200
```
If you are in ubuntu search your serial port with : 
```objc
ls /dev
```
Typically in  Linux use the following serial port: /dev/ttyUSB0

Grant permission to access the port: 
```objc
sudo usermod -a -G dialout $USER
sudo reboot
```
Install Gtkterm
```objc
sudo apt-get install gtkterm
sudo gtkterm
```

Select port /dev/ttyUSB0
Select baud rate to 115200

### Congratulations!! you must see the Repl:
```objc
MicroPython v1.8.6-7-gefd0927 on 2016-11-10; ESP module with ESP8266
Type "help()" for more information.
>>> 
```
You must able to interact with your module. Type help() to get help

In order to access Micropython file system you must install AMPY

### How to Install Ampy

```objc
pip install adafruit-ampy
```
If you are on MAC OS edit .bash_profile at ~ (home directory) 
and add at the end the following line:
```objc
export AMPY_PORT=/dev/tty.SLAB_USBtoUART
```
If you are on Ubuntu edit .bashrc at ~ (home directory) 
and add at the end the following line:
```objc
export AMPY_PORT=/dev/ttyUSB0
```

Commands:
```objc
Commands:
  get  Retrieve a file from the board.
  ls   List contents of a directory on the board.
  put  Put a file on the board.
  rm   Remove a file from the board.
  run  Run a script and print its output.
```
Example:
```objc
ampy ls
ampy get main.py
ampy put boot.py boot.py
ampy rm foo.py
ampy run test.py
```
