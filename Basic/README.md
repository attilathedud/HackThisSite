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