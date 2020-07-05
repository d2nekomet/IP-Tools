import sys, time


defaultColor = '\033[0m'
green = '\033[32m'
red = '\033[31m'	 # это окраска текста с помощью ANSI
cyan = '\033[36m'

art = cyan + '''
╔══╦═══╦════╗    ╔╗
╚╣╠╣╔═╗║╔╗╔╗║    ║║
 ║║║╚═╝╠╝║║╠╩═╦══╣║╔══╗     My Project: t.me/www_project
 ║║║╔══╝ ║║║╔╗║╔╗║║║══╣     Author: t.me/os_people
╔╣╠╣║    ║║║╚╝║╚╝║╚╬══║
╚══╩╝    ╚╝╚══╩══╩═╩══╝'''

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
