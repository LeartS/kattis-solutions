#!/usr/bin/env python3
import sys
import re

hex_re = re.compile('0x[0-9a-f]{1,8}', re.I)

for line in sys.stdin.readlines():
    for hex_number in hex_re.finditer(line):
        print(hex_number.group(), int(hex_number.group(), 16))