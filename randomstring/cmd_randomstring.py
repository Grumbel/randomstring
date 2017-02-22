# RandomString - Random string generation
# Copyright (C) 2017 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import io
import sys
import string
import re
import argparse
import itertools
import unicodedata

import randomstring.unicode
from randomstring.randomstring import make_random_string, make_random_unicode_string


class RangeArg:

    def __init__(self, text):
        m = re.match(r"([0-9]+)-([0-9]+)", text)
        if m is not None:
            self.start = int(m.group(1))
            self.stop = int(m.group(2)) + 1
        else:
            m = re.match(r"([0-9]+)", text)
            if m is not None:
                self.start = int(m.group(1))
                self.stop = self.start + 1
            else:
                raise Exception("Couldn't convert '{}' to range".format(text))

    def as_range(self):
        return range(self.start, self.stop)


def parse_args():
    parser = argparse.ArgumentParser(description='Generate random strings')
    parser.add_argument('-c', '--characters', type=str,
                        help="List of characters to include in the generated strings")
    parser.add_argument('-u', '--unicode', action='store_true', default=False,
                        help="Use unicode characters")
    parser.add_argument('-U', '--unicode-blocks', type=str,
                        help="Use Unicode characters from the given block")
    parser.add_argument('-n', '--number', type=int, default=1,
                        help="Number of strings to generate (default: 1)")
    parser.add_argument('-l', '--length', type=RangeArg, default=RangeArg("8-12"),
                        help="Length of the string (default: \"8-12\")")
    return parser.parse_args()


def good_char(c):
    cat = unicodedata.category(c)
    return cat not in ['Cc', 'Cf', 'Cn', 'Co', 'Cs']

def main():
    # Python 3.5.2 still doesn't have "surrogateescape" enabled by
    # default on stdout/stderr, so we have to do it manually. Test with:
    #   print(os.fsdecode(b"\xff"))
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,
                                  encoding='utf-8', errors="surrogateescape",
                                  line_buffering=True)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer,
                                  encoding='utf-8', errors="surrogateescape",
                                  line_buffering=True)

    args = parse_args()

    if args.number == 0:
        seq = itertools.repeat(None)
    else:
        seq = range(args.number)

    characters = string.ascii_letters + string.digits

    if args.characters:
        characters = args.characters

    if args.unicode_blocks:
        if args.unicode_blocks == "help":
            for k in sorted(randomstring.unicode.blocks.keys()):
                print(k)
            sys.exit(0)

        for block in args.unicode_blocks.split(","):
            characters += "".join([chr(c) for c in randomstring.unicode.blocks[block] if good_char(chr(c))])

    for _ in seq:
        if args.unicode:
            text = make_random_unicode_string(args.length.as_range())
        else:
            text = make_random_string(characters, args.length.as_range())

        print(text)


# EOF #
