#!/usr/bin/env python3

from sys import argv

if len(argv) != 2:
    print('Usage: {} <codename>'.format(argv[0]))
    exit(1)

testers = {
    'I001D': ['Adesh15'],
    'beryllium': ['akhilnarang', 'grewal', 'gr0ndpa', 'Rokban', 'LucentW', 'ZTR23'],
    'bonito': ['Skittles9823'],
    'cheeseburger': ['gotenksIN'],
    'coral': ['XlxFoXxlX'],
    'dipper': ['argraur'],
    'dumpling': ['zorock', 'AnmolChawla', 'HydroPetro'],
    'enchilada': [
        'anirudhgupta109',
        'ronell1292k',
        'Giuseppe_Longobardo',
        'Pavan_Paps',
    ],
    'fajita': ['anirudhgupta109', 'ironhydee', 'gautamhans1', 'edi194'],
    'gauguin': ['grewal'],
    'guacamole': ['anirudhgupta109', 'gotenksIN', 'RandomPooka', 'nezorflame'],
    'hotdogb': ['anirudhgupta109', 'gotenksIN', 'McConvict', 'georgemath24'],
    'jasmine_sprout': ['muthu25'],
    'mata': ['KuranKaname', 'Y45HW4N7'],
    'mido': [],
    'perseus': ['mjevange'],
    'phoenix': ['akhilnarang', 'Harmanpreet_Singh', 'TheDemon12'],
    'potter': ['NickvBokhorst', 'Deadpool_61'],
    'raphael': [
        'Ayushd70',
        'federicog86',
        'GodsAmongU',
        'panicker666',
        'ZERJ23',
        'pavanpaps',
    ],
    'sargo': ['Skittles9823'],
    'taimen': ['Eamo5'],
    'walleye': ['Eamo5', 'repopic'],
    'whyred': ['iwantz', 'kekguy', 'Sanchith_Hegde', 'Pavan_Paps', 'DioKiwi'],
    'x2': ['moto999999', 'agustindev'],
    'z2_plus': ['panicker666'],
    'zl1': ['Gabronog', 'LucentW', 'agustindev'],
}

device = argv[1]

message = ''

if device in testers.keys():
    print("@", ", @".join(testers[device]), sep='')
else:
    print('Wrong device {}(?)'.format(device))
