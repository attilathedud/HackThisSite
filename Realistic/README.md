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

###Realistic 3
Notice this tip when inspecting the source of the hacker's page:
```
<!--Note to the webmasterThis website has been hacked, but not totally destroyed. The old website is still up. I simply copied the old index.html file to oldindex.html and remade this one. Sorry about the inconvenience.-->
```

Navigate to /oldindex.html to find the original page. We can assume there must be a vulnerbility in the submit functionality. Since the poem won't be displayed, that rules out xss attacks - instead, we can just try overwriting files. Simply copy oldindex.html and give the poem the title ../index.html. 

###Realistic 4
Like all good problem solvers, let's first enter some broken text into the email input box (just a test string like 'test'). Doing so should throw an error and reveal the table we want to target: email.

So we are going to have to do some sql injection somewhere, but targeting the email box doesn't work. What about the product page? We see their URL is in the form: /products.php?category=1. Could it be that they are running a query like:
```
Select * FROM $_GET['category']
```

It's worth a shot to try and exploit this possibility. We can tell from the layout that they return four items from their query (id, picture, description, price). With that, we will try to union on the emails table:
```
/products.php?category=1 UNION ALL SELECT *,*,*,* FROM email
```
