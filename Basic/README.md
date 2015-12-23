###Basic 1
Idiot test, as they say. Simply opening up the source and searching through it will reveal the password in a comment.

###Basic 2
Since there is no password file, there is no password, so we enter nothing and pass. We should also pick up on the lesson of always trying the null case for these, as it will give you clues.

###Basic 3:
If we look in the source, we see the following line:
```
<input type="hidden" name="file" value="password.php">
```
With that information, it makes sense to append password.php to the url and we are revealed the password.

###Basic 4:
So for this, we can assume that we have to edit the email address that the reminder is sent to. Look at the source and we see this line:
```
<input type="hidden" name="to" value="sam@hackthissite.org">
```
Just set the value to your email and you will be sent the password.

###Basic 5:
I'm not exactly sure how this is different from basic 4 - I'm guessing this challenge was probably made easier by the introduction of easy development tools.

###Basic 6:
A pretty basic encryption scheme is being used here. As a start, enter 'aaaaaa' into the search box and you will see it returns 'abcdef.' From this we can easily see that each position has its index adding to the char code of the entered screen. If our encrypted password is '08d:<66:', we know that the first three characters will be '07b'. From there we can look up the ascii code chart and work on the other characters.

###Basic 7:
Since the input to the cal command is not sanitized, we can inject our own commands into it by using the ; to end the current command and run another. So if we enter '1999;ls' we are giving the calender with the directory listing appended. The password file will appear in that list, so simply append it to the url and get the password.

###Basic 8:
The key to this challenge is finding out that the "name" you enter is partially evaluated; enter in:
```
<!--
```

And the result will be:
```
&lt;!--
```

Combined with the knowledge that SSI is needed for the page, we can pull up the doc for SSI's (https://httpd.apache.org/docs/2.4/howto/ssi.html) and try the example there:
```
<!--#echo var="DATE_LOCAL" -->
```

You'll get the helpful message that you are on the right track. Since we are looking for a hidden file, we can leverage the php exec command with ls:
```
<!--#exec cmd="ls ../" -->
```

Opening the saved file, it will reveal our hidden file we are looking for:
```
au12ha39vc.php
```

###Basic 9:
A very similar idea to last time; only difference is that we need to go up an additional level since we are executing from challenge 8's directory:
```
<!--#exec cmd="ls ../../9/" -->
```

This will reveal our hidden file in /9/:
```
p91e283zc3.php
```

###Basic 10:
Apparently this challenge is using Javascript to validate us, but there's nothing easy in the source we can identify. Fire up Live HTTP headers (or some network logger), and look for your request. You will see the following interesting line:
```
Cookie: level10_authorized=no; PHPSESSID=sfvjacpmd94gr0btvugdcmbr41; ads_bm_last_load_status=BLOCKING
```

That's a suspicious looking cooking - modifying it to yes will give us the access we need:
```
document.cookie = "level10_authorized=yes"
```

###Basic 11:
So from the page, we get a hint that something is hidden; run a directory scanner and you should get two items of interest: index.php (where we will enter our password) and /e/. Going to /e/ reveals a list of subdirectories down to /e/l/t/o/n/.

Since this is an apache server, we'll see if we can access .htaccess. We can, and it will reveal the DaAnswer subdirectory. Navigate there and you will be given a simple riddle to get the answer.
