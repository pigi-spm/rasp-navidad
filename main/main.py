#!/usr/bin/env python

"""
==============================================================================
Author: Pierluigi Minardi
Credits: Luciano Minardi
License: CC BY 4.0
Version: 0.0.1
Creation date: 2020/11/02
LastChange: 2020/12/12
Username: Pigi
Description: rasp-navidad project
==============================================================================
"""

import os
import config
import logging
from inc.utils import Utils
from inc.lightsEffect import LightsEffect
from inc.relay import Relay
from inc.lightsStrip import LightsStrip

import RPi.GPIO as GPIO
from gpiozero import LED

#sets GPIO in BCM mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

global ledBlue
global ledRed
global ledGreen
global relayBlue
global relayRed
global relayGreen

class Main:
    
    def __init__(self):
        self.lightsEffect = LightsEffect()
        lightsStrip = LightsStrip()
        self.relay = Relay()
        self.utils = Utils()

        self.utils.setLoggingConfig()

        logging.info('Welcome from rasp-navidad')
        logging.info('sets the GPIO pins in the variable')

        self.ledBlue = config.pid['blue']
        self.ledRed = config.pid['red']
        self.ledGreen = config.pid['green']
        self.relayBlue = config.relay['blue']
        self.relayRed = config.relay['red']
        self.relayGreen = config.relay['green']

        lightsStrip.setLightsStrip([self.ledBlue, self.ledRed, self.ledGreen])
        self.relay.setRelay([self.relayBlue, self.relayRed, self.relayGreen])
        logging.info('GPIO was setted with succesfull')

    def main(self):
        
        self.effectSelector(self.ledBlue, self.ledRed, self.ledGreen, self.relayBlue, self.relayRed, self.relayGreen)

        logging.info('Goodbye from rasp-navidad')

    def effectSelector(self, ledBlue, ledRed, ledGreen, relayBlue, relayRed, relayGreen):
        self.relay.onRelay([self.relayBlue, self.relayRed, self.relayGreen])
        self.lightsEffect.lightsEffectWithGPIO("1_Deck the Halls", [self.ledRed, self.ledBlue, self.ledGreen])

        self.relay.offRelay([self.relayBlue, self.relayRed, self.relayGreen])
        self.lightsEffect.lightsEffectWithoutGPIO(str(self.utils.setRandomRange()))

        self.relay.offRelay([self.relayBlue, self.relayRed, self.relayGreen])
        self.lightsEffect.lightsEffectWithoutGPIO(str(5))

        self.relay.offRelay([self.relayBlue, self.relayRed, self.relayGreen])
        self.lightsEffect.lightsEffectWithoutGPIO("thunder_rain_05")

        self.relay.onRelay([self.relayBlue, self.relayRed, self.relayGreen])
        self.lightsEffect.lightsEffectWithGPIO("3_O Jingle Bells", [self.ledBlue])

        GPIO.cleanup() # GPIO cleanup -> The pins are turned off
        logging.info("GPIO is off")

if __name__ == "__main__":
   s = Main()
   s.main()
