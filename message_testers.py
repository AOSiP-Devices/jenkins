#!/usr/bin/env python3

from sys import argv

if len(argv) != 2:
    print("Usage: {} <codename>".format(argv[0]))
    exit(1)

testers = {
    "beryllium": ["akhilnarang", "grewal", "gr0ndpa", "Rokban", "LucentW", "ZTR23"],
    "bonito": ["Skittles9823"],
    "cheeseburger": ["gotenksIN", "HydroPetro"],
    "coral": ["XlxFoXxlX", "MrWilsonxD"],
    "dipper": ["argraur"],
    "dumpling": ["HydroPetro", "edi194"],
    "enchilada": ["anirudhgupta109", "ronell1292k"],
    "fajita": ["ironhydee", "gautamhans1", "edi194"],
    "hotdogb": ["anirudhgupta109"],
    "jasmine_sprout": ["Artsarino", "kenny3fcb"],
    "mata": ["KuranKaname", "Y45HW4N7"],
    "potter": ["NickvBokhorst", "Deadpool_61"],
    "raphael": ["ai94iq", "gr0ndpa", "Pavan_Paps", "M86xKC"],
    "wayne": ["kenny3fcb"],
    "whyred": ["iwantz", "ahmed_tohamy", "Sanchith_Hegde", "anunaym14", "Pavan_Paps"],
    "x2": ["moto999999"],
    "z2_plus": ["Pavan_Paps", "panicker666"],
    "zl1": ["Gabronog", "LucentW"],
}

device = argv[1]

message = ""

if device in testers.keys():
    for tester in testers[device]:
        message += "@{} ".format(tester)
    print(message)
else:
    print("Wrong device {}(?)".format(device))
