import os
import logging

import RPi.GPIO as GPIO
from gpiozero import LED

class Relay:

    def setRelay(self, relayPort):
        for i in range(len(relayPort)):
            GPIO.setup(relayPort[i],GPIO.OUT) # The GPIO pid is setted with the OUTPUT mode
            logging.info("The GPIO setup for the relay with the port "+ str(relayPort[i]) +" is completed")


    def onRelay(self, relayPort):
        for i in range(len(relayPort)):
            GPIO.output(relayPort[i], GPIO.LOW) # The relay is with the status on
            logging.info("The relay "+ str(relayPort[i]) +" is on")


    def offRelay(self, relayPort):
        for i in range(len(relayPort)):
            GPIO.output(relayPort[i], GPIO.HIGH) # The relay is with the status off
            logging.info("The relay "+ str(relayPort[i]) +" is off")
