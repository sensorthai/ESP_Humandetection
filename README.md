<img src = "https://user-images.githubusercontent.com/37290558/216087644-acc8a249-bfc4-49f4-9eab-2856729b6a4c.png" width='50%'/> <br />

# About this respository
This project aims to deploy a TensorFlow lite model into TTGO T-Camera ESP32 WROVER using Micropython. The given approach use Thonny as a Python IDE to install the firmware and compile the scripts. <br />
This project was based on @moclieri https://github.com/mocleiri/tensorflow-micropython-examples/tree/main/examples/person_detection and thanks to @uraich https://github.com/uraich/EdgeComputing/tree/main/firmware for fixing the camera module issues presented in the recent MicroPython firmware. For more information please visit their respository. <br />
 
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

<img src = "https://user-images.githubusercontent.com/37290558/216365255-ff58276d-d754-446c-b1cd-58e7184dcb05.png">

Run main.py script
> If there is an 'Error when initializing the camera', simply reset your ESP32.<br />

# About the scripts
To write and update the SSD1306 OLED screen, a function with three input parameters was used. <br />
The first input is a string variable which displays text into OLED screen. <br />
Second input positions the texts in x-direction(horizontal) of the OLED screen.  <br />
Third input was used to position the texts in y-direction(vertical) of the OLED screen. <br /><br />
<img src = "https://user-images.githubusercontent.com/37290558/216828890-1bf7c724-d4cf-4c4b-ba7c-ad05525f50a2.png"> <br />

Thanks to Random Nerd Tutorials for providing the SSD1306 OLED display file, for more information please visit their site https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/ <br /> <br />


Since I'm using TTGO T-Camera ESP32 WROVER, the camera pins was assign as followings. Please check your camera pins accordingly. <br />
> If an 'Error when initializing the camera' still persisted after resetting esp32, please check your camera pins. <br /> <br />

<img src = "https://user-images.githubusercontent.com/37290558/216828227-13d9b565-2398-42e7-a6c1-f79b5e8a57d9.png"> <br /> <br />


Input_callback function setup bytes for an input Tensor. In other words it prepares the input picture captured by the camera to be used with AI model. <br />
<img src = "https://user-images.githubusercontent.com/37290558/216828407-b22152f7-6cef-4bf0-855b-7d8431ba32b5.png"> <br /> <br />

Output_callback function retrives AI condfidence values and print them to OLED screen. Microlite Outputs a Tensor value in signed 8-bit integer, namely from
-128 to 127. We will convert this in a more readable manner, from 0 to 100 % instead. <br />
If the confidence values is more than or equal to 52 %, change the color of the screen to white and display 'Person found!'<br />
If no person is found or confidence is below 52 %, flip the screen's color the black and display 'No person found' <br />
<img src = "https://user-images.githubusercontent.com/37290558/216828633-094d7599-af97-4dee-87ab-34da3b453a89.png"> <br /> <br />


This sections primarily opens and prepares the Tensorflow-Lite model to be used in the program. The bytearray in line 58 depends on the size of the model. <br />
microlite interpreter in line 63 has 4 input paramters.<br />
> Size of the input model, in this case we already prepares the model in previous section. <br />
> Memory space for inferencing the Tensorflow-Lite model, again this depends greatly on the size of the model. <br />
> Callback function for input tensor. <br />
> Callback fucntion for the output tensor. <br />

<img src = "https://user-images.githubusercontent.com/37290558/216828319-eb244890-f107-4aae-9b87-08a098b9e20e.png"> <br /> <br />


In the main loop the program runs as followings: <br />
1. Get machine time in seconds, use for calculating FPS. <br />
2. Use the camera to capture an image. <br />
3. Get ouput from the AI in accordance with the captured image. <br />
4. Display FPS value on the bottom of the OLED screen. <br />
5. Reset OLED screen so it can be updated with new texts/values. <br />

<img src = "https://user-images.githubusercontent.com/37290558/216828682-bc0428ac-af3d-4c1b-8d34-4941b5d0b294.png"> <br /> <br />

# Credits
Thanks to @moecleiri for providing the scripts and firmware for this respository https://github.com/mocleiri/tensorflow-micropython-examples/tree/main/examples/person_detection. <br />
Thanks to @uraich https://github.com/uraich/EdgeComputing/tree/main/firmware for fixing the camera module issues presented in the recent MicroPython firmware. <br />
Thanks to Random nerd tutorial again for providing SSD1306 OLED screen Micropython file. https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/.
