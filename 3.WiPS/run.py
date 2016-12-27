import urequests
import time
scan=sta_if.scan()
for item in scan:
    print(item[0])
