# Run the person detection model
# This version reads the images from the ov2640 camera on the esp32-cam board
# with minor changes this also works for the m5 timer camera
import sys
import camera
import microlite
import time
from machine import Pin, SoftI2C
import ssd1306 #screen

i2c = SoftI2C(scl=Pin(22), sda=Pin(21)) #set-up i2c communication for OLED screen
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

try:
    camera.init(0,format=camera.GRAYSCALE,framesize=camera.FRAME_96X96,
        sioc=23,siod=18,xclk=4,vsync=5,href=27,pclk=25,
        d0=34,d1=13,d2=14,d3=35,d4=39,d5=38,d6=37,d7=36)
except:
    print("Error when initializing the camera")
    sys.exit()

test_image = bytearray(9612) #created empty byte array to prepare image

#function to write into OLED screen and update text
def update_oled(input_txt, pos):  
    oled.text(input_txt, 0, pos)
    oled.show()

#loop through input picture and set tensor-value
def input_callback (microlite_interpreter):    
    inputTensor = microlite_interpreter.getInputTensor(0)
    for i in range (0, len(test_image)):
        inputTensor.setValue(i, test_image[i])
    print ("setup %d bytes on the inputTensor." % (len(test_image)))

#get output value from given picture and print into screen
def output_callback (microlite_interpreter):
    outputTensor = microlite_interpreter.getOutputTensor(0)
    person = outputTensor.getValue(1)  #output range from -128 to 127
    person = abs(round((person + 128) * 0.392))  #scale value above from 0 to 100
    not_a_person = 100 - person
    print ("'not a person' = %d, 'person' = %d" % (100 - person, person)) #print to screen for debug
    if person >= 52:  #if AI is 52% confident then change colour of OLED to white and update screen
        oled.invert(1)
        update_oled("Person " + str(person) + "%", 10)
    elif person < 52: #if AI is less than 52% confident change color of OLED to black and update screen
        oled.invert(0)
        update_oled("Not person "+ str(not_a_person) + "%", 10)

#read the model
person_detection_model_file = open ('person_detect_model.tflite', 'rb') 
person_detection_model = bytearray (300568)   #prepare empty byte model
person_detection_model_file.readinto(person_detection_model) #combined model together
person_detection_model_file.close() #close file to save memory

# create the interpreter
interp = microlite.interpreter(person_detection_model,136*1024, input_callback, output_callback) 

while True:
    program_runtime = time.time() #increase timer everyloop
    test_image = camera.capture() #capture image
    interp.invoke()  #invoke interpreter
    update_oled("Timer " + str(program_runtime), 50) #print program runtime duration
    update_oled("FPS " + str(1.0/(time.time() - program_runtime)), 20) #calculate FPS
    oled.fill(0) #Reset screen
camera.deinit() #Stop camera after program is interupted 
