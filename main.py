import requests
from fake_useragent import UserAgent
from requests.exceptions import HTTPError
import os
import json
import time
import json
import shodan

# ---------------------------
#61TvA2dNwxNxmWziZxKzR5aO9tFD00Nj

#pHHlgpFt8Ka3Stb5UlTxcaEwciOeF2QM

#fW9K4luEx65RscfUiPDakiqp15jiK5f6

#17xz7MYEBoXLPoi8RdqbgkPwTV2T2H0y >>>>>> Shodan keys

#Jvt0B5uZIDPJ5pbCqMo12CqD7pdnMSEd

#n7voYT0TVVzZGVSLaQNRnnkkWgVqxA3b
# ---------------------------

shodanKey = 'PSKINdQe1GyxGgecYz2191H2JoS9qvgD'
api = shodan.Shodan(shodanKey)

colorNum = ['\033[32m','\033[0m','\033[31m','\033[0m','\036[0m'] # это окраска текста с помощью ANSI
def startScript():
	global url, pingType
	os.system('clear')
	print('''\033[36m
╔═══╗──────────────╔══╦═══╗╔═══╗
║╔═╗║──────────────╚╣╠╣╔═╗║║╔═╗║
║╚══╦══╦══╦╗╔╦═╦══╗─║║║╚═╝║║╚══╦══╦══╦═╗╔═╗╔══╦═╗
╚══╗║║═╣╔═╣║║║╔╣║═╣─║║║╔══╝╚══╗║╔═╣╔╗║╔╗╣╔╗╣║═╣╔╝
║╚═╝║║═╣╚═╣╚╝║║║║═╣╔╣╠╣║───║╚═╝║╚═╣╔╗║║║║║║║║═╣║
╚═══╩══╩══╩══╩╝╚══╝╚══╩╝───╚═══╩══╩╝╚╩╝╚╩╝╚╩══╩╝
My Project: t.me/www_ptoject
Author: t.me/os_people\033[0m
''' + colorNum[0] +'''Menu:\033[0m
''' + colorNum[0] +'1)'+ colorNum[1] + ' Full scan - Full scan site'
 + colorNum[0] +'\n2)'+ colorNum[1] + ' Base scan - Scan server and delivery of open ports'
 + colorNum[0] +'\n3)'+ colorNum[1] + ' Port scanner - Output ports open and closed'
 + colorNum[0] +'\n4)'+ colorNum[1] + ' Ping - Сhecking integrity and quality of the compound'
 + colorNum[0] +'\n5)'+ colorNum[1] + ' Domain search - Registered Domain Names Search'
 + colorNum[0] +'\n6)'+ colorNum[1] + ' HTTP Headers - Shows the http response header'
 + colorNum[0] +'\n7)'+ colorNum[1] + ' IP to Hostname - Shows the domains linked to the ip'
 + colorNum[0] +'\n8)'+ colorNum[1] + ' Hostname to IP - shows the IP bound to a domain'
 + colorNum[0] +'\n9)'+ colorNum[1] + ' MX Lookup - check MX record of domain'
 + colorNum[0] +'\n10)'+ colorNum[1] + ' Subdomain finder - find subdomains'
 + colorNum[0] +'\n11)'+ colorNum[1] + ' Traceroute - it makes tracing and displays the results'
 + colorNum[0] +'\n12)'+ colorNum[1] + ' Subnet Lookup - calculates subnet boundaries'
 + colorNum[0] +'\n13)'+ colorNum[1] + ' ExtractLink - download all links from site')
	print(colorNum[2]+'Other:'+ colorNum[1]
+colorNum[2]+'\n1a)'+ colorNum[1]+ ' Shodan IP info'
+colorNum[2]+'\n2a)'+ colorNum[1]+ ' Shodan port scanner'
+colorNum[2]+'\n3a)'+ colorNum[1]+ ' Shodan DNS domen info'
+colorNum[2]+'\n4a)'+ colorNum[1]+ ' Shodan scan vulnerability')
	selectMode = input('Выберите нужный вариант (Select an option):')
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
		portFunc()
		restartMenu()
	elif selectMode == '4':
		url = input('Введи IP или домен сайта(не URL!): ')
		checkPingType()
	elif selectMode == '5':
		url = input('Введите домен: ')
		regDomainSearch()
	elif selectMode == '6':
		url = input('Введите домен: ')
		headReq()
	elif selectMode == '7':
		url = input('Введите IP: ')
		IpToHost()
	elif selectMode == '8':
		url = input('Введите домен: ')
		HostToIp()
	elif selectMode == '9':
		url = input('Введите домен: ')
		MXLookup()	
	elif selectMode == '10':
		url = input('Введи IP или домен сайта(не URL!): ')
		subdominFunc()
	elif selectMode == '11':
		url = input('Введи IP или домен сайта(не URL!): ')
		tracerouteFunc()
	elif selectMode == '12':
		url = input('Введи IP или домен сайта(не URL!): ')
		subnetFunc()
	elif selectMode == '13':
		url = input('Введи домен сайта(не URL!): ')
		linkExtract()
	elif selectMode == '1a':
		url = input('Введите IP или домен: ')
		shodanFunc()
	elif selectMode == '2a':
		url = input('Введите IP или домен: ')
		shodanPortScan()
	elif selectMode == '3a':
		url = input('Введите IP или домен: ')
		shodanDNSScan()
	elif selectMode == '4a':
		url = input('Введите IP или домен: ')
		shodanVulnScan()
	else:
		print('Введено не верное значение!')
		time.sleep(1)
		startScript()


