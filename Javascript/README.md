###Javascript 1
If we check the source of the page, there is an easy block of javascript that stands out:
```
function check(x)
{
    if (x == "cookies")
    {
        alert("win!");
        window.location += "?lvl_password="+x;
    } else {
        alert("Fail D:");
    }
}
```

Without even looking at how it is called, we can safely guess entering cookies will cause us to pass.

###Javascript 2
This challenge has a very simple bit of redirection going on. If you are feeling slow, all you have to do is disable javascript before you load the page and you will be good to go. If you are on a slow connection, you can simply kill the page load by spamming escape and then browse the code to see how this challenge works:
```
<script language="javascript">
    window.location="http://www.hackthissite.org/missions/javascript/2/fail.php";
</script>
<a href="/missions/javascript/2/index.php?challengePass=X(KB5V">Click here to win.</a>
```

From there, it's as easy as navigating to the generated link to completing the challenge.

###Javascript 3
For this challenge, we are given the following function that will check our password:
```
var foo = 5 + 6 * 7 
var bar = foo % 8
var moo = bar * 2
var rar = moo / 3
function check(x)
{
    if (x.length == moo)
    {
        alert("win!");
        window.location += "?lvl_password="+x;
    } else {
        alert("fail D:");
    }
}
```

If you are feeling particularly motivated, you can attempt to dissect the logic, but it's far easier to just throw this code into Chrome's developer console (or Firefox's Scratchpad) and then querying the value of moo, which happens to be 14. From there all we need to do is generate a password that is 14 characters long.

###Javascript 4
So for this challenge, we are given the following function to check our password:
```
RawrRawr = "moo";
function check(x)
{
    "+RawrRawr+" == "hack_this_site"
    if (x == ""+RawrRawr+"")
    {
        alert("Rawr! win!");
        window.location = "../../../missions/javascript/4/?lvl_password="+x;
    } else {
        alert("Rawr, nope, try again!");
    }
}
```

The key to this challenge is just to have a keen eye; the line you should focus on is:
`if (x == ""+RawrRawr+"")`

While it is tempting to confuse this with the line above, let's separate this line out with some spaces:
`if (x == "" + RawrRawr + "")`

This is nothing but a simple string concatination to RawrRawr which was already defined as "moo". Since we are adding nothing, we know the answer is just moo.

###Javascript 5
Our code block for this challenge:
```
moo = unescape('%69%6C%6F%76%65%6D%6F%6F');
function check (x) {
    if (x == moo)
    {
        alert("Ahh.. so that's what she means");
        window.location = "../../../missions/javascript/5/?lvl_password="+x;
    }
    else {
        alert("Nope... try again!");
    }
}
```

Entering the first line into a developer console, we can then easily query for what it is: ilovemoo.

###Javascript 6
The only difficulty from this challenge comes from the fact that we have multiple check pass functions defined. Checking the code for the Check Password will define which one we will use:
`<button onclick="javascript:checkpass(document.getElementById('pass').value)">Check Password</button>`

But weirdly enough, that function name (checkpass) doesn't appear in the code; however, if we look above the code-block, we see another suspicious include:
`<script type="text/javascript" src="/missions/javascript/6/checkpass"></script>`

Following this, we find our real checkpass code:
```
dairycow="moo";
moo = "pwns";
rawr = "moo";

function checkpass(pass)
{
if(pass == rawr+" "+moo)
{	
alert("How did you do that??? Good job!");
window.location = "../../../missions/javascript/6/?lvl_password="+pass;
} else {
alert("Nope, try again");
}
}
```

Besides some slightly obfuscated code, it should be pretty to see that the password will end up being "moo pwns".

###Javascript 7
This is a particularly ugly piece of code:
```
var _0x4e9d=["\x66\x72\x6F\x6D\x43\x68\x61\x72\x43\x6F\x64\x65","\x77\x72\x69\x74\x65"];document[_0x4e9d[0x1]](String[_0x4e9d[0x0]](0x3c,0x62,0x75,0x74,0x74,0x6f,0x6e,0x20,0x6f,0x6e,0x63,0x6c,0x69,0x63,0x6b,0x3d,0x27,0x6a,0x61,0x76,0x61,0x73,0x63,0x72,0x69,0x70,0x74,0x3a,0x69,0x66,0x20,0x28,0x64,0x6f,0x63,0x75,0x6d,0x65,0x6e,0x74,0x2e,0x67,0x65,0x74,0x45,0x6c,0x65,0x6d,0x65,0x6e,0x74,0x42,0x79,0x49,0x64,0x28,0x22,0x70,0x61,0x73,0x73,0x22,0x29,0x2e,0x76,0x61,0x6c,0x75,0x65,0x3d,0x3d,0x22,0x6a,0x30,0x30,0x77,0x31,0x6e,0x22,0x29,0x7b,0x61,0x6c,0x65,0x72,0x74,0x28,0x22,0x59,0x6f,0x75,0x20,0x57,0x49,0x4e,0x21,0x22,0x29,0x3b,0x77,0x69,0x6e,0x64,0x6f,0x77,0x2e,0x6c,0x6f,0x63,0x61,0x74,0x69,0x6f,0x6e,0x20,0x2b,0x3d,0x20,0x22,0x3f,0x6c,0x76,0x6c,0x5f,0x70,0x61,0x73,0x73,0x77,0x6f,0x72,0x64,0x3d,0x22,0x2b,0x64,0x6f,0x63,0x75,0x6d,0x65,0x6e,0x74,0x2e,0x67,0x65,0x74,0x45,0x6c,0x65,0x6d,0x65,0x6e,0x74,0x42,0x79,0x49,0x64,0x28,0x22,0x70,0x61,0x73,0x73,0x22,0x29,0x2e,0x76,0x61,0x6c,0x75,0x65,0x7d,0x65,0x6c,0x73,0x65,0x20,0x7b,0x61,0x6c,0x65,0x72,0x74,0x28,0x22,0x57,0x52,0x4f,0x4e,0x47,0x21,0x20,0x54,0x72,0x79,0x20,0x61,0x67,0x61,0x69,0x6e,0x21,0x22,0x29,0x7d,0x27,0x3e,0x43,0x68,0x65,0x63,0x6b,0x20,0x50,0x61,0x73,0x73,0x77,0x6f,0x72,0x64,0x3c,0x2f,0x62,0x75,0x74,0x74,0x6f,0x6e,0x3e));
```

So what do we do with this? Well, we can get a basic idea of what it is doing by looking at the first readable word: document. For this code to be executed, we know that the code needs to be injected into the document somewhere, so the document[] call must be writing the code in somehow. Throwing the code into JSNice will support our guess:
```
/** @type {Array} */
var _0x4e9d = ["fromCharCode", "write"];
document[_0x4e9d[1]](String[_0x4e9d[0]](60, 98, 117, 116, 116, 111, 110, 32, 111, 110, 99, 108, 105, 99, 107, 61, 39, 106, 97, 118, 97, 115, 99, 114, 105, 112, 116, 58, 105, 102, 32, 40, 100, 111, 99, 117, 109, 101, 110, 116, 46, 103, 101, 116, 69, 108, 101, 109, 101, 110, 116, 66, 121, 73, 100, 40, 34, 112, 97, 115, 115, 34, 41, 46, 118, 97, 108, 117, 101, 61, 61, 34, 106, 48, 48, 119, 49, 110, 34, 41, 123, 97, 108, 101, 114, 116, 40, 34, 89, 111, 117, 32, 87, 73, 78, 33, 34, 41, 59, 119, 105, 110, 
100, 111, 119, 46, 108, 111, 99, 97, 116, 105, 111, 110, 32, 43, 61, 32, 34, 63, 108, 118, 108, 95, 112, 97, 115, 115, 119, 111, 114, 100, 61, 34, 43, 100, 111, 99, 117, 109, 101, 110, 116, 46, 103, 101, 116, 69, 108, 101, 109, 101, 110, 116, 66, 121, 73, 100, 40, 34, 112, 97, 115, 115, 34, 41, 46, 118, 97, 108, 117, 101, 125, 101, 108, 115, 101, 32, 123, 97, 108, 101, 114, 116, 40, 34, 87, 82, 79, 78, 71, 33, 32, 84, 114, 121, 32, 97, 103, 97, 105, 110, 33, 34, 41, 125, 39, 62, 67, 104, 101, 99, 
107, 32, 80, 97, 115, 115, 119, 111, 114, 100, 60, 47, 98, 117, 116, 116, 111, 110, 62));
```

From this we can gather that we are writing these series of charcodes into the page - all we need to do now is translate the char codes into something we can read. I used the following utility to, but any char code translator will work: http://jdstiles.com/java/cct.html. The code spit out:
```
<button onclick='javascript:if (document.getElementById("pass").value=="j00w1n"){alert("You WIN!");window.location += "?lvl_password="+document.getElementById("pass").value}else {alert("WRONG! Try again!")}'>Check Password</button>
```

From there it is pretty easy to see our password.
