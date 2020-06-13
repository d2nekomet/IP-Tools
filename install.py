import os
import time

colorNum = ['\033[32m','\033[0m','\033[31m','\033[0m','\033[36m'] # это окраска текста с помощью ANSI

def startInstall():
	os.system('clear')
	print(colorNum[4]+''' 
╭━━┳━╮╱╭┳━━━┳━━━━┳━━━┳╮╱╱╭╮
╰┫┣┫┃╰╮┃┃╭━╮┃╭╮╭╮┃╭━╮┃┃╱╱┃┃
╱┃┃┃╭╮╰╯┃╰━━╋╯┃┃╰┫┃╱┃┃┃╱╱┃┃
╱┃┃┃┃╰╮┃┣━━╮┃╱┃┃╱┃╰━╯┃┃╱╭┫┃╱╭╮
╭┫┣┫┃╱┃┃┃╰━╯┃╱┃┃╱┃╭━╮┃╰━╯┃╰━╯┃
╰━━┻╯╱╰━┻━━━╯╱╰╯╱╰╯╱╰┻━━━┻━━━╯
Author: t.me/os_people
My Project: t.me/www_ptoject
'''+colorNum[0] +'''Меню:
'''+colorNum[0]+'''1)'''+colorNum[1]+''' Debina (Ubuntu) install
'''+colorNum[0]+'''2)'''+colorNum[1]+''' Termux install
'''+colorNum[0]+'''3)'''+colorNum[1]+''' Ручная установка\n''')
	selectMode = input('Выберите нужный вариант: ')
	if selectMode == '1':
		os.system('clear')
		print('Установка началась!')
		os.system('sudo apt install python3-pip -y')
		os.system('pip3 install requests')
		os.system('pip3 install fake_useragent')
		os.system('pip3 install shodan')
		os.system('clear')
		print('Чтобы запустить скрипт напишите python3 main.py')
	elif selectMode == '2':
		os.system('clear')
		print('Установка началась!')
		os.system('pip3 install requests')
		os.system('pip3 install fake_useragent')
		os.system('pip3 install shodan')
		os.system('clear')
		print('Чтобы запустить скрипт напишите python3 main.py')
	elif selectMode == '3':
		print('''
Если что-то пошло не так, то вот инструкция по ручной установке:
Для Debina/Ubuntu:
1) sudo apt install python3-pip
2) pip3 install requests
3) pip3 install fake_useragent
4) pip3 install shodan
Для Termux:
1) pip3 install requests
2) pip3 install fake_useragent
3) pip3 install shodan
''')

startInstall()