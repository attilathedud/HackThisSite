### Problem 1 (Word Unscrambler)
This is a relatively easy challenge due to Python's ability to easily read and parse files. We simply read in our wordlist and then iterate through sorting each word and assigning it to a new list. Since we know the append operation is synchronise, we can safely assume the index of both lists are identical. From there, we simply sort our arguments and find them in the sorted list and return the word from the unsorted list by index.

### Problem 2 (Analyze the picture and find the ascii code)
Using pypng, we can grab an array of the image's pixels and simply iterate over them, calculating distance as we go. From there, we split the morse code into an array and use a dictionary to map each series to a character.

### Problem 12 (String manipulation)
The algorithm is basically written out in the introduction text. The most complex part of this challenge is writing the regex to grab digits and directly manipulating the DOM to deal with the time-limit. Hence why the solution is a script intended to run directly against the page.
