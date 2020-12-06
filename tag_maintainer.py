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
    'curtana': 'kenny3fcb',
    'dipper': 'argraur',
    'dumpling': 'gotenksIN',
    'enchilada': 'anirudhgupta109',
    'fajita': 'anirudhgupta109',
    'flame': 'XlxFoXxlX',
    'guacamole': 'gotenksIN',
    'hotdogb': 'gotenksIN',
    'jasmine_sprout': 'kenny3fcb',
    'mata': 'KuranKaname',
    'miatoll': 'kenny3fcb',
    'mido': 'Adesh15',
    'perseus': 'mjevange',
    'phoenix': 'akhilnarang',
    'potter': 'NickvBokhorst',
    'raphael': 'ai94iq',
    'sargo': 'Skittles9823',
    'taimen': 'Eamo5',
    'walleye': 'Eamo5',
    'wayne': 'kenny3fcb',
    'whyred': 'kenny3fcb',
    'x2': 'agustindev',
    'zl1': 'agustindev',
}

device = argv[1]

maintainer = maintainers.get(device, 'KronicBot')
print(f'@{maintainer} fix {device} build please!')
