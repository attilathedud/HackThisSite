###Application 1

Enter a random serial and the program will throw: "Sorry, you entered an incorrect serial number." Simply open up the memory dump of the program in Olly and do a search for this string and our serial will be living right above:
```
00742A8F                                            37 36                76
00742A9F  39 32 2D 33 33 34 39 2D 31 39 31 34 2D 34 35 36  92-3349-1914-456
00742AAF  37 00 00 00 00 01 00 00 00 C8 2A 74 00 41 00 00  7.......È*t.A..
00742ABF  00 3F 00 00 00 00 01 00 08 3F 53 6F 72 72 79 2C  .?.....?Sorry,
00742ACF  20 79 6F 75 20 65 6E 74 65 72 65 64 20 61 6E 20   you entered an
00742ADF  69 6E 63 6F 72 72 65 63 74 20 73 65 72 69 61 6C  incorrect serial
00742AEF  20 6E 75 6D 62 65 72 2E 20 50 6C 65 61 73 65 20   number. Please
00742AFF  72 65 2D 65 6E 74 65 72 2E 00 00 00 00 02        re-enter.....
```

###Application 2

The note demanding an internet connection gives us some clues; fire up Wireshark (or any packet sniffer), and send a request. You will see the following lovely GET request:
```
32    10.240613    10.7.242.165    198.148.81.136    HTTP    121    GET /application/app2/keys123.txt HTTP/1.1 
```

Opening up that page gives us plenty of valid keys.

###Application 3 
According to threads on HTS, this challenge is broken and requires a fair bit of patching to become workable again. The basic breakdown is that we are sending a GET request to /application/app3/auth.php?key=[key] which is supposed to respond with a 200 and a true or false value. Realisitically all we need to do is point to a local page that returns true all the time, but the function for sending the request is appending extra null characters to the key parameter. Will return to this when time permits.

###Application 4
Scanning the application with PEiD reveals it is a VB app, which means we can use a VB decompiler to make our life significantly easier. From the events, we see that the mouse_move function for button 1 lives at 402810; opening up Olly, we can navigate to this and see where it is called from:
```
00402810   > 55             PUSH EBP
...
0040249E   . E9 6D030000    JMP app4win.00402810
```

We can also see from the decompiler that 402ad0 represents the mouse_click function - we can simply change our mouse_move call to call this for us and our challenge is complete:
```
0040249E     E9 2D060000    JMP app4win.00402AD0
```