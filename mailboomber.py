import design
import colors
import redirect
import time


class Initializing():
    def __init__(self):
        design.aggrement()
        rules = input(f'{colors.HBYellow}Do you agree ? [y/n]: ')

        if rules == "y":
            print(f'\n{colors.HBGreen}[*] Initializing Programme...\n')
            time.sleep(1)
            redirect.Main()
        elif rules == "n":
            print(f'\n{colors.HBRed}[!] Sorry! You have to Agree on that Policy!')
            exit(0)
        else:
            print(f'\n{colors.HBRed}[!] Please! Enter a valid parameter!')
            exit(0)

if __name__ == '__main__':
    Initializing()