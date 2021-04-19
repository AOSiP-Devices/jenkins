#!/usr/bin/env python3

from sys import argv

if len(argv) != 2:
    print('Usage: {} <codename>'.format(argv[0]))
    exit(1)

maintainers = {
    'I001D': 'Adesh15',
    'beryllium': 'akhilnarang',
    'bonito': 'Skittles9823',
    'cheeseburger': 'gotenksIN',
    'coral': 'XlxFoXxlX',
    'dipper': 'argraur',
    'dumpling': 'gotenksIN',
    'enchilada': 'anirudhgupta109',
    'fajita': 'anirudhgupta109',
    'flame': 'XlxFoXxlX',
    'gauguin': 'grewal',
    'guacamole': 'gotenksIN',
    'hotdogb': ['anirudhgupta109', 'gotenksIN'],
    'mata': 'KuranKaname',
    'mido': 'Adesh15',
    'perseus': 'mjevange',
    'phoenix': 'akhilnarang',
    'potter': 'NickvBokhorst',
    'raphael': 'ai94iq',
    'sargo': 'Skittles9823',
    'taimen': 'Eamo5',
    'walleye': 'Eamo5',
    'x2': 'agustindev',
    'zl1': 'agustindev',
}

device = argv[1]

if device in maintainers.keys():
    blamelist = ', @'.join(maintainers[device])
else:
    blamelist = 'KronicBot '
print(f'@{blamelist} fix {device} build please!')