def linkExtract():
	os.system('clear')
	linkReq = requests.get('https://api.hackertarget.com/pagelinks/?q='+url)
	print('\nResult:\n'+linkReq.text)
	restartMenu()

def subnetFunc():
	os.system('clear')
	subnetReq = requests.get('https://api.hackertarget.com/subnetcalc/?q='+url)
	print('\nResult:\n'+subnetReq.text)
	restartMenu()

def tracerouteFunc():
	os.system('clear')
	traceroutReq = requests.get('https://api.hackertarget.com/mtr/?q='+url)
	print('\nResult:\n'+traceroutReq.text)
	restartMenu()
def subdominFunc():
	os.system('clear')
	subdomainReq = requests.get('https://api.hackertarget.com/hostsearch/?q='+url)
	print('Please wait...')
	os.system('clear')
	print('\nResult:\n'+subdomainReq.text)
	restartMenu()

def restartMenu():
	print('''\n\033[32mМеню:\033[0m
\033[32m1)\033[0m Войти в главное меню (Enter the main menu)
\033[32m2)\033[0m Выйти (Exit)''')
	selectMode = input('\nВыберите нужный вариант (Select an option): ')
	if selectMode == '1':
		startScript()
	elif selectMode == '2':
		print('Exit...')
	else:
		print('Введено не верное значение!\n'+
			'Permission is not the correct value')
def shodanVulnScan():
	try:
		ipGetter = requests.get('http://ip-api.com/json/' + url + '?fields=query',
			headers={'User-Agent': UserAgent().firefox},
			data = {'fields': 'query'})
		jsonIPGetter = json.loads(ipGetter.text)
		ip = jsonIPGetter['query']
		shodanResult = api.host(ip,history=True)
		os.system('clear')
		print('\nVulns: '+ format(str(shodanResult["vulns"])))
		restartMenu()
	except KeyError:
		print('Not Found!')

def shodanDNSScan():
	try:
		os.system('clear')
		shodanDNSReq = requests.get('https://api.shodan.io/dns/domain/' + url + '?key='+shodanKey,
			headers={'User-Agent': UserAgent().firefox})
		shodanDNSJson = json.loads(shodanDNSReq.text)
		dnsData = 0
		dnsSubData = 0
		os.system('clear')
		print('\nResult ('+url+'): ')
		while True:	# цикл на перечисление JSON результат
			print('\n------\n' +
	'Subdomain: ' + format(str(shodanDNSJson['data'][dnsData]['subdomain']))+
	'\nType: ' + format(str(shodanDNSJson['data'][dnsData]['type']))+
	'\nValue: ' + format(str(shodanDNSJson['data'][dnsData]['value']))+
	'\nLast seen: ' + format(str(shodanDNSJson['data'][dnsData]['last_seen']))+
	'\n------')
			dnsData += 1
	except IndexError:
		print('\nFINISH!')
		restartMenu()

