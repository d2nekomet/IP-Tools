import os
import time

def startInstall():
	os.system('clear')
	print(''' 
╔══╗╔═╦╗╔══╗╔══╗╔══╗╔╗─╔╗─
╚║║╝║║║║║══╣╚╗╔╝║╔╗║║║─║║─
╔║║╗║║║║╠══║─║║─║╠╣║║╚╗║╚╗
╚══╝╚╩═╝╚══╝─╚╝─╚╝╚╝╚═╝╚═╝
Author: t.me/os_people
My Project: t.me/www_ptoject
Меню:
1) Debina (Ubuntu) install
2) Termux install
3) Ручная установка\n''')
	selectMode = input('Выберите нужный вариант: ')
	if selectMode == '1':
		os.system('clear')
		print('Усстановка началась!')
		os.system('sudo apt install python3-pip -y')
		os.system('pip3 install requests')
		os.system('pip3 install fake_useragent')
		os.system('clear')
		print('Чтобы запустить скрипт напишите python3 main.py')
	elif selectMode == '2':
		os.system('clear')
		print('Усстановка началась!')
		os.system('pip3 install requests')
		os.system('pip3 install fake_useragent')
		os.system('clear')
		print('Чтобы запустить скрипт напишите python3 main.py')
	elif selectMode == '3':
		print('''
Если что-то пошло не так, то вот инструкция по ручной установке:
Для Debina/Ubuntu:
1) sudo apt install python3-pip
2) pip3 install requests
3) pip3 install fake_useragent

Для Termux:
1) pip3 install requests
2) pip3 install fake_useragent
''')

startInstall()