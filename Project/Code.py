import time
import urllib
import sys
import os
import Adafruit_DHT
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(18,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(24,GPIO.IN)
def startcode():
    while True:
        #ROOM UNLOCK
        response=urllib.urlopen("Link  to things speak")
        command=response.read()
        command=command.decode()
        if (command=='unlock_my_room'):
            #print("Unlocked")
            GPIO.output(3,True)#lock
            time.sleep(10)
            GPIO.output(3,False)
            continue
        #TAKE SHOT
        if (command=='take_a_shot'):
            #print("Target down")
            GPIO.output(5,True)#coil
            time.sleep(10)
            GPIO.output(5,False)
            continue
        #SECURITY ON
        if (command=='security_on'):
            #print("Security is on")
            GPIO.output(7,True)#laser
            GPIO.output(3,False)#lock
            continue
        #MOTOR ON
        if (command=="motor_on"):
            GPIO.output(11,True)
            #print("Motor is ON")
            time.sleep(10)
            GPIO.output(11,False)
            continue
        #LIGHT ON
        if (command=="light_on"):
            GPIO.output(13,True)
            #print("Lights ON")
            continue
        #LIGHT OFF
        if (command=="light_off"):
            GPIO.output(13,False)
            #print("Lights OFF")
            continue
        #BUZZER ON
        if (command=="buzzer_on"):
            for i in range(0,10):
                GPIO.output(22,True)
                time.sleep(2)
                GPIO.output(22,False)
                time.sleep(2)
                #print("Buzzer ON")
            continue
    #DOOR UNLOCK
    while (GPIO.input(15)==0):
        GPIO.output(3,True)
        time.sleep(10)
        GPIO.output(3,False)
    #LASER CIRCUIT
    while (GPIO.input(16)==True):
        data=urllib.urlopen("Link to app")
        time.sleep(20)
    #HUMIDITY
    while (GPIO.input(18)==0):
            Humidity_alert=urllib.urlopen("Link to app")
            GPIO.output(11,True)
            time.sleep(3)
            GPIO.output(11,False)
    Humidity_value=input("value=")
    Humidity_value=~Humidity_value
    moisture=((Humidity_value+1024.0)/1023.0)*100
    Humidity_upload=urllib.urlopen("Link to Things speak",+str(moisture))
    #TEMPERATURE
    humidity,temperature=Adafruit_DHT.read_retry(24,22)
    hvalue=urllib.urlopen("Link to Things Speak",+str(humidity))
    tvalue=urllib.urlopen("Link to things Speak",+str(temperature))help()
    
    if (temperature>=30):
        urllib.urlopen("Link to app")
    elif(temperature>20 and temperature<30):
        urllib.urlopen("Link to app")    
startcode()
