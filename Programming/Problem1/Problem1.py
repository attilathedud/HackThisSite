import sys

with open('wordlist.txt') as wordlist:
    content = wordlist.read().splitlines()
    sorted_content = list()

    # For each element in our wordlist, sort the letters alphabetically
    # and append them in the same order to our new list
    for s in content:
        sorted_content.append(''.join(sorted(s)))

    for arg in sys.argv[1:]:
        print(content[sorted_content.index(''.join(sorted(arg)))] + ",")
