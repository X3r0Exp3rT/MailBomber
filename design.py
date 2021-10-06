import banner
import colors
import random
import datetime

# input = input(f'{colors.HBPurple}[X3r0]-> ')

def aggrement():
    print(f'{colors.HBRed}{banner.Policy}')

def design():
    print(f'{colors.HBRed}{random.choice(banner.logo)}')
    print(f'{colors.HBPurple}{banner.author}')
    print(f'{colors.HBBlue}{banner.author_details}')
    print(f'{colors.HBYellow}Today\'s date: {datetime.date.today()}')

