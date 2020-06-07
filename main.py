import requests
from fake_useragent import UserAgent
from requests.exceptions import HTTPError
import os
import json
import time
import json

cookies = dict(cookies_are='cookies')

def startScript():
	global url, pingType
	os.system('clear')
	print('''
╔══╗╔═╗╔═╗╔╦╗╔═╗╔═╗     ╔══╗╔═╗     ╔══╗╔═╗╔══╗╔═╦╗╔═╦╗╔═╗╔═╗
║══╣║╦╝║╔╝║║║║╬║║╦╝     ╚║║╝║╬║     ║══╣║╔╝║╔╗║║║║║║║║║║╦╝║╬║
╠══║║╩╗║╚╗║║║║╗╣║╩╗     ╔║║╗║╔╝     ╠══║║╚╗║╠╣║║║║║║║║║║╩╗║╗╣
╚══╝╚═╝╚═╝╚═╝╚╩╝╚═╝     ╚══╝╚╝─     ╚══╝╚═╝╚╝╚╝╚╩═╝╚╩═╝╚═╝╚╩╝
Author: t.me/os_people
My Project: t.me/www_ptoject
Меню:
1) Full scan - Full scan site
2) Base scan - Scan server and delivery of open ports
3) Port scanner - Output ports open and closed
4) Ping- Сhecking integrity and quality of the compound''')
	selectMode = input('Выберите нужный вариант: ')
	print('Выбран режим ' + selectMode + '!')
	time.sleep(1)
	os.system('clear')
	if selectMode == '1':
		url = input('Введи IP или домен сайта(не URL!): ')
		fullScan()
	elif selectMode == '2':
		url = input('Введи IP или домен сайта(не URL!): ')
		baseScan()
	elif selectMode == '3':
		url = input('Введи IP или домен сайта(не URL!): ')
		portScan()
	elif selectMode == '4':
		url = input('Введи IP: ')
		checkPingType()


def checkPingType():
	global pingType
	pingType = input('Введи метод(tcp,udp,dns или http): ')
	if pingType == 'tcp' or pingType == 'udp' or pingType == 'http' or pingType == 'dns':
		pingIP()
	else:
		print('Не правильные данные!')
		time.sleep(1.4)
		startScript()

