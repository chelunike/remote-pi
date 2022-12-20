# remote-pi
Remote control raspberry pi by web internaface. Just required stay on same network.
Principal Idena:
 - Get Camera Image
 - Control Serial Terminal (for arduino)
 - Other stuff: display some data and some functions


## Camera Transmission

We need to locate our camera device. For example: `/dev/video0`.

### Camera setup

There are a few alternatives to install a camera on raspberry pi depending of what you have. Here explain a few ways.

#### "Ofical" Rapberry Pi Camera
Or at least anything you can connect directly to the raspberry pi.
You should enable this function from: 
```
	raspi-config
```

#### Usb Webcam or Makeshift usb camera
You can connect via usb a webcam and just install the correct drivers.

#### Phone camera with Droidcam
There is a project for use yours mobile camera as a normal camera.



## Install Dependencies

```
   pip install requirements.txt 
```

## Run server
```
    python main.py
```
