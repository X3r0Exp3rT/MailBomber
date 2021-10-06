import design
import colors
import modules
import time


def Main():
    design.design()
    time.sleep(1)

    print(f'\n{colors.HBCyan}[!] You should edit the {colors.HBRed}"config.py" {colors.HBCyan}file in order to Run this script!\n')
    config = str(input(f'{colors.HBYellow}Do you edited the {colors.HBRed}"config.py" {colors.HBYellow}file ? [y/n]: '))

    if config == "y":
        print(f'\n{colors.HBGreen}[!] Loading {colors.HBPurple}"modules.py"\n')
        time.sleep(1)
        modules.send_mail()

    elif config == "n":
        print(f'\n{colors.HBCyan}To edit the {colors.HBRed}"config.py" {colors.HBCyan}file,\nOpen {colors.HBRed}"config.py" {colors.HBCyan}file with any text editor,\nThen change the {colors.HBRed}Gmail {colors.HBCyan}and {colors.HBRed}Password {colors.HBCyan}value within {colors.HBRed}QUOTES.\n{colors.HBCyan}You have to edit the {colors.HBRed}"config.py" {colors.HBCyan}file just for the {colors.HBRed}First time.')
        exit(0)

    else:
        print(f'\n{colors.HBRed}[!] Please! Enter a valid parameter!')
        exit(0)


