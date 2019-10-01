"""
    Library Max7219 7 segment 8 digits
    Micropython for ESP32 & ESP8266

	© Copyright 2019 Nuovo, TD.
	Author Chatdanai Phakaket
	email zchatdanai@gmail.com or nuovo.td@gmail.com

"""

from micropython import const
from machine import Pin, SPI

CHAR_MAP = {
    #digit
    0: 0x7e, 1: 0x30, 2: 0x6d, 3: 0x79,
    4: 0x33, 5: 0x5b, 6: 0x5f, 7: 0x70,
    8: 0x7f, 9: 0x7b, 10: 0x77, 11: 0x1f,
    12: 0x4e, 13: 0x3d, 14: 0x4f, 15: 0x47,
    '0': 0x7e, '1': 0x30, '2': 0x6d, '3': 0x79,
    '4': 0x33, '5': 0x5b, '6': 0x5f, '7': 0x70,
    '8': 0x7f, '9': 0x7b, 'A': 0x77, 'b': 0x1f,
    'C': 0x4e, 'd': 0x3d, 'E': 0x4f, 'F': 0x47,
    'c': 0x0d, 'h': 0x17, '-': 0x01,
    'H': 0x37, 'O': 0x7e, 'P': 0x4f, 'S': 0x5b,
    'U': 0x3e, '\xb0': 0x63, '.': 0x80
}

CHAR_MAP_POINT = {
    #digit
    0: 0xfe, 1: 0xb0, 2: 0xed, 3: 0xf9,
    4: 0xb3, 5: 0xdb, 6: 0xdf, 7: 0xf0,
    8: 0xff, 9: 0xfb, 10: 0xf7, 11: 0x9f,
    12: 0xce, 13: 0xbd, 14: 0xcf, 15: 0xc7,
    '0': 0xfe, '1': 0xb0, '2': 0xed, '3': 0xf9,
    '4': 0xb3, '5': 0xdb, '6': 0xdf, '7': 0xf0,
    '8': 0xff, '9': 0xfb, 'A': 0xf7, 'b': 0x9f,
    'C': 0xce, 'd': 0xbd, 'E': 0xcf, 'F': 0xc7,
    'c': 0x8d, 'h' : 0x97,
    'H': 0xb7, 'O': 0xfe, 'P': 0xcf, 'S': 0xdb,
    'U': 0xbe, '\xb0': 0x63, '.': 0x80
}
_NOOP = const(0)
_DIGIT0 = const(1)
_DECODEMODE = const(9)
_INTENSITY = const(10)
_SCANLIMIT = const(11)
_SHUTDOWN = const(12)
_DISPLAYTEST = const(15)

class Nuovo7Segment:

    def __init__(self, din, cs, clk):
        self.spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=clk, mosi=din)
        self.cs = cs
        self.cs.init(cs.OUT, True)
        self.buffer = bytearray(8)
        self.init()
        self.clearDisplay()

    def _wr(self, command, data):
        self.cs(0)
        self.spi.write(bytearray([command, data]))
        self.cs(1)

    def init(self):
        for command, data in (
            (_SHUTDOWN, 0),
            (_DISPLAYTEST, 0),
            (_SCANLIMIT, 7),
            (_DECODEMODE, 0),
            (_SHUTDOWN, 1),
        ):
            self._wr(command, data)

    def setBrightness(self, value):
        if not 0 <= value <= 15:
            raise ValueError("Brightness out of range")
        self._wr(_INTENSITY, value)

    def setString(self,str):
        if len(str) == 8:
            for i in range(8):
                self.cs(0)
                self.spi.write(bytearray([_DIGIT0 + i, CHAR_MAP[str[7-i]]]))
                self.cs(1)
        else:
            print("String is not equal 8 character")

    def setDigit(self,digit,num,dot=False):
        if num in CHAR_MAP:
            self.cs(0)
            self.spi.write(bytearray([_DIGIT0 + digit, CHAR_MAP_POINT[num] if dot  else CHAR_MAP[num] ]))
            self.cs(1)
        else:
            print("not have this number")

    def setChar(self,digit,ch,dot=False):
        if ch in CHAR_MAP:
            self.cs(0)
            self.spi.write(bytearray([_DIGIT0 + digit, CHAR_MAP_POINT[ch] if dot  else CHAR_MAP[ch] ]))
            self.cs(1)
        else:
            print("not have this character")

    def setRow(self,digit,bi):
        self.cs(0)
        self.spi.write(bytearray([_DIGIT0 + digit, bi]))
        self.cs(1)

    def clearDisplay(self):
        for i in range(8):
            self.cs(0)
            self.spi.write(bytearray([_DIGIT0 + i, 0x00]))
            self.cs(1)

    def reset(self):
        self.init()