import os
import logging

import RPi.GPIO as GPIO
from gpiozero import LED

class LightsStrip:

    def setLightsStrip(self, pidPort):
        for i in range(len(pidPort)):
            GPIO.setup(pidPort[i],GPIO.OUT) # The GPIO pid is setted with the OUTPUT mode
            logging.info("The GPIO setup for the led strips with the port " + str(pidPort[i]) + " is completed")
