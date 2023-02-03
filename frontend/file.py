from machine import Pin, PWM, ADC
import utime
import time
import network
import urequests
import ujson

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
xValueStored = xAxis.read_u16()
yValueStored = yAxis.read_u16()
jButton = Pin(22, mode=Pin.IN, pull=Pin.PULL_UP)
led17 = Pin(17, mode=Pin.OUT)

ssid = 'Erebor'
password = 'ce mot de passe est difficile'
wlan.connect(ssid, password)
url = "http://192.168.174.176:3000/"

while not wlan.isconnected():
    led17.on()
    utime.sleep(0.06)
    led17.off()
    utime.sleep(1)
    print("down")
print("up")
led17.on()

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    xValueUpper = xValueStored * 1.4
    xValueLower = xValueStored * 0.6
    yValueUpper = yValueStored * 1.4
    yValueLower = yValueStored * 0.6
    # print(str(xValue) +", " + str(yValue))
    # print(jButton.value())
    # utime.sleep(0.1)

    try:
        if jButton.value() == 0:
            r = urequests.post(url + "switch")
            r.close
            utime.sleep(0.1)
    except Exception as e:
        print(e)

    try:
        if yValue > yValueUpper:
            r = urequests.post(url + "right")
            r.close
            utime.sleep(0.1)
    except Exception as e:
        print(e)

    try:
        if yValue < yValueLower:
            r = urequests.post(url + "left")
            r.close
            utime.sleep(0.1)
    except Exception as e:
        print(e)

    try:
        if xValue > xValueUpper:
            r = urequests.post(url + "up")
            r.close
            utime.sleep(0.1)
    except Exception as e:
        print(e)

    try:
        if xValue < xValueLower:
            r = urequests.post(url + "down")
            r.close
            utime.sleep(0.1)
    except Exception as e:
        print(e)

    # try:
    #     print("GET")
    #     r = urequests.get(url)
    #     print(r.json())
    #     r.close
    #     utime.sleep(1)
    # except Exception as e:
    #     print(e)

# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)

# ssid = 'IIM_Private'
# password = 'Creatvive_Lab_2023'
# wlan.connect(ssid, password)
# url = "http://date.jsontest.com/"

# while wlan.isconnected() == False:
#     pass

# while True:
#     try:
#         print("GET")
#         r = urequests.get(url)
#         print(r.json()["date"])
#         r.close
#         utime.sleep(1)
#     except Exception as e:
#         print(e)

# adc = ADC(Pin(26, mode=Pin.IN))

# led17 = PWM(Pin(17, mode=Pin.OUT))
# led21 = PWM(Pin(21, mode=Pin.OUT))
# led27 = PWM(Pin(27, mode=Pin.OUT))
# led6 = PWM(Pin(6, mode=Pin.OUT))
# led10 = PWM(Pin(10, mode=Pin.OUT))
# pinButton = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
# led17.freq(1000)
# led21.freq(1000)
# led27.freq(1000)
# led6.freq(1000)
# led10.freq(1000)

# while True:
#     val = adc.read_u16()
#     print(val)

#     if pinButton.value() == 0 :
#         led17.duty_u16(val)
#         time.sleep(.1)
#         led21.duty_u16(val)
#         time.sleep(.1)
#         led27.duty_u16(val)
#         time.sleep(.1)
#         led6.duty_u16(val)
#         time.sleep(.1)
#         led10.duty_u16(val)

#         time.sleep(.5)
    
#         led17.duty_u16(0)
#         time.sleep(.1)
#         led21.duty_u16(0)
#         time.sleep(.1)
#         led27.duty_u16(0)
#         time.sleep(.1)
#         led6.duty_u16(0)
#         time.sleep(.1)
#         led10.duty_u16(0)
#     else:
#         led17.duty_u16(0)
#         led21.duty_u16(0)
#         led27.duty_u16(0)
#         led6.duty_u16(0)
#         led10.duty_u16(0)


# led17 = PWM(Pin(17, mode=Pin.OUT))
# led21 = PWM(Pin(21, mode=Pin.OUT))
# led27 = PWM(Pin(27, mode=Pin.OUT))
# led6 = PWM(Pin(6, mode=Pin.OUT))
# led10 = PWM(Pin(10, mode=Pin.OUT))
# pinButton = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
# led17.freq(1000)
# led21.freq(1000)
# led27.freq(1000)
# led6.freq(1000)
# led10.freq(1000)

# while True:
#     if pinButton.value() == 0 :
#         for i in range(0, 30000):
#             led17.duty_u16(i)
#         for i in range(0, 30000):
#             led21.duty_u16(i)
#         for i in range(0, 30000):
#             led27.duty_u16(i)
#         for i in range(0, 30000):
#             led6.duty_u16(i)
#         for i in range(0, 30000):
#             led10.duty_u16(i)
        
#         for i in range(0, 30000):
#             led17.duty_u16(30000 - i)
#         for i in range(0, 30000):
#             led21.duty_u16(30000 - i)
#         for i in range(0, 30000):
#             led27.duty_u16(30000 - i)
#         for i in range(0, 30000):
#             led6.duty_u16(30000 - i)
#         for i in range(0, 30000):
#             led10.duty_u16(30000 - i)
#     else:
#         led17.duty_u16(0)
#         led21.duty_u16(0)
#         led27.duty_u16(0)
#         led6.duty_u16(0)
#         led10.duty_u16(0)


# led17 = Pin(17, mode=Pin.OUT)
# led21 = Pin(21, mode=Pin.OUT)
# led27 = Pin(27, mode=Pin.OUT)
# led6 = Pin(6, mode=Pin.OUT)
# led10 = Pin(10, mode=Pin.OUT)
# pinButton = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)

# while True:
#     print(pinButton.value())
#     utime.sleep(.1)
#     if pinButton.value() == 0 :
#         led17.toggle()
#         utime.sleep(0.05)
#         led17.toggle()
#         led21.toggle()
#         utime.sleep(0.05)
#         led21.toggle()
#         led27.toggle()
#         utime.sleep(0.05)
#         led27.toggle()

#         led6.toggle()
#         utime.sleep(0.05)
#         led6.toggle()
#         led10.toggle()
#         utime.sleep(0.05)
#         led10.toggle()
#     else :
#         led17.off()
#         led21.off()
#         led27.off()
#         led6.off()
#         led10.off()

# led17 = Pin(17, mode=Pin.OUT)
# led21 = Pin(21, mode=Pin.OUT)
# led27 = Pin(27, mode=Pin.OUT)
# led6 = Pin(6, mode=Pin.OUT)
# led10 = Pin(10, mode=Pin.OUT)
# led14 = Pin(14, mode=Pin.OUT)

# while True:
#     led17.toggle()
#     utime.sleep(0.09)
#     led17.toggle()
#     led21.toggle()
#     utime.sleep(0.09)
#     led21.toggle()
#     led27.toggle()
#     utime.sleep(0.09)
#     led27.toggle()

#     led6.toggle()
#     utime.sleep(0.09)
#     led6.toggle()
#     led10.toggle()
#     utime.sleep(0.09)
#     led10.toggle()
#     led14.toggle()
#     utime.sleep(0.09)
#     led14.toggle()