#!/usr/bin/env python3

from sys import argv

if len(argv) != 2:
    print("Usage: {} <codename>".format(argv[0]))
    exit(1)

testers = {
    "berkeley": ["srisurya95"],
    "beryllium": ["akhilnarang", "grewal", "gr0ndpa", "Rokban", "LucentW", "ZTR23"],
    "bullhead": ["anirudhgupta109", "Skittles8923"],
    "cheeseburger": ["HydroPetro", "fryevia", "gotenksIN"],
    "crosshatch": ["Fire69Flame"],
    "dipper": ["argraur"],
    "dumpling": ["divadsn", "HydroPetro"],
    "enchilada": ["anirudhgupta109", "ohayoubaka", "MrWilsonxD", "ronell1292k"],
    "fajita": ["ironhydee", "gautamhans1"],
    "guacamole": ["nezorflame"],
    "kiwi": ["coldhans"],
    "mata": ["KuranKaname", "Y45HW4N7"],
    "mido": ["Adesh15"],
    "oneplus3": ["HydroPetro", "theshinybeast", "nezorflame"],
    "platina": ["nysadev"],
    "potter": ["NickvBokhorst", "Deadpool_61"],
    "rapheal": ["ai94iq", "gr0ndpa", "Pavan_Paps"],
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
