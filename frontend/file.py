from machine import Pin, PWM, ADC
import utime
import time
import network
import urequests
import ujson

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'Erebor'
password = 'ce mot de passe est difficile'
wlan.connect(ssid, password)
url = "http://192.168.174.176:3000/"

while not wlan.isconnected():
    utime.sleep(1)
    print("co down")
print("co up")

while True:
    try:
        print("GET")
        r = urequests.get(url)
        print(r.json())
        r.close
        utime.sleep(1)
    except Exception as e:
        print(e)

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