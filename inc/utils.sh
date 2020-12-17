#!/bin/bash

#The function checks if you use the admin permissions
function checkSudoPermissions(){
    if [ `whoami` != root ]; then
        echo "Please do not run this script as root or using sudo"
        exit 1
    fi
}