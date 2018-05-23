Random String Generator
=======================

The `randomstring` tool allows the generation of random strings. The
length and character set can be choosen on command line:

    $ randomstring --help
    usage: randomstring [-h] [-n COUNT] [-l LENGTH]
                        [-c CHARACTERS | -u | -U UNICODE_BLOCKS | -A]

    Generate random strings

    optional arguments:
      -h, --help            show this help message and exit
      -n COUNT, --count COUNT
                            Number of strings to generate (default: 1)
      -l LENGTH, --length LENGTH
                            Length of the string (default: "8-12")

    Character Set Options:
      -c CHARACTERS, --characters CHARACTERS
                            List of characters to include in the generated strings
      -u, --unicode         Use unicode characters
      -U UNICODE_BLOCKS, --unicode-blocks UNICODE_BLOCKS
                            Use Unicode characters from the given block
      -A, --ascii           Use printable non-whitespace ASCII characters


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