def shodanPortScan():
	try:
		os.system('clear')
		ipGetter = requests.get('http://ip-api.com/json/' + url + '?fields=query',
			headers={'User-Agent': UserAgent().firefox},
			data = {'fields': 'query'})
		jsonIPGetter = json.loads(ipGetter.text)
		ip = jsonIPGetter['query']
		shodanResult = api.host(ip)
		print('\nOpen Ports: ' + format(str(shodanResult['ports'])))
		portNum = 1
		while 9999 > portNum:
			print('\nInfo: ' + format(str(shodanResult["data"][portNum]["_shodan"])))
			portNum += 1
	except IndexError:
		print('\nFINISH!')
		restartMenu()
	except shodan.APIError as e:
		if format(e) == 'Invalid IP':
			print('\nRussian version:\nОшибка!\nВведите IP а не URL/Hostname!\n'+
				'\nEnglish version:\nError!\nEnter the IP instead of the URL or Hostname')
			restartMenu()
def shodanFunc(): # функция с поиском инфы по Shodan
	try:
		os.system('clear')
		ipGetter = requests.get('http://ip-api.com/json/' + url + '?fields=query', # тут мы узнаем ip домена (если ввели ip)
			headers={'User-Agent': UserAgent().firefox},
			data = {'fields': 'query'})
		jsonIPGetter = json.loads(ipGetter.text)
		ip = jsonIPGetter['query']
		shodanResult = api.host(ip,history=True) # сам запрос
		print('\nIP: ' + format(str(shodanResult['ip_str']))+
		'\nASN: ' + format(str(shodanResult['asn']))+
		'\nISP: ' + format(str(shodanResult['isp']))+
		'\nCountry: ' + format(str(shodanResult['country_name']))+
		'\nCity: ' + format(str(shodanResult['city']))+
		'\nOrganization: ' + format(str(shodanResult['org']))+
		'\nOpen Ports: ' + format(str(shodanResult['ports']))+
		'\nTime: ' + format(str(shodanResult["data"][0]["timestamp"]))+
		'\nDomains: ' + format(str(shodanResult["data"][0]["domains"]))+
		'\nOS: ' + format(str(shodanResult["data"][0]["os"]))+
		'\nVulns: ' + format(str(shodanResult["vulns"])))
		#info = api.host(ip, history=True)
		#print(info)
		shodanSelect = input('''
1) Информация про порты
2) Выйти в меню
3) Выйти
Выберите нужный вариант: ''')
		if shodanSelect == '1':
			portNum = 1
			while 9999 > portNum:
				print('\nInfo: ' + format(str(shodanResult["data"][portNum]["_shodan"])))
				portNum += 1
		elif shodanSelect == '2':
			startScript()
		elif shodanSelect == '3':
			print('Exit...')
	except KeyError:
				print('\nIP: ' + format(str(shodanResult['ip_str']))+
		'\nASN: ' + format(str(shodanResult['asn']))+
		'\nISP: ' + format(str(shodanResult['isp']))+
		'\nCountry: ' + format(str(shodanResult['country_name']))+
		'\nCity: ' + format(str(shodanResult['city']))+
		'\nOrganization: ' + format(str(shodanResult['org']))+
		'\nOpen Ports: ' + format(str(shodanResult['ports']))+
		'\nTime: ' + format(str(shodanResult["data"][0]["timestamp"]))+
		'\nDomains: ' + format(str(shodanResult["data"][0]["domains"]))+
		'\nOS: ' + format(str(shodanResult["data"][0]["os"]))+
		'\nVulns: Not Found!')
				restartMenu()
	except IndexError:
		print('\nFINISH!')
		restartMenu()
	except shodan.APIError as e:
		if format(e) == 'Invalid IP':
			print('\nRussian version:\nОшибка!\nВведите IP а не URL/Hostname!\n'+
				'\nEnglish version:\nError!\nEnter the IP instead of the URL or Hostname')
			restartMenu()

def MXLookup():
	try:
		os.system('clear')
		MXLookupReq = requests.post('https://codebeautify.org/iptools/mxLookup', # запрос на MXlookup
		headers={'User-Agent': UserAgent().firefox}, 
		data={'domain':url})
		MXLookupJson = json.loads(MXLookupReq.text)
		targetList = 0
		while True:
			print('\nHost: '+url + # а вот и вывод в более менее удобной форме
				'\nTarget: ' + MXLookupJson[targetList]['target']+
				'\nClass: ' + MXLookupJson[targetList]['class']+
				'\nTTL: ' + str(MXLookupJson[targetList]['ttl'])+
				'\nType: ' + MXLookupJson[targetList]['type'])
			targetList += 1
	except IndexError:
		print('\nFINISH!')
		restartMenu()

