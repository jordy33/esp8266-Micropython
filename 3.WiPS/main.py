# WiFI Positioning System
import urequests
import time
import network
from ubinascii import hexlify

sta_if = network.WLAN(network.STA_IF)
scan=sta_if.scan()
list=[]
for item in scan:
    ssid=item[0].decode('utf-8')
    macaddress=hexlify(item[1]).decode('utf-8')
    bssid="{}{}-{}{}-{}{}-{}{}-{}{}-{}{}".format(*macaddress)
    channel=str(item[2])
    rssi=str(item[3])
    unknown=str(item[4])
    list.append(dict({'ssid':ssid,'bssid':bssid,'channel':channel,'rssi':rssi}))
url='https://maps.googleapis.com/maps/api/browserlocation/json?browser=firefox&sensor=true'
for item in list:    
    url=url+"&wifi=mac:{}|ssid:{}|ss:{}".format(item['bssid'],item['ssid'],item['rssi'])  
#print(url)
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
data={}
resp = urequests.get(url, data=data,headers=headers)
print(resp.json())
resp.close()

