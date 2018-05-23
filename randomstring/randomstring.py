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


import random
import unicodedata


def make_random_string(characters: str, length_range: range, rng: random.Random) -> str:
    result = ""

    length = rng.randint(length_range.start, length_range.stop - 1)
    for _ in range(length):
        result += rng.choice(characters)

    return result


def random_unicode_chr(rng: random.Random) -> str:
    # See:
    # http://www.fileformat.info/info/unicode/category/index.htm
    # http://stackoverflow.com/questions/1477294/generate-random-utf-8-string-in-python
    while True:
        c = chr(rng.randint(0, 0x10ffff))
        cat = unicodedata.category(c)

        if cat not in ['Cc', 'Cf', 'Cn', 'Co', 'Cs']:
            return c


def make_random_unicode_string(length_range: range, rng: random.Random) -> str:
    result = ""

    length = rng.randint(length_range.start, length_range.stop - 1)
    for _ in range(length):
        result += random_unicode_chr(rng)

    return result


# EOF #