def HostToIp():
	os.system('clear')
	HostToIpReq = requests.post('https://codebeautify.org/iptools/hostNameToIP',
	headers={'User-Agent': UserAgent().firefox}, 
	data={'domain':url})
	HostToIPJson = json.loads(HostToIpReq.text)
	print('\nHost: ' + url + 
		'\nIP: ' + HostToIPJson[0]['ip'] + 
		'\nClass: ' + HostToIPJson[0]['class'] +
		'\nTTL: ' + str(HostToIPJson[0]['ttl']) + 
		'\nType: ' + HostToIPJson[0]['type'])
	restartMenu()


def IpToHost():
	os.system('clear')
	ipToHostReq = requests.post('https://codebeautify.org/iptools/ipToHostname',
	headers={'User-Agent': UserAgent().firefox}, 
	data={'domain':url})
	ipToHostJson = json.loads(ipToHostReq.text)
	print('\nIP: ' + url + 
		'\nHost: ' + ipToHostJson[0]['hostname'])
	restartMenu()

def headReq():
	os.system('clear')
	ipInfoReq = requests.get('https://www.4it.me/api/getavaiblestatus?query=' + url,
	headers={'User-Agent': UserAgent().firefox}, 
	data={'query' : str(url)})
	# ipInfoReq выдает инфу о сервере
	ipInfoJson = json.loads(ipInfoReq.text)
	print('\nСервер: ' + str(ipInfoJson['headers']['server']) +
'\nДата: ' + str(ipInfoJson['headers']['date']) + 
'\nСоединение: ' + str(ipInfoJson['headers']['connection']))
	restartMenu()

def regDomainSearch():
	try:
		domainSearchReq = requests.get('https://api.domainsdb.info/v1/domains/search?limit=50&domain='+url,  # get запрос на получене JSON списка доменов
			data={'Accept':'application/json'})
		domainSearchJson = json.loads(domainSearchReq.text)
		print('Домены с именем '+url)
		domainList = 49
		while domainList > 1:  #цикл для выводы всех полученных результатов
			print('------\n'+ str(domainSearchJson['domains'][domainList]['domain'] + 
			'\nДомен умер: ' +domainSearchJson['domains'][domainList]['isDead']))	
			domainList -= 1
		print('\nНайденные совпадения выше.')
		restartMenu()
	except KeyError:
		print('\nCовпадений не найдено.')
		restartMenu()
	except IndexError:
		print('\nЧто-то пошло не так.')
		restartMenu()

def checkPingType():
	global pingType
	os.system('clear')
	pingType = input('Введи метод(tcp,udp,dns или http): ')
	if pingType == 'tcp' or pingType == 'udp' or pingType == 'http' or pingType == 'dns':
		pingIP()
		restartMenu()
	else:
		print('Не правильные данные!')
		time.sleep(1.4)
		startScript()

def whoisFunc():
	whoisReq = requests.post('https://check-host.net/ip-info/whois',headers={'User-Agent': UserAgent().firefox}, data={'host':str(url)})
		# whoisReq делает запрос на получение базовой информации о домене.
	print('\nДанные №1: \n' +str(whoisReq.text))

def infoScan():
	try:
		baseReq = requests.get('http://ip-api.com/json/' + url + '?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query',headers={'User-Agent': UserAgent().firefox},
		 data = {'fields': 'status,message,continent,continentCode,country,'+
 			'countryCode,region,regionName,city,district,zip,lat,lon,'+
 			'timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query'})
 			# baseReq делает запрос на получение информации о IP
		jsonGet = json.loads(baseReq.text)
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
	except KeyError:
		print('Данные №2: \n' + 
'IP: ' + jsonGet['query']+
'\nИх меньше из-за ошибки')

def portFunc():
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

def headersFunc():
	ipInfoReq = requests.get('https://www.4it.me/api/getavaiblestatus?query=' + url,
		headers={'User-Agent': UserAgent().firefox}, 
		data={'query' : str(url)})
		# ipInfoReq выдает инфу о сервере
	print('\nСервер: ' + str(ipInfoJson['headers']['server']) +
'\nДата: ' + str(ipInfoJson['headers']['date']) + 
'\nСоединение: ' + str(ipInfoJson['headers']['connection']))

def fullScan():
	whoisFunc()
	infoScan()
	portFunc()
	restartMenu()

def baseScan():
	os.system('clear')
	infoScan()
	portFunc()
	restartMenu()


def pingIP():  # кривой,но рабочий Ping. Работает с помощью сервиса check-host.net
	os.system('clear')
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
	#print(pingReq.text)
	restartMenu()


startScript()