# piHDR
Scripts for capturing and processing HDR images on a raspberry pi
  
Dependencies include:
* Radiance (pfilt, evalglare, pcond, falsecolor, ra_tiff http://www.radiance-online.org/)
* genHDR (http://www.anyhere.com/)
* python
* picamera

How to use:  
execute `./run_hdrcapture.bsh` to capture exposure bracketed jpgs, create an HDR image, calculate glare metrics, crate a falsecolor image, and create a tone-mapped image.  
### Using cron to schedule regular captures. ###
Use `crontab -e` to edit crontab file
  
To capture an hdr image every 5 minutes between 8AM and 7PM on weekdays, add this to the file crontab file:
```
*/5 8-19 * * 1-5  bash /home/pi/piHDR/run_hdrcapture.bsh
```

Make sure the pi is set to auto login to the user with the crontab file.


Watchits:
* Make sure your camera module is enabled using raspi-config
* Make sure you have the python library picamera
* Set the field of view variables in run_hdrcapture.bsh for your camera + lens combo
* Make sure the path to piHDR in run_hdrcapture.bsh is valid.

 
