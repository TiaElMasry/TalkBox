
import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from pynput.keyboard import Key, Controller


#for the keyboard
GPIO.setmode(GPIO.BCM)
keyboard = Controller()

# Create an ADS1115 ADC (16-bit) instance.
adcY = Adafruit_ADS1x15.ADS1115()   #y-axis
adcX = Adafruit_ADS1x15.ADS1115()   #X-axis
adcSW = Adafruit_ADS1x15.ADS1115()  #Button

GAIN = 1


#adcY.start_adc(1,gain=GAIN)
#adcX.start_adc(2,gain=GAIN)
#adcSW.start_adc(3,gain=GAIN)

start=0
print('Press Ctrl-C to quit...')
while True:

    start= time.time()
    while(time.time() - start)< 5:
        if(adcY.read_adc(1,gain=GAIN) >=25000):
            print('joystick towards the user')
            #keyboard.press(Key.down)
            #keyboard.release(Key.down)
        if(adcX.read_adc(2,gain=GAIN) <=10000):
            print('joystick right')
            keyboard.press(Key.ctrl_r)
            keyboard.release(Key.ctrl_r)
        if(adcX.read_adc(2,gain=GAIN) >=25000):
            print('joystick left')
            keyboard.press(Key.ctrl_l)
            keyboard.release(Key.ctrl_l)
        if(adcSW.read_adc(3,gain=GAIN) ==0):
            print('Button is pressed')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        time.sleep(0.5)
