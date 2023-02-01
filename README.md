# EdgeComputing
This project aims to deploy a TensorFlow lite model into TTGO T-Camera ESP32 WROVER using Micropython. The approach is suitable for beginners willing to deploy a simple human detection model in Tensorflow lite framework. <br />
This project was based on @moclieri  https://github.com/mocleiri/tensorflow-micropython-examples.git and thanks to @uraich https://github.com/uraich/EdgeComputing/tree/main/firmware for fixing the camera module issues presented in the recent MicroPython firmware. For more information please visit their respository. <br />
 
# Instructions
Any Python compiler should work with this project. 
However, this guide will use the latest Thonny IDE version as an intuition for new users, visit https://thonny.org/.<br /> <br />
Click tools and go to option, set the interpreter to ESP32 micropython and select your ESP port.<br />
Next click on 'Install or update Micropython' on bottom right of the window.<br /> 

<img src="https://user-images.githubusercontent.com/37290558/216077119-3222619c-a5c7-43d0-83e1-f48bf03b8a50.png">
<br />
<br />

Upload the firmware bin, the file can be found inside firmware folder with .bin extension <br /> 
<img src="https://user-images.githubusercontent.com/37290558/216079469-459d8627-3502-4b05-8a4c-109652592622.png">
<br /> 

