import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time
import gettemp
import datetime
import RPi.GPIO as GPIO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#Testverdier
view=0
test_beerID="Mosaic P. Ale"
test_SG=1.021
test_OG=1.060
test_FG=1.006
target_temp=23
test_ABV=3.5

button1=11  # Input for knapp
button2=9   # Input for knapp

#Konfigurerer interrupt ved tastetrykk
def setmode0(pin):
    global view
    view=0 # Endre skjermvisning
def setmode1(pin):
    global view
    view=1 # Endre skjermvisning
GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button1, GPIO.RISING, callback=setmode0)
GPIO.add_event_detect(button2, GPIO.RISING, callback=setmode1)

#Initier display
DC=23
RST=None
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3c)
disp.begin()
disp.clear()
disp.display()

width=disp.width
height=disp.height
image=Image.new('1',(width, height))
draw=ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
font=ImageFont.load_default()
x=0
top=0


# Layout for display1
def disp1(temp, beerID, SG, target_temp):
    currentDT = datetime.datetime.now()
    temp=round(gettemp.gettemp(),2)
    draw.rectangle((0,0, width, height), outline=0, fill=0)
    draw.text((x, top), 'Brygg: {}'.format(beerID), font=font, fill=255)
    draw.line((x,12, width,12), fill=255)
    draw.text((x, top+14), "S.G: {:4.3f}".format(SG), font=font, fill=255)
    draw.text((x, top+24), "Temp: {}°".format(temp), font=font, fill=255)
    draw.text((x, top+34), "Target: {}°".format(target_temp), font=font, fill=255)
    draw.text((x, 54), currentDT.strftime("%Y-%m-%d %H:%M:%S"), font=font, fill=255)
    disp.image(image)
    disp.display()
    time.sleep(0.1)

# Layout for display2
def disp2(OG, FG, SG, ABV):
    draw.rectangle((0,0, width, height), outline=0, fill=0)
    draw.rectangle((8,height/2-6, width-8, height/2+6), outline=255, fill=0)
    draw.line((x,12, width,12), fill=255)
    draw.rectangle((8,height/2-5, 8+(OG-SG)/(OG-FG)*width-8, height/2+5), outline=255, fill=255)
    draw.text((x, 0), "Fremgang:", font=font, fill=255)
    draw.text((0, height/2+8), "{:4.3f}".format(OG), font=font, fill=255)
    draw.text((width-29, height/2+8), "{:4.3f}".format(FG), font=font, fill=255)
    draw.text((width/2-32, height/2+20), "ABV: {}%".format(ABV), font=font, fill=255)
    disp.image(image)
    disp.display()
    time.sleep(0.1)



try:

    while(1):
        currentDT = datetime.datetime.now()
        crt_date = currentDT.strftime("%Y-%m-%d %H:%M:%S")
        if view==0:
            disp1(round(gettemp.gettemp(),2), test_beerID, test_SG, target_temp)

        elif view==1:
            test_ABV=round(((test_OG-test_SG)/0.75)*100,2)
            disp2(test_OG, test_FG, test_SG, test_ABV)

except KeyboardInterrupt:
    print("Cleaning IOs")
    GPIO.cleanup()
finally:
    GPIO.cleanup
