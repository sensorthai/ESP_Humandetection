<img src = "https://user-images.githubusercontent.com/37290558/216087644-acc8a249-bfc4-49f4-9eab-2856729b6a4c.png" width='50%'/> <br />

# About this respository
This project aims to deploy a TensorFlow lite model into TTGO T-Camera ESP32 WROVER using Micropython. The given approach use Thonny as a Python IDE to install the firmware and compile the scripts. <br />
This project was based on @moclieri  [https://github.com/mocleiri/tensorflow-micropython-examples.git](https://github.com/mocleiri/tensorflow-micropython-examples/tree/main/examples/person_detection) and thanks to @uraich https://github.com/uraich/EdgeComputing/tree/main/firmware for fixing the camera module issues presented in the recent MicroPython firmware. For more information please visit their respository. <br />
 
# Uploading firmware into ESP32
Any Python compiler should work with this project. <br /> 
However, this guide will use the latest Thonny IDE version as an intuition for new users, visit https://thonny.org/.<br /> <br />
Click tools and go to option, set the interpreter to 'Micropython (ESP32)' and select your ESP port.<br />
Next click on 'Install or update Micropython' on the bottom right of the window.<br /> 

<img src="https://user-images.githubusercontent.com/37290558/216077119-3222619c-a5c7-43d0-83e1-f48bf03b8a50.png"> <br /><br />

Upload the firmware bin. The file can be found inside the firmware folder with .bin extension <br /> <br />
> Thanks @uraich again for the recent fix with the given firmware. <br /><br />
<img src="https://user-images.githubusercontent.com/37290558/216079469-459d8627-3502-4b05-8a4c-109652592622.png"> <br /> <br /> 

Once the firmware is uploaded, press the boot button to reset ESP32 and test the firmware by importing the given library. <br /> 
All imports should not raise any errors. <br /> <br />
<img src = "https://user-images.githubusercontent.com/37290558/216085798-f03d6867-c657-4eb9-ad8e-3d39111771d0.png"> <br /> <br /> 

# Compiling the scripts
Upload all files in 'Micropython-scripts' folder into ESP-32.<br />  
> If 'device is busy' reset the ESP-32 by pressing the rst button, or interupt Thonny's backend by pressing ctr+c.<br />


Run the program
> If there is an 'Error when initializing the camera', simply reset your ESP32.<br />