def fullScan():
	whoisReq = requests.post('https://check-host.net/ip-info/whois',headers={'User-Agent': UserAgent().firefox}, data={'host':str(url)})
	# whoisReq делает запрос на получение базовой информации о домене.

	baseReq = requests.get('http://ip-api.com/json/' + url + '?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query',headers={'User-Agent': UserAgent().firefox},
	 data = {'fields': 'status,message,continent,continentCode,country,'+
 			'countryCode,region,regionName,city,district,zip,lat,lon,'+
 			'timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query'})
	# baseReq делает запрос на получение информации о IP

	portReq = requests.get('https://www.4it.me/api/checkports?host=' + url + 
		'&ports=20%2C22%2C21%20%2C23%20%2C25%20%2C53%20%2C80%20%2C110%20%2C139%20%2C8000%20%2C8080%20%2C3128%20%2C3389%20%2C6588%2C1080%2C5900%2C8888',
			headers={'User-Agent': UserAgent().firefox}, 
			data={'host' : str(url)} and
				{'ports' : '20,22,21 ,23 ,25 ,53 ,80 ,110 ,139 ,8000 ,8080 ,3128 ,3389 ,6588,1080,5900,8888'})
	# portReq делает запрос на сканирование портов IP

	ipInfoReq = requests.get('https://www.4it.me/api/getavaiblestatus?query=' + url,
		headers={'User-Agent': UserAgent().firefox}, 
		data={'query' : str(url)})
	# ipInfoReq выдает инфу о сервере

	jsonGet = json.loads(baseReq.text)
	print('\nДанные №1: \n' +str(whoisReq.text))
	print('Данные №2: \n' + 
'IP: ' + jsonGet['query'] + 
'\nСоединение: ' + jsonGet['status'] + 
'\nCountry: ' + jsonGet['country'] + 
'\nCountry code: ' + jsonGet['countryCode'] + 
'\nRegion: ' + jsonGet['regionName'] + 
'\nRegion code: ' + jsonGet['region'] +
'\nCity: ' + jsonGet['city'] +
'\nZip: ' + jsonGet['zip'] + 
'\nCoordinates: \n ├ Latitude(Широта): ' + str(jsonGet['lat']) + 
'\n └ Longitude(Долгота): ' + str(jsonGet['lon']) + 
'\nTimezone: ' + jsonGet['timezone'] + 
'\nProvaider: ' + jsonGet['isp'] + 
'\nOrganization: ' + jsonGet['org'] + 
'\nAS: ' + jsonGet['as'] + 
'\nAS Name: ' + jsonGet['asname'] + 
'\nDomen: ' + jsonGet['reverse'] + 
'\nMobile: ' + str(jsonGet['mobile']) + 
'\nProxy: ' + str(jsonGet['proxy']) + 
'\nHosting: ' + str(jsonGet['hosting']))
	print('\nРасположение IP на карте: \n' +
'https://cache.ip-api.com/'+str(jsonGet['lon']) + ',' + str(jsonGet['lat']) +',10')
	portJson = json.loads(portReq.text)
	print('\n\nПорты: \n' + 
'FTP-DATA(20 PORT): ' + portJson['20'] +
'\nFTP(21 PORT): ' + portJson['21'] +
'\nSSH(22 PORT): ' + portJson['22'] + 
'\nTelnet(23 PORT): ' + portJson['23'] + 
'\nSMTP(25 PORT): ' + portJson['25'] + 
'\nDNS(53 PORT): ' + portJson['53'] + 
'\nHTTP(80 PORT): ' + portJson['80'] + 
'\nPOP3(110 PORT): ' + portJson['110'] + 
'\nNETBIOS-SSN(139 PORT): ' + portJson['139'] + 
'\niRDMI(Intel Remote Desktop Management Interface - 8000 PORT): ' + portJson['8000'] +
'\nHTTP ALT(8080 PORT): ' + portJson['8080'],
'\nHTTP used by Web caches(3128 PORT): ' + portJson['3128'] +
'\nRDP(Microsoft Terminal Server - 3389 PORT): ' + portJson['3389'] + 
'\nAnalogX Proxy Server(6588 PORT): ' + portJson['6588'] + 
'\nSOCKS(1080 PORT): ' + portJson['1080'] + 
'\nVNC(5900 PORT): ' + portJson['5900'] + 
'\nNewsEDGE(8888 PORT): ' + portJson['8888'])
#print(r.text)
	ipInfoJson = json.loads(ipInfoReq.text)
	print('Данные №3')
	print('\nСервер: ' + str(ipInfoJson['headers']['server']) +
'\nДата: ' + str(ipInfoJson['headers']['date']) + 
'\nСоединение: ' + str(ipInfoJson['headers']['connection']))
	print('\nFINISH!')

