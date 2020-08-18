#!/usr/bin/python3
import requests
import re
r = requests.get("http://sound-captcha.sstf.site/",cookies={"PHPSESSID" : "836034d1480117f4c2863a91593a51cd"}).text
while(True):
    sound = requests.get("http://sound-captcha.sstf.site/cache/8d5dfced7d20b0cbe4d9b6ae0860cbd7.mp3").content
    soundsNumber = ['' for i in range(10)]
    for i in range(10):
        soundsNumber[i] = open("./challenge/mp3/%d.mp3" % i,"rb").read()

    captcha = ""
    while(len(captcha) != 6):
        for soundNum,soundVoice in enumerate(soundsNumber):
            if(soundVoice in sound):
                if(sound.index(soundVoice) == 0):
                    captcha += str(soundNum)
                    sound = sound.replace(soundVoice,b"",1)

    r = requests.post("http://sound-captcha.sstf.site/",data={"captcha_val" : captcha},cookies={"PHPSESSID" : "836034d1480117f4c2863a91593a51cd"}).text
    if("SCTF" in r):
        print(r)
        exit()
    elif("Correct Captcha!" not in r):
        print("Something bad happened")
        print(r)
        exit()
    else:
        print("Everything is fine")