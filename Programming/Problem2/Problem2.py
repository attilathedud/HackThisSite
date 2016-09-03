import png

# Taken from  https://gist.github.com/ebuckley/1842461
morse_alphabet ={
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "1" : ".----",
	"2" : "..---",
	"3" : "...--",
	"4" : "....-",
	"5" : ".....",
	"6" : "-....",
	"7" : "--...",
	"8" : "---..",
	"9" : "----.",
	"0" : "-----",
	"." : ".-.-.-",
	"," : "--..--",
	":" : "---...",
	"?" : "..--..",
	"'" : ".----.",
	"-" : "-....-",
	"/" : "-..-.",
	"@" : ".--.-.",
	"=" : "-...-"
}

inverse_morse_alphabet 		= dict((v,k) for (k,v) in morse_alphabet.items())

# Read in our png file
reader 						= png.Reader( filename = 'download.png' )
w, h, pixels, metadata 		= reader.read_flat( )

# Iterate over the image, keeping a counter so we can calculate distance
last_white_pixel_pos 		= 0
current_pos			 		= 0
morse_string		 		= ""

for i in pixels:
	if i == 1:
		morse_string += chr( current_pos - last_white_pixel_pos )
		last_white_pixel_pos = current_pos

	current_pos += 1

# Divide up the morse code and translate each letter
morse_string_decoded 		= ""
morse_string_split 			= morse_string.split()
for letter in morse_string_split:
	morse_string_decoded += inverse_morse_alphabet[ letter ]

print morse_string_decoded
