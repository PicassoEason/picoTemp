import utime
import random
from machine import I2C, Pin, ADC
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


I2C_ADDR     = 63
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
Lama= bytearray([0x00,0x02,0x07,0x06,0x0E,0x0E,0x0A,0x00])
badsmile= bytearray([0x1F,0x1F,0x04,0x1F,0x1B,0x1F,0x11,0x1F])
dog= bytearray([ 0x00,0x00,0x06,0x0A,0x0A,0x07,0x05,0x00])
hert= bytearray([ 0x00,0x0A,0x1F,0x1F,0x1F,0x1F,0x0E,0x04])

def read_temp():
    sensor_temp = ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    formatted_temperature = "{:.2f}".format(temperature)
    string_temperature = str("Temp:" + formatted_temperature)
    print(string_temperature)
    utime.sleep(1)
    return string_temperature
  

while True:
    temperature = read_temp()
    lcd.move_to(0,0)
    lcd.putstr(temperature)
    utime.sleep(1)
    lcd.clear()
#草尼瑪
    for i in range(0,4,1):
        lcd.clear()
        lcd.move_to(i,random.randint(0,1))
        lcd.custom_char(0,Lama)
        lcd.putchar(chr(0))
        utime.sleep(0.1)
        lcd.clear()
#土狗
    for i in range(4,7,1):
        lcd.clear()
        lcd.move_to(i,random.randint(0,1))
        lcd.custom_char(0,badsmile)
        lcd.putchar(chr(0))
        utime.sleep(0.1)
        lcd.clear()
#puppy   
    for i in range(7,10,1):
            lcd.clear()
            lcd.move_to(i,random.randint(0,1))
            lcd.custom_char(0,dog)
            lcd.putchar(chr(0))
            utime.sleep(0.1) #顯示速度
            lcd.clear()
#love   
    for i in range(10,16,1):
            lcd.clear()
            lcd.move_to(i,random.randint(0,1))
            lcd.custom_char(0,hert)
            lcd.putchar(chr(0))
            utime.sleep(0.1)
            lcd.clear()