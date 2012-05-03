#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Display the local time to the nearest half-hour using the Unicode
analog clock-face code-points.

You can see the glyphs here: http://www.unicode.org/charts/PDF/U1F300.pdf

Example:

python -c "import clockface; print clockface.glyph()"

License: GPLv3+
"""


import os, sys, time

def _wide_supported():
    try:
        unichr(0x10fffe)
    except ValueError, ignored:
        return False
    return True

def _print_error():
    sys.stderr.write("Your Python build does not support 'wide'"
                     " Unicode characters.  This program displays"
                     " wide unicode characters, so it won't work."
                     + os.linesep)

def glyph(localtime=None):
    base_clock = 0x1F550 # 🕐
    
    clocks  = [unichr(base_clock + 11)]
    clocks += [unichr(i) for i in range(base_clock, base_clock + 11)]
    clocks += [unichr(base_clock + 11 + 12)]
    clocks += [unichr(i) for i in range(base_clock + 12, base_clock + 23)]
    
    if localtime is None:
        localtime = time.localtime()
    clockface_index = localtime.tm_hour % 12
    if (localtime.tm_min >= 30):
        clockface_index += 12

    return clocks[clockface_index]



if __name__ == "__main__":
    if not _wide_supported():
        _print_error()
        sys.exit(1)
    sys.stdout.write(glyph() + os.linesep)

