Random String Generator
=======================

The `randomstring` tool allows the generation of random strings. The
length and characters can be choosen on command line:

    $ randomstring --help
    usage: randomstring [-h] [-c CHARACTERS] [-n NUMBER] [-l LENGTH]

    Generate random strings

    optional arguments:
      -h, --help            show this help message and exit
      -c CHARACTERS, --characters CHARACTERS
                            Characters to include in the generated strings
      -n NUMBER, --number NUMBER
                            Number of strings to generate (default: 0)
      -l LENGTH, --length LENGTH
                            Length of the string (default: "8-12")

Example usage:
--------------

    $ randomstring -l 10-20 -n 5
    MdHqkzQczc1pVp5mlP
    jgMfDZr8gEEmFGuO0ye1
    aV94DZZ42JNJNMi2X
    7bByLLKlRDcr
    ir5edXprCbYJywTV

Repeating characters can be used to change their likelyhood in the
output:

    $ randomstring -l 8 -c 0000001 -n 5
    01010101
    00100000
    00011011
    00010000
    00000000
