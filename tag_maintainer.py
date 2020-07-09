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
    'guacamole': 'anirudhgupta109',
    'hotdogb': 'anirudhgupta109',
    'jasmine_sprout': 'kenny3fcb',
    'mata': 'KuranKaname',
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
    'z2_plus': 'kenny3fcb',
    'zl1': 'agustindev',
}

device = argv[1]

maintainer = maintainers.get(device, 'KronicBot')
print(f'@{maintainer} fix {device} build please!')
