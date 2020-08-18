# Sound Captcha - 17 solves

## Story

I made sound captcha system at the first time in my life!

After finished deploy, I realize that I did some mistake.
Time limit is soooooo tight that nobody can pass it!

Do you agree with me?

## Soultion

In this challenge, We have  to solve 10 sound captchas under 20 seconds.

After reading source code of challenge, we can find mp3 files that used in captcha. So if we have 2 in captcha, Then `2.mp3` will be added to the sound.

I wrote `solve.py` to solve this challenge. First we add all sounds in array. Then we iterate through array and find the first sound based on array sounds and then remove the first letter's sound. Then we continue until we find all 6 letter and then POST the captcha to challenge. Then send the captcha 10 times and we have the flag.

### Flag

SCTF{T4ke_car3_0f_s0und_c4p4ch4_1n_gnub04r6}