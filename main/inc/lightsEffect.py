import time
import logging

from mutagen.mp3 import MP3
from inc.utils import Utils

import RPi.GPIO as GPIO
from gpiozero import LED

class LightsEffect:

    def __init__(self):
        self.utils = Utils()

    # The method sets the lighting effect. 
    # It allows to increase and decrease the light intensity of the led strips.
    def lightsEffectWithGPIO(self, filename, leds):
            l = []
            mp3File = self.utils.setMusicName(filename)
            mp3Audio = MP3(mp3File)

            # Contains all the metadata about the mp3 file
            audioInfo = mp3Audio.info
            totalDurationInSecs = time.time()+float(audioInfo.length) ## time now + get the total duration from the mp3 audio
            halfTotalDurationInSecs = time.time()+(float(audioInfo.length)/2) ## time now + get the half duration from the mp3 audio
            
            self.utils.playMusic(mp3File)  ## start with a subprocess the music
            logging.info('The mp3 file '+mp3File+ ' was started')
            
            for i in range(len(leds)):
                l.append(GPIO.PWM(leds[i], 1000)) # set Frequece to 1KHz
                l[i].start(0) # Start PWM output, Duty Cycle = 0
            while True:
                # It is true if the time is less than halfTotalDurationInSecs
                if time.time() < halfTotalDurationInSecs:
                    for dc in range(0, 101, 1): # Increase duty cycle: 0~100
                            logging.info("go up")
                            for i in range(len(leds)):
                                l[i].ChangeDutyCycle(dc) # Change duty cycle
                            time.sleep(float(audioInfo.length/2)/100) # The script waits for the next duty cycle
                    time.sleep(1)  
                # It is true if the time is included between halfTotalDurationInSecs and totalDurationInSecs
                elif time.time() >= halfTotalDurationInSecs and time.time() < totalDurationInSecs:
                    for dc in range(100, -1, -1): # Decrease duty cycle: 100~0
                            logging.info("go down")
                            for i in range(len(leds)):
                                l[i].ChangeDutyCycle(dc) # Change duty cycle                       
                            time.sleep(float(audioInfo.length/2)/100) # The script waits for the next duty cycle
                    time.sleep(1)
                else:
                    break

    # The method sets the lighting effect. 
    # It simply lets you start the song and wait for it to end. The relays are off
    def lightsEffectWithoutGPIO(self, filename):
            l = []
            mp3File = self.utils.setMusicName(filename)
            mp3Audio = MP3(mp3File)

            # Contains all the metadata about the mp3 file
            audioInfo = mp3Audio.info
            audioLength = float(audioInfo.length) 

            self.utils.playMusic(mp3File)  ## start with a subprocess the music
            logging.info('The mp3 file '+mp3File+ ' was started')

            while True:
                logging.info("waiting for the audio to finish...")
                time.sleep(audioLength)
                
                break
