###ExtBasic 1
We can see that the buffer only has a length of 200 so all we need to do is pass a string longer than 200 characters for strcpy to overflow and crash.

###ExtBasic 2
Since we are in https://www.hackthissite.org/missions/extbasic/2/ and need the source of /index.php, we simply need to go two levels up:
```
../../index
```

###ExtBasic 3
Let's comment out our given language:
```
;language is type insensitive
;variables created at 0
BEGIN notr.eal              ;begin the file
CREATE int AS 2             ;int CREATE = 2
DESTROY int AS 0            ;int DESTROY = 0
ANS var AS Create + TO      ;var = CREATE + TO (0)
out TO                      ;TO = 2
```

Breaking it down logically with a bit of guesswork makes the solution clear.

###ExtBasic 4
Let's comment out our given language again:
```
User types 6,7
BEGIN F.ake             ;begin the file
var int as in   6       ;var = 6
int var as in   7       ;int = 7
out var int             ;67
```

