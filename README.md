# PiZero Setup
## Format your SD card: 

```
https://www.sdcard.org/downloads/formatter_4/
```

Download the latest Raspbian image
```
https://www.raspberrypi.org/downloads/
```

Open terminal
NOTE: In my system show 'disk4s1' is the sd card, this can be different from yours.
Check for sd card location run
```
$ df -h
``` 	

Record the SD card location (ex:/dev/disk4s1) and type:
```
$ diskutil unmount /dev/disk4s1 
```

Copy the image to your sd card run (take about 10 minutes or less)
```
$ sudo dd bs=1m if=~/Downloads/piZero/RaspianImage/2017-07-05-raspbian-jessie.img of=/dev/rdisk4 (make sure the rdisk4 not disk4s1)
```

Eject your SDCard 

## Configure Pi
Login with default id/password:

```
username:pi, password:raspberry
```
To change password:

```
$ passwd
```
Update/Upgrade:

```
$ sudo apt-get update
$ sudo apt-get upgrade
```
Disable Blutooth:

```
$ sudo nano /boot/config.txt
```
Add this line at the end of the file

```
“dtoverlay=pi3-disable-bt” 
```
Run a quick reboot 

```
$ sudo reboot
```
Enable SSH

```
$ sudo raspi-config
	Interface -> SSH -> Enable -> Yes -> Finish
```
Common Error when SSH:

```
“ECDSA host key for 192.168.0.45 has changed and you have requested strict checking.
Host key verification failed.”
```
Fix:

```
$ ssh-keygen -R 192.168.0.99
```
## Install Node and NPM:
Link: https://github.com/sdesalas/node-pi-zero

Open terminal from pi zero:
```
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v6.9.1.sh | bash
```

Check node version:
```
$ node -v
$ npm -v
```

Copy file/folder from Mac to your Pi:
Copy a file:
```
scp ~/Desktop/piZero/server.js pi@[pi-ipaddress]:~/IPS
```
Copy a folder:
```
scp -r ~/Desktop/piZero/ pi@[pi-ipaddress]:~/IPS
```

## Install Dependencies

From your pi open terminal:
```
$ mkdir ProjectFolder
$ npm init
$ sudo npm install kalmanjs express sylvester http body-parser optimized-averages
```




















