# piHDR
Scripts for capturing and processing HDR images on a raspberry pi
  


### How to use:
execute `./run_hdrcapture.bsh` to capture exposure bracketed jpgs, create an HDR image, calculate glare metrics, crate a falsecolor image, and create a tone-mapped image.  
<br>
<br>

## Setting up dependencies
Dependencies include:
* Radiance (pfilt, evalglare, pcond, falsecolor, ra_tiff http://www.radiance-online.org/)
* genHDR (http://www.anyhere.com/)
* python
* picamera

### Using cron to schedule regular captures.
Use `crontab -e` to edit crontab file
  
To capture an hdr image every 5 minutes between 8AM and 7PM on weekdays, add this to the file crontab file:
```
*/5 8-19 * * 1-5  bash /home/pi/piHDR/run_hdrcapture.bsh
```
Make sure the pi is set to auto login to the user with the crontab file.

### Compiling Radiance for Raspberry Pi
```
sudo apt-get install tcsh
sudo apt-get install libx11-dev
wget http://www.radiance-online.org/software/snapshots/radiance-HEAD.tgz
wget http://www.radiance-online.org/download-install/radiance-source-code/latest-release/rad5R0supp.tar.gz
tar -xf radiance-HEAD.tgz
tar -xf rad5R0supp.tar.gz
cd ray
sudo ./makeall install
```

### Installing genHDR
```
wget http://www.anyhere.com/gward/pickup/hdrgen_AMDRaspian.tar.gz
tar -xf hdrgen_AMDRaspian.tar.gz
sudo mv hdrgen /usr/local/bin/.
sudo mv hdrcvt /usr/local/bin/.
```

### Enabling the camera module
```
sudo raspi-config
select "5 Interfacing Options"
select "P1 Camera"
select "Yes"

sudo reboot
```

### Disable Camera LED ###
The red LED on the camera module can affect your images, especially if you use clip on lenses. The instructions to disable the LED below come from this website: http://www.raspberrypi-spy.co.uk/2013/05/how-to-disable-the-red-led-on-the-pi-camera-module/
```
sudo nano /boot/config.txt
```
add the following:
```
disable_camera_led=1
```

###Watchits:###
* Make sure you have the python library picamera (you should)
* Set the field of view variables in run_hdrcapture.bsh for your camera + lens combo
* Make sure the path to piHDR in run_hdrcapture.bsh is valid.

 
