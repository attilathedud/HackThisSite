###Stego 1
Open up the bmp in a hex editor and look for two null characters (i.e., 00 00). After the header, you should exactly two pairs, with this series encoded between them:
```
16 16 17 17 17 16 16 16 16 17 17 16 16 17 17 16 16 17 17 16 17 17 17 16 17 17 16 17 16 16 16 16 17 17 16 16 16 16 17 16 17 17 17 16 16 17 17 16 16 17 17 16 17 17 16
```

Looks like a binary number scheme, converting 16 -> 0 and 17 -> 1 gives us:
```
00111000
01100110
01101110
11010000
11000010
11100110
0110110
```

You will notice we are off a diget. Throwing a 0 on the beginning and the end don't give us correct answers either, so we can't just easily pad it out. I'm not sure if there is a better way, but I simply wrote a script to iterate through and pad a 0 at every possible position until I arrived at a series that translated into reasonable text.

