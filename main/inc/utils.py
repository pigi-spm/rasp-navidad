import os
import logging
import subprocess
import random
import config
import sys

class Utils:

    def setMusicName(self, filename):
            for root, directory, files in os.walk(config.confRasp["path"] + "/audio/"):
                for file in files:
                    if file.endswith('.mp3'):
                        if (filename+".mp3") == str(file):
                            logging.info("The audio-file: " + str(file) + " was found!")

                            return (root+str(file))
                        if ((str(file)[0:1]) == filename):
                            logging.info("The audio-file: " + str(file) + " was found!")

                            return (root+str(file))

            logging.warning("The audio-file: " + filename + " was not found! Please check if the file is saved into the audio folder or if the name is correct")

            sys.exit(0)
    
    def setRandomRange(self):
            count = 0
            for root, directory, files in os.walk(config.confRasp["path"] + "/audio/"):
                for file in files:
                    if file.endswith('.mp3'):
                        if((str(file)[0:1]).isdigit()):
                            count += 1
            
            return random.randrange(1, count, 1)

    def playMusic(self, mp3File):
            play = subprocess.Popen(['omxplayer', '-o', 'local', '--vol', str(config.mp3['volume']) , mp3File], stdout=subprocess.PIPE)  #it creates the name of the mp3 file in the selected folder

    def setLoggingConfig(self):
        #sets the basic configs for the logging system
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')