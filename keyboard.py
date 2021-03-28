import time
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.
adcY = Adafruit_ADS1x15.ADS1115()   #y-axis
adcX = Adafruit_ADS1x15.ADS1115()   #X-axis
adcSW = Adafruit_ADS1x15.ADS1115()  #Button

GAIN = 1


#adcY.start_adc(1,gain=GAIN)
#adcX.start_adc(2,gain=GAIN)
#adcSW.start_adc(3,gain=GAIN)


print('Press Ctrl-C to quit...')
while True:

        start =time.time()
        while(time.time() - start)<= 2.5:
                if(adcY.read_adc(1,gain=GAIN) >=25000):
                        print('joystick towards the user')
                if(adcX.read_adc(2,gain=GAIN) <=10000):
                        print('joystick right')
                if(adcX.read_adc(2,gain=GAIN) >=25000):
                        print('joystick left')
                if(adcSW.read_adc(3,gain=GAIN) ==0):
                        print('Button is pressed')
                #value = adcY.get_last_result()
                #print('Channel Y: {0}'.format(value))
                time.sleep(0.5)
