ALT = 5
SHIFT = 6
CTRL = 7
CMD = 4


    # mod =   [0,  # Right GUI - Windows Key
    #          1,  # Right ALT
    #          2,  # Right Control
    #          3,  # Right Shift
    #          4,  # Left GUI
    #          5,  # Left ALT
    #          6,  # Left Shift
    #          7]  # Left Control




keytable = {
    "RESERVED" : (0,),
    "SPOTLIGHT" : (44,[CMD]),
    "ESC" : (41,),
    "1" : (30,),
    "2" : (31,),
    "3" : (32,),
    "4" : (33,),
    "5" : (34,),
    "6" : (35,),
    "7" : (36,),
    "8" : (37,),
    "9" : (38,),
    "0" : (39,),
    "-" : (52,),
    "=" : (46,),
    "BACKSPACE" : (42,),
    "TAB" : (43,),
    "Q" : (20,),
    "W" : (26,),
    "E" : (8,),
    "R" : (21,),
    "T" : (23,),
    "Z" : (28,),
    "U" : (24,),
    "I" : (12,),
    "O" : (18,),
    "P" : (19,),
    "<" : (47,),
    ">" : (48,),
    "ENTER" : (40,),
    "LEFTCTRL" : (224,),
    "A" : (4,),
    "S" : (22,),
    "D" : (7,),
    "F" : (9,),
    "G" : (10,),
    "@" : (10,[ALT]),
    "H" : (11,),
    "J" : (13,),
    "K" : (14,),
    "L" : (15,),
    ";" : (51,),
    "'" : (45,),
    "GRAVE" : (53,),
    "LEFTSHIFT" : (225,),
    "\\" : (36,[SHIFT,ALT]),
    "Y" : (29,),
    "X" : (27,),
    "C" : (6,),
    "V" : (25,),
    "B" : (5,),
    "N" : (17,),
    "M" : (16,),
    "," : (54,),
    "." : (55,),
    "/" : (36,[SHIFT]),
    "RIGHTSHIFT" : (229,),
    "KPASTERISK" : (85,),
    "LEFTALT" : (226,),
    " " : (44,),
    "CAPSLOCK" : (57,),
    "F1" : (58,),
    "F2" : (59,),
    "F3" : (60,),
    "F4" : (61,),
    "F5" : (62,),
    "F6" : (63,),
    "F7" : (64,),
    "F8" : (65,),
    "F9" : (66,),
    "F10" : (67,),
    "NUMLOCK" : (83,),
    "SCROLLLOCK" : (71,),
    "KP7" : (95,),
    "KP8" : (96,),
    "KP9" : (97,),
    "KPMINUS" : (86,),
    "KP4" : (92,),
    "KP5" : (93,),
    "KP6" : (94,),
    "KPPLUS" : (87,),
    "KP1" : (89,),
    "KP2" : (90,),
    "KP3" : (91,),
    "KP0" : (98,),
    "KPDOT" : (99,),
    "ZENKAKUHANKAKU" : (148,),
    "102ND" : (100,),
    "F11" : (68,),
    "F12" : (69,),
    "RO" : (135,),
    "KATAKANA" : (146,),
    "HIRAGANA" : (147,),
    "HENKAN" : (138,),
    "KATAKANAHIRAGANA" : (136,),
    "MUHENKAN" : (139,),
    "KPJPCOMMA" : (140,),
    "KPENTER" : (88,),
    "RIGHTCTRL" : (228,),
    "KPSLASH" : (84,),
    "SYSRQ" : (70,),
    "RIGHTALT" : (230,),
    "HOME" : (74,),
    "UP" : (82,),
    "PAGEUP" : (75,),
    "LEFT" : (80,),
    "RIGHT" : (79,),
    "END" : (77,),
    "DOWN" : (81,),
    "PAGEDOWN" : (78,),
    "INSERT" : (73,),
    "DELETE" : (76,),
    "MUTE" : (239,),
    "VOLUMEDOWN" : (238,),
    "VOLUMEUP" : (237,),
    "POWER" : (102,),
    "KPEQUAL" : (103,),
    "PAUSE" : (72,),
    "KPCOMMA" : (133,),
    "HANGEUL" : (144,),
    "HANJA" : (145,),
    "YEN" : (137,),
    "LEFTMETA" : (227,),
    "RIGHTMETA" : (231,),
    "COMPOSE" : (101,),
    "STOP" : (243,),
    "AGAIN" : (121,),
    "PROPS" : (118,),
    "UNDO" : (122,),
    "FRONT" : (119,),
    "COPY" : (124,),
    "OPEN" : (116,),
    "PASTE" : (125,),
    "FIND" : (244,),
    "CUT" : (123,),
    "HELP" : (117,),
    "CALC" : (251,),
    "SLEEP" : (248,),
    "WWW" : (240,),
    "COFFEE" : (249,),
    "BACK" : (241,),
    "FORWARD" : (242,),
    "EJECTCD" : (236,),
    "NEXTSONG" : (235,),
    "PLAYPAUSE" : (232,),
    "PREVIOUSSONG" : (234,),
    "STOPCD" : (233,),
    "REFRESH" : (250,),
    "EDIT" : (247,),
    "SCROLLUP" : (245,),
    "SCROLLDOWN" : (246,),
    "_" : (56,[SHIFT]),
    "?" : (45,[SHIFT]),
    "[" : (34,[ALT]),
    "#" : (32,[ALT]),
    "F13" : (104,),
    "F14" : (105,),
    "F15" : (106,),
    "F16" : (107,),
    "F17" : (108,),
    "F18" : (109,),
    "F19" : (110,),
    "F20" : (111,),
    "F21" : (112,),
    "F22" : (113,),
    "F23" : (114,),
    "F24" : (115,)
}

def convert(keycode):

    code = keytable[keycode.upper()][0]

    mod =   [0,  # Right GUI - Windows Key
             0,  # Right ALT
             0,  # Right Control
             0,  # Right Shift
             0,  # Left GUI
             0,  # Left ALT
             0,  # Left Shift
             0]  # Left Control

    if (len(keytable[keycode.upper()]) > 1):
        for i in keytable[keycode.upper()][1]:
            mod[i] = 1

    if (keycode.isupper()):
        mod[SHIFT] = 1
    
    bin_str = ""
    for bit in mod:
        bin_str += str(bit)
    return (int(bin_str, 2),code)