def baseScan():
	portReq = requests.get('https://www.4it.me/api/checkports?host=' + url + 
		'&ports=20%2C22%2C21%20%2C23%20%2C25%20%2C53%20%2C80%20%2C110%20%2C139%20%2C8000%20%2C8080%20%2C3128%20%2C3389%20%2C6588%2C1080%2C5900%2C8888',
		headers={'User-Agent': UserAgent().firefox}, 
		data={'host' : str(url)} and
				{'ports' : '20,22,21 ,23 ,25 ,53 ,80 ,110 ,139 ,8000 ,8080 ,3128 ,3389 ,6588,1080,5900,8888'})
	# portReq делает запрос на сканирование портов IP

	ipInfoReq = requests.get('https://www.4it.me/api/getavaiblestatus?query=' + url,
		headers={'User-Agent': UserAgent().firefox}, 
		data={'query' : str(url)})
	portJson = json.loads(portReq.text)
	# ipInfoReq выдает инфу о сервере
	print('\n\nПорты: \n' + 
'FTP-DATA(20 PORT): ' + portJson['20'] +
'\nFTP(21 PORT): ' + portJson['21'] +
'\nSSH(22 PORT): ' + portJson['22'] + 
'\nTelnet(23 PORT): ' + portJson['23'] + 
'\nSMTP(25 PORT): ' + portJson['25'] + 
'\nDNS(53 PORT): ' + portJson['53'] + 
'\nHTTP(80 PORT): ' + portJson['80'] + 
'\nPOP3(110 PORT): ' + portJson['110'] + 
'\nNETBIOS-SSN(139 PORT): ' + portJson['139'] + 
'\niRDMI(Intel Remote Desktop Management Interface - 8000 PORT): ' + portJson['8000'] +
'\nHTTP ALT(8080 PORT): ' + portJson['8080'],
'\nHTTP used by Web caches(3128 PORT): ' + portJson['3128'] +
'\nRDP(Microsoft Terminal Server - 3389 PORT): ' + portJson['3389'] + 
'\nAnalogX Proxy Server(6588 PORT): ' + portJson['6588'] + 
'\nSOCKS(1080 PORT): ' + portJson['1080'] + 
'\nVNC(5900 PORT): ' + portJson['5900'] + 
'\nNewsEDGE(8888 PORT): ' + portJson['8888'])
#print(r.text)
	ipInfoJson = json.loads(ipInfoReq.text)
	print('Данные №3')
	print('\nСервер: ' + str(ipInfoJson['headers']['server']) +
'\nДата: ' + str(ipInfoJson['headers']['date']) + 
'\nСоединение: ' + str(ipInfoJson['headers']['connection']))
	print('\nFINISH!')

def portScan():
	portReq = requests.get('https://www.4it.me/api/checkports?host=' + url + 
		'&ports=20%2C22%2C21%20%2C23%20%2C25%20%2C53%20%2C80%20%2C110%20%2C139%20%2C8000%20%2C8080%20%2C3128%20%2C3389%20%2C6588%2C1080%2C5900%2C8888',
		headers={'User-Agent': UserAgent().firefox}, 
		data={'host' : str(url)} and
				{'ports' : '20,22,21 ,23 ,25 ,53 ,80 ,110 ,139 ,8000 ,8080 ,3128 ,3389 ,6588,1080,5900,8888'})
	# portReq делает запрос на сканирование портов IP
	portJson = json.loads(portReq.text)
	print('\n\nПорты: \n' + 
'FTP-DATA(20 PORT): ' + portJson['20'] +
'\nFTP(21 PORT): ' + portJson['21'] +
'\nSSH(22 PORT): ' + portJson['22'] + 
'\nTelnet(23 PORT): ' + portJson['23'] + 
'\nSMTP(25 PORT): ' + portJson['25'] + 
'\nDNS(53 PORT): ' + portJson['53'] + 
'\nHTTP(80 PORT): ' + portJson['80'] + 
'\nPOP3(110 PORT): ' + portJson['110'] + 
'\nNETBIOS-SSN(139 PORT): ' + portJson['139'] + 
'\niRDMI(Intel Remote Desktop Management Interface - 8000 PORT): ' + portJson['8000'] +
'\nHTTP ALT(8080 PORT): ' + portJson['8080'],
'\nHTTP used by Web caches(3128 PORT): ' + portJson['3128'] +
'\nRDP(Microsoft Terminal Server - 3389 PORT): ' + portJson['3389'] + 
'\nAnalogX Proxy Server(6588 PORT): ' + portJson['6588'] + 
'\nSOCKS(1080 PORT): ' + portJson['1080'] + 
'\nVNC(5900 PORT): ' + portJson['5900'] + 
'\nNewsEDGE(8888 PORT): ' + portJson['8888'])

def pingIP():  # кривой,но рабочий Ping. Работает с помощью сервиса check-host.net 
	pingReq = requests.get('https://check-host.net/check-'+str(pingType)+'?host=' + url + '&max_nodes=26', 
	headers={'Accept':'application/json'},   # делает запрос на ping серверов
	data={'host': url})
	print('Подождите 10 секунд!')
	time.sleep(10)
	pingJson = json.loads(pingReq.text)
	print(pingJson['request_id'])
	pingReqResult = requests.get('https://check-host.net/check-result/' + pingJson['request_id'], 
	headers={'Accept':'application/json'}) #отправляет запрос на результаты пингa
	pingJsonResult = json.loads(pingReqResult.text)
	print('\n'+pingType+' Ping result:\n' + 
'\n' + str(pingJson['nodes']['ch1.node.check-host.net'][1]) + ': '+ str(pingJsonResult['ch1.node.check-host.net'])+
'\n' + str(pingJson['nodes']['de2.node.check-host.net'][1]) + ': '+ str(pingJsonResult['de2.node.check-host.net'])+
'\n' + str(pingJson['nodes']['de3.node.check-host.net'][1]) + ': '+ str(pingJsonResult['de3.node.check-host.net'])+
'\n' + str(pingJson['nodes']['fi1.node.check-host.net'][1]) + ': '+ str(pingJsonResult['fi1.node.check-host.net'])+
'\n' + str(pingJson['nodes']['fr2.node.check-host.net'][1]) + ': '+ str(pingJsonResult['fr2.node.check-host.net'])+
'\n' + str(pingJson['nodes']['it1.node.check-host.net'][1]) + ': '+ str(pingJsonResult['it1.node.check-host.net'])+
'\n' + str(pingJson['nodes']['it2.node.check-host.net'][1]) + ': '+ str(pingJsonResult['it2.node.check-host.net'])+
'\n' + str(pingJson['nodes']['it3.node.check-host.net'][1]) + ': '+ str(pingJsonResult['it3.node.check-host.net'])+
'\n' + str(pingJson['nodes']['lt1.node.check-host.net'][1]) + ': '+ str(pingJsonResult['lt1.node.check-host.net'])+
'\n' + str(pingJson['nodes']['md1.node.check-host.net'][1]) + ': '+ str(pingJsonResult['md1.node.check-host.net'])+
'\n' + str(pingJson['nodes']['nl1.node.check-host.net'][1]) + ': '+ str(pingJsonResult['nl1.node.check-host.net'])+
'\n' + str(pingJson['nodes']['nl2.node.check-host.net'][1]) + ': '+ str(pingJsonResult['nl2.node.check-host.net'])+
'\n' + str(pingJson['nodes']['ru1.node.check-host.net'][1]) + ': '+ str(pingJsonResult['ru1.node.check-host.net'])+
'\n' + str(pingJson['nodes']['ru2.node.check-host.net'][1]) + ': '+ str(pingJsonResult['ru2.node.check-host.net'])+
'\n' + str(pingJson['nodes']['ru3.node.check-host.net'][1]) + ': '+ str(pingJsonResult['ru3.node.check-host.net'])+
'\n' + str(pingJson['nodes']['se2.node.check-host.net'][1]) + ': '+ str(pingJsonResult['se2.node.check-host.net'])+
'\n' + str(pingJson['nodes']['ua1.node.check-host.net'][1]) + ': '+ str(pingJsonResult['ua1.node.check-host.net'])+
'\n' + str(pingJson['nodes']['ua2.node.check-host.net'][1]) + ': '+ str(pingJsonResult['ua2.node.check-host.net'])+
'\n' + str(pingJson['nodes']['us4.node.check-host.net'][1]) + ': '+ str(pingJsonResult['us4.node.check-host.net']))
	#print(pingReq.text)u
startScript()