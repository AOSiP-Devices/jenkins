#!/usr/bin/env python3

from sys import argv

if len(argv) != 2:
    print('Usage: {} <codename>'.format(argv[0]))
    exit(1)

testers = {
    'I001D': ['Adesh15'],
    'beryllium': ['akhilnarang', 'grewal', 'gr0ndpa', 'Rokban', 'LucentW', 'ZTR23'],
    'bonito': ['Skittles9823'],
    'cheeseburger': ['gotenksIN', 'fryevia', 'HydroPetro'],
    'coral': ['XlxFoXxlX', 'MrWilsonxD'],
    'dipper': ['argraur'],
    'dumpling': ['zorock', 'AnmolChawla', 'HydroPetro'],
    'enchilada': ['anirudhgupta109', 'ronell1292k'],
    'fajita': ['ironhydee', 'gautamhans1', 'edi194'],
    'guacamole': ['anirudhgupta109', 'RandomPooka', 'nezorflame'],
    'hotdogb': ['anirudhgupta109', 'DioKiwi', 'McConvict', 'georgemath24', 'subhaam'],
    'jasmine_sprout': ['kenny3fcb', 'muthu25'],
    'mata': ['KuranKaname', 'Y45HW4N7'],
    'mido': ['Pavan_Paps'],
    'perseus': ['mjevange'],
    'phoenix': ['akhilnarang'],
    'potter': ['NickvBokhorst', 'Deadpool_61'],
    'raphael': [
        'ai94iq',
        'federicog86',
        'devanshbajaj',
        'gr0ndpa',
        'Lacentix',
        'M86xKC',
        'Pavan_Paps',
        'panicker666',
    ],
    'sargo': ['Skittles9823'],
    'taimen': ['Eamo5'],
    'walleye': ['Eamo5', 'repopic'],
    'wayne': ['kenny3fcb'],
    'whyred': ['iwantz', 'ahmed_tohamy', 'Sanchith_Hegde', 'anunaym14', 'Pavan_Paps'],
    'x2': ['moto999999', 'agustindev'],
    'z2_plus': ['kenny3fcb', 'panicker666'],
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
