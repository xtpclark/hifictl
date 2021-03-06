#!/usr/bin/env python


class AVR_Command(object):
    """Encaspulate AVR remote control commands."""

    # The following dict is copied from the table on pages 10-11 in the
    # H/K AVR RS-232 interface document
    Commands = {
        "POWER ON":       bytes([0x80, 0x70, 0xC0, 0x3F]),
        "POWER OFF":      bytes([0x80, 0x70, 0x9F, 0x60]),
        "MUTE":           bytes([0x80, 0x70, 0xC1, 0x3E]),
        "AVR":            bytes([0x82, 0x72, 0x35, 0xCA]),
        "DVD":            bytes([0x80, 0x70, 0xD0, 0x2F]),
        "CD":             bytes([0x80, 0x70, 0xC4, 0x3B]),
        "TAPE":           bytes([0x80, 0x70, 0xCC, 0x33]),
        "VID1":           bytes([0x80, 0x70, 0xCA, 0x35]),
        "VID2":           bytes([0x80, 0x70, 0xCB, 0x34]),
        "VID3":           bytes([0x80, 0x70, 0xCE, 0x31]),
        "VID4":           bytes([0x80, 0x70, 0xD1, 0x2E]),
        "VID5":           bytes([0x80, 0x70, 0xF0, 0x0F]),
        "AM/FM":          bytes([0x80, 0x70, 0x81, 0x7E]),
        "6CH/8CH":        bytes([0x82, 0x72, 0xDB, 0x24]),
        "SLEEP":          bytes([0x80, 0x70, 0xDB, 0x24]),
        "SURR":           bytes([0x82, 0x72, 0x58, 0xA7]),
        "DOLBY":          bytes([0x82, 0x72, 0x50, 0xAF]),
        "DTS":            bytes([0x82, 0x72, 0xA0, 0x5F]),
        "DTS NEO:6":      bytes([0x82, 0x72, 0xA1, 0x5E]),
        "LOGIC7":         bytes([0x82, 0x72, 0xA2, 0x5D]),
        "STEREO":         bytes([0x82, 0x72, 0x9B, 0x64]),
        "TEST TONE":      bytes([0x82, 0x72, 0x8C, 0x73]),
        "NIGHT":          bytes([0x82, 0x72, 0x96, 0x69]),
        "1":              bytes([0x80, 0x70, 0x87, 0x78]),
        "2":              bytes([0x80, 0x70, 0x88, 0x77]),
        "3":              bytes([0x80, 0x70, 0x89, 0x76]),
        "4":              bytes([0x80, 0x70, 0x8A, 0x75]),
        "5":              bytes([0x80, 0x70, 0x8B, 0x74]),
        "6":              bytes([0x80, 0x70, 0x8C, 0x73]),
        "7":              bytes([0x80, 0x70, 0x8D, 0x72]),
        "8":              bytes([0x80, 0x70, 0x8E, 0x71]),
        "9":              bytes([0x80, 0x70, 0x9D, 0x62]),
        "0":              bytes([0x80, 0x70, 0x9E, 0x61]),
        "TUNE UP":        bytes([0x80, 0x70, 0x84, 0x7B]),
        "TUNE DOWN":      bytes([0x80, 0x70, 0x85, 0x7A]),
        "VOL UP":         bytes([0x80, 0x70, 0xC7, 0x38]),
        "VOL DOWN":       bytes([0x80, 0x70, 0xC8, 0x37]),
        "PRESET UP":      bytes([0x82, 0x72, 0xD0, 0x2F]),
        "PRESET DOWN":    bytes([0x82, 0x72, 0xD1, 0x2E]),
        "DIGITAL":        bytes([0x82, 0x72, 0x54, 0xAB]),
        "DIGITAL UP":     bytes([0x82, 0x72, 0x57, 0xA8]),
        "DIGITAL DOWN":   bytes([0x82, 0x72, 0x56, 0xA9]),
        "FMMODE":         bytes([0x80, 0x70, 0x93, 0x6C]),
        "DELAY":          bytes([0x82, 0x72, 0x52, 0xAD]),
        "DELAY UP":       bytes([0x82, 0x72, 0x8A, 0x75]),
        "DELAY DOWN":     bytes([0x82, 0x72, 0x8B, 0x74]),
        "COM SET":        bytes([0x82, 0x72, 0x84, 0x7B]),
        "COM UP":         bytes([0x82, 0x72, 0x99, 0x66]),
        "COM DOWN":       bytes([0x82, 0x72, 0x9A, 0x65]),
        "SPEAKER":        bytes([0x82, 0x72, 0x53, 0xAC]),
        "SPEAKER UP":     bytes([0x82, 0x72, 0x8E, 0x71]),
        "SPEAKER DOWN":   bytes([0x82, 0x72, 0x8F, 0x70]),
        "CHANNEL":        bytes([0x82, 0x72, 0x5D, 0xA2]),
        "RDS":            bytes([0x82, 0x72, 0xDD, 0x22]),
        "DIRECT":         bytes([0x80, 0x70, 0x9B, 0x64]),
        "CLEAR":          bytes([0x82, 0x72, 0xD9, 0x26]),
        "MEMORY":         bytes([0x80, 0x70, 0x86, 0x79]),
        "MULTIROOM":      bytes([0x82, 0x72, 0xDF, 0x20]),
        "MULTIROOM UP":   bytes([0x82, 0x72, 0x5E, 0xA1]),
        "MULTIROOM DOWN": bytes([0x82, 0x72, 0x5F, 0xA0]),
        "OSD":            bytes([0x82, 0x72, 0x5C, 0xA3]),
        "OSD LEFT":       bytes([0x82, 0x72, 0xC1, 0x3E]),
        "OSD RIGHT":      bytes([0x82, 0x72, 0xC2, 0x3D]),
        "SURR UP":        bytes([0x82, 0x72, 0x85, 0x7A]),
        "SURR DOWN":      bytes([0x82, 0x72, 0x86, 0x79]),
        "PRESCAN":        bytes([0x80, 0x70, 0x96, 0x69]),
        "DIMMER":         bytes([0x80, 0x70, 0xDC, 0x23]),
        "FAROUDJA":       bytes([0x82, 0x72, 0xC6, 0x39]),
        "TONE":           bytes([0x82, 0x72, 0xC5, 0x3A]),
    }

    @classmethod
    def parse_dgram(cls, data):
        """Parse a datagram containing a command sent to the AVR.

        The AVR receives 4-byte datagram over the serial port (not
        including the protocol overhead managed by AVR_Connection)
        containing remote control commands to be executed by the AVR.
        The 4-byte remote control codes are listed in the above
        dictionary.

        Return a 2-tuple containing 4-byte data value, and the
        corresponding keyword from the above dictionary (or None).
        Throw an exception if parsing failed.
        """
        assert isinstance(data, bytes)
        assert len(data) == 4, "Unexpected length"

        # Reverse-lookup the 4-byte data value in the command dict
        keyword = None
        for k, v in cls.Commands.items():
            if data == v:
                keyword = k
                break
        return (data, keyword)

    @classmethod
    def from_dgram(cls, dgram):
        data, keyword = cls.parse_dgram(dgram)
        return cls(keyword)

    def __init__(self, keyword):
        assert keyword in self.Commands
        self.keyword = keyword

    def __str__(self):
        return "<AVR_Command: '%s'>" % (self.keyword)

    def dgram(self):
        return self.Commands[self.keyword]
