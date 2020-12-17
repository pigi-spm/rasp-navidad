#It sets the volume for your music.
mp3 = dict(
    #The range to set the volume is as follows:
    ### volume = -1 --> 100%
    ### volume = -4500 --> 0%
    volume = -1,
)

#If you have not changed the location of the rasp-navidad folder, please do not change this path
confRasp = dict(
    path = "/usr/script/rasp-navidad"
)

## Please search in google the GPIO.BCM for raspberry
#Here is an example from google images: https://www.google.com/search?q=pid+gpio+bcm&rlz=1C1CHBF_itDE922DE922&hl=de&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjNvffxmpHtAhWlBGMBHVR9Bp4Q_AUoAXoECA8QAw&biw=1536&bih=722#imgrc=W_7whm8PX5Ka5M
#See the README.md file to know how to configure it
#pid
pid = dict(
    blue=<pid number>,
    red=<pid number>,
    green=<pid number>,
)

#See the README.md file to know how to configure it
#relay
relay = dict(
    blue=<pid number>,
    red=<pid number>,
    green=<pid number>,
)