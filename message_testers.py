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
    'coral': ['XlxFoXxlX', 'MrWilsonxD'],
    'curtana': ['kenny3fcb'],
    'dipper': ['argraur'],
    'dumpling': ['zorock', 'AnmolChawla', 'HydroPetro'],
    'enchilada': ['anirudhgupta109', 'ronell1292k', 'Giuseppe_Longobardo'],
    'fajita': ['ironhydee', 'gautamhans1', 'edi194'],
    'guacamole': ['anirudhgupta109', 'RandomPooka', 'nezorflame'],
    'hotdogb': ['anirudhgupta109', 'DioKiwi', 'McConvict', 'georgemath24', 'gotenksIN'],
    'jasmine_sprout': ['muthu25'],
    'mata': ['KuranKaname', 'Y45HW4N7'],
    'mido': ['Pavan_Paps'],
    'perseus': ['mjevange'],
    'phoenix': ['akhilnarang'],
    'potter': ['NickvBokhorst', 'Deadpool_61'],
    'raphael': ['Ayushd70', 'federicog86', 'GodsAmongU', 'panicker666', 'ZERJ23',],
    'sargo': ['Skittles9823'],
    'taimen': ['Eamo5'],
    'walleye': ['Eamo5', 'repopic'],
    'wayne': ['kenny3fcb'],
    'whyred': ['iwantz', 'kekguy', 'Sanchith_Hegde', 'Pavan_Paps'],
    'x2': ['moto999999', 'agustindev'],
    'z2_plus': ['panicker666'],
    'zl1': ['Gabronog', 'LucentW', 'agustindev'],
}

device = argv[1]

message = ''

if device in testers.keys():
    for tester in testers[device]:
        message += '@{} '.format(tester)
    print(message)
else:
    print('Wrong device {}(?)'.format(device))
