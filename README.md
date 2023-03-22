
請確保
SDA 連在 1
SCL 連在 2
並啟動MAIN(getTemp.py)程式
Raspberry Pico 練習
==


1. 使用 Thonny 將 blink (內建LED燈閃爍) 程式燒錄到 Pico
2. 使用 Pico + 1602 LCD 顯示內建溫度感測器讀取到的溫度資料
3. 使用 Raspberry Pi 燒錄/除錯 Pico 程式(All)
![](https://i.imgur.com/C09WwSI.jpg)
* getTemp.py 
* 取溫度程式
```Python=
import utime
from machine import I2C, Pin, ADC
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
I2C_ADDR     = 63
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
def read_temp():
    sensor_temp = ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    formatted_temperature = "{:.2f}".format(temperature)
    string_temperature = str("Temp:" + formatted_temperature)
    print(string_temperature)
    utime.sleep(2)
    return string_temperature
while True:
    temperature = read_temp()
    lcd.move_to(0,0)
    lcd.putstr(temperature)
```

4. 使用 VSCode 搭配 Pico 開發 MicroPython 程式
![](https://i.imgur.com/8RmvIhI.png)

![](https://i.imgur.com/ez2V7OS.jpg)
