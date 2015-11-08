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