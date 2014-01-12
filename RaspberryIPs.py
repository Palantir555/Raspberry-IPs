#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import * 
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()
cmdInt = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
cmdExt = "curl ifconfig.me/ip"

lcd.begin(16,1)
lcd.clear()

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

E_ip = run_cmd(cmdExt)

I_ip = run_cmd(cmdInt)
lcd.clear()
lcd.message('I %s' % (I_ip))
lcd.message('E %s' % (E_ip))
sleep(2)
