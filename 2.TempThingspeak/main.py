# creating objects
from bmp180 import BMP180
from machine import I2C, Pin
import urequests
import time
print("start")
while True:
    bus =  I2C(scl=Pin(2), sda=Pin(0), freq=100000)
    bmp180 = BMP180(bus)
    bmp180.oversample_sett = 2
    bmp180.baseline = 101325

    api_key='WRNYXJXBZO2PUMLK'
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    data={}

    temp = bmp180.temperature
    p = bmp180.pressure
    altitude = bmp180.altitude
    print(temp, p, altitude)
    url = 'http://api.thingspeak.com/update?key={}&field1={}&field2={}&field3={}'.format(api_key, str(temp), str(p),str(altitude))
    resp = urequests.post(url, data=data,headers=headers)
    resp.close()
    time.sleep(300)


