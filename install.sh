#!/bin/bash

source ./inc/utils.sh

function install(){
    checkSudoPermissions
    echo "Installation is started"

    apt-get update
    apt-get dist-upgrade
    apt-get -y install \
               omxplayer \
               bc \
               rsync \
               cron \
               build-essential \
               python \
               python-pip \
               python-gpiozero

    pythonModulesInstallation
    createDirLogs
    cronjobInstallation
    copyDir

    echo "The installation was completed"
}

function pythonModulesInstallation(){
    pip install pydub \
                mutagen \
                RPi.GPIO
}

function cronjobInstallation(){
    #The if checks, if the cronjob is installed already in the system
    if grep "/usr/script/rasp-navidad/" /var/spool/cron/crontabs/root;
    then
        echo "The crontab is already installed"
    else
        echo "The crontab is NOT installed"
       
        crontab -l > rasp-navidad-cron

        echo '*/30 19-23 * * * /usr/bin/python /usr/script/rasp-navidad/main.py >> /var/log/rasp-navidad-logs/rasp-navidad_`date +\%Y-\%m-\%d`.log 2>&1' >> rasp-navidad-cron
        echo "30 20 * * * find /var/log/rasp-navidad-logs/ -type f -mtime +7 -name '*.log' -exec rm {} \;" >> rasp-navidad-cron
        
        crontab rasp-navidad-cron
        rm rasp-navidad-cron
        
        echo "The crontab is NOW installed"

        /etc/init.d/cron start
        echo "The cron is started"
    fi
}

function createDirLogs(){
    if [ -d "/var/log/rasp-navidad-logs" ];
    then
        echo "Directory already exists"
    else
        mkdir -p "/var/log/rasp-navidad-logs"
    fi
}

function copyDir(){
    if [[ -d "/usr/script/rasp-navidad" ]];
    then
        echo "The rasp-navidad is already installed."
    else
        mkdir -p /usr/script/rasp-navidad
        rsync -aHx main/* /usr/script/rasp-navidad
        chmod 750 -R /usr/script/rasp-navidad
        echo "The rasp-navidad directory was copied."
    fi
}

install