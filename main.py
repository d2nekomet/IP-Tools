import requests
from requests.exceptions import HTTPError
import os
import json
import time
import json
import shodan
import sys
from Art import print_slow, art



os.system('clear')
print_slow(art)



# ---------------------------
#61TvA2dNwxNxmWziZxKzR5aO9tFD00Nj

#pHHlgpFt8Ka3Stb5UlTxcaEwciOeF2QM

#fW9K4luEx65RscfUiPDakiqp15jiK5f6

#17xz7MYEBoXLPoi8RdqbgkPwTV2T2H0y >>>>>> Shodan  api keys

#Jvt0B5uZIDPJ5pbCqMo12CqD7pdnMSEd

#n7voYT0TVVzZGVSLaQNRnnkkWgVqxA3b
# ---------------------------

shodanKey = '61TvA2dNwxNxmWziZxKzR5aO9tFD00Nj'
api = shodan.Shodan(shodanKey)

defaultColor = '\033[0m'
green = '\033[32m'
red = '\033[31m'	 # это окраска текста с помощью ANSI
cyan = '\033[36m'

firefoxUserAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0'
chromeUserAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F'
operaUserAgent = 'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01'






def baseScript():
	global url
	os.system('clear')
	print(cyan + '''
╔══╦═══╦════╗    ╔╗
╚╣╠╣╔═╗║╔╗╔╗║    ║║
 ║║║╚═╝╠╝║║╠╩═╦══╣║╔══╗     My Project: t.me/www_project
 ║║║╔══╝ ║║║╔╗║╔╗║║║══╣     Author: t.me/os_people
╔╣╠╣║    ║║║╚╝║╚╝║╚╬══║
╚══╩╝    ╚╝╚══╩══╩═╩══╝'''
 + green +'''\nMenu:''' 
 + green +'\n1)'+ defaultColor + ' Full scan - Full scan site'
 + green +'\n2)'+ defaultColor + ' Base scan - Scan server and delivery of open ports'
 + green +'\n3)'+ defaultColor + ' Port scanner - Output ports open and closed'
 + green +'\n4)'+ defaultColor + ' HTTP Ping - Сhecking integrity and quality of the compound'
 + green +'\n5)'+ defaultColor + ' Domain search - Registered Domain Names Search'
 + green +'\n6)'+ defaultColor + ' HTTP Headers - Shows the http response header'
 + green +'\n7)'+ defaultColor + ' IP to Hostname - Shows the domains linked to the ip'
 + green +'\n8)'+ defaultColor + ' Hostname to IP - shows the IP bound to a domain'
 + green +'\n9)'+ defaultColor + ' MX Lookup - check MX record of domain'
 + green +'\n10)'+ defaultColor + ' Subdomain finder - find subdomains'
 + green +'\n11)'+ defaultColor + ' Traceroute - it makes tracing and displays the results'
 + green +'\n12)'+ defaultColor + ' Subnet Lookup - calculates subnet boundaries'
 + green +'\n13)'+ defaultColor + ' ExtractLink - download all links from site'
 + green +'\n14)'+ defaultColor + ' Proxy Finder - find proxy server')
	print(red+'Other:'+ defaultColor
+red+'\n1a)'+ defaultColor+ ' Shodan IP info'
+red+'\n2a)'+ defaultColor+ ' Shodan port scanner'
+red+'\n3a)'+ defaultColor+ ' Shodan DNS domen info'
+red+'\n4a)'+ defaultColor+ ' Shodan scan vulnerability'
+red+'\n5a)'+ defaultColor+ ' Shodan search')
	selectMode = input('Выберите нужный вариант (Select an option):')
	print('Выбран режим ' + selectMode + '!')
	time.sleep(1)
	os.system('clear')
	if selectMode == '1':
		url = input('Введи IP или домен сайта(Enter the IP or domain of the website): ')
		fullScan()
	elif selectMode == '2':
		url = input('Введи IP или домен сайта(Enter the IP or domain of the website): ')
		baseScan()
	elif selectMode == '3':
		url = input('Введи IP или домен сайта(Enter the IP or domain of the website): ')
		portFunc()
		restartMenu()
	elif selectMode == '4':
		url = input('Введи IP или домен сайта(Enter the IP or domain of the website): ')
		pingIP()
	elif selectMode == '5':
		url = input('Введите домен(Enter the domain): ')
		regDomainSearch()
	elif selectMode == '6':
		url = input('Введите домен(Enter the domain): ')
		headReq()
	elif selectMode == '7':
		url = input('Введите IP (Enter the IP): ')
		IpToHost()
	elif selectMode == '8':
		url = input('Введите домен(Enter the domain): ')
		HostToIp()
	elif selectMode == '9':
		url = input('Введите домен(Enter the domain): ')
		MXLookup()	
	elif selectMode == '10':
		url = input('Введи IP или домен сайта(Enter the IP or domain of the website): ')
		subdominFunc()
	elif selectMode == '11':
		url = input('Введи IP или домен сайта(Enter the IP or domain of the website): ')
		tracerouteFunc()
	elif selectMode == '12':
		url = input('Введи IP или домен сайта(Enter the IP or domain of the website): ')
		subnetFunc()
	elif selectMode == '13':
		url = input('Введите домен(Enter the domain): ')
		linkExtract()
	elif selectMode == '14':
		proxyFinder()
	elif selectMode == '1a':
		url = input('Введите IP или домен(Enter IP or domain): ')
		shodanFunc()
	elif selectMode == '2a':
		url = input('Введите IP или домен(Enter IP or domain): ')
		shodanPortScan()
	elif selectMode == '3a':
		url = input('Введите IP или домен(Enter IP or domain): ')
		shodanDNSScan()
	elif selectMode == '4a':
		url = input('Введите IP или домен(Enter IP or domain): ')
		shodanVulnScan()
	elif selectMode == '5a':
		url = input('Введите запрос(enter the query): ')
		shodanSearch()
	else:
		print('Введено не верное значение!')
		time.sleep(1)
		baseScript()

def proxyFinder():
	country = input('Введите код страны(Enter the country code): ')
	typeProxy = input('Введите тип прокси(Enter the proxy type): ')
	proxyReq = requests.get('https://www.proxy-list.download/api/v1/get?type='+typeProxy+'&anon=elite&country='+country)
	proxyReq2 = requests.get('https://www.proxy-list.download/api/v1/get?type='+typeProxy+'&anon=transparent&country='+country)
	proxyReq3 = requests.get('https://www.proxy-list.download/api/v1/get?type='+typeProxy+'&anon=anonymous&country='+country)
	otherEliteReq = requests.get(' https://api.proxyscrape.com?request=displayproxies&proxytype='+typeProxy
		+'&timeout=7000&country='+country+'&anonymity=elite&ssl=no')
	
	otherTransparentReq2 = requests.get(' https://api.proxyscrape.com?request=displayproxies&proxytype='+typeProxy
		+'&timeout=7000&country='+country+'&anonymity=transparent&ssl=no')
	
	otherAnonymousReq3 = requests.get(' https://api.proxyscrape.com?request=displayproxies&proxytype='+typeProxy
		+'&timeout=7000&country='+country+'&anonymity=anonymous&ssl=no')
	
	print('Result: \n' +
		'\nElite anon: \n'+ proxyReq.text + otherEliteReq.text +
		'\nTransparent anon: \n ' + proxyReq2.text+ otherTransparentReq2.text + 
		'\nAnonymous anon: \n ' + proxyReq3.text + otherAnonymousReq3.text +
		'\nFINISH!')
	restartMenu()


def shodanSearch():
	try:
		result = requests.get('https://api.shodan.io/shodan/host/search?key='+shodanKey+'&query='+url)
		resultText = json.loads(result.text)
		resultFile = open('result.txt','w+')
		resultNum = 0
		while True:
			resultFile.write('\nResult '+str(resultNum)+':\n'+ 
				'\nPort: '+str(resultText['matches'][resultNum]['port'])+
				'\nIP: '+ str(resultText['matches'][resultNum]['ip_str'])+
				'\nDomains: '+ str(resultText['matches'][resultNum]['domains'])+
				'\nOrganization: '+ str(resultText['matches'][resultNum]['org'])+
				'\nTransport protocol: '+ str(resultText['matches'][resultNum]['transport'])+
				'\nLocation: '+ 
				'\n ├Latitude(Широта): ' + str(resultText['matches'][resultNum]['location']['latitude'])+
				'\n ├Longitude(Долгота): ' + str(resultText['matches'][resultNum]['location']['longitude'])+
				'\n └Country: ' + str(resultText['matches'][resultNum]['location']['country_name'])+'('+str(resultText['matches'][resultNum]['location']['city'])+')'+
				'\n-----------------------\n')
			resultNum += 1
	except shodan.APIError:
		print('\nShodan выдал ошибку. Попробуйте позже или проверьте правильность введенных данных!'+
			'\nShodan gave the error. Please try later or check your entries!')
		restartMenu()
	except IndexError:
		print('\nFINISH!\n'+
			'Откройте файл result.txt с содержанием ответа Shodan.\n'+
			'Open the file result.txt the contents of the reply Shodan.')
		resultFile.close()
		resultNum = 0
		restartMenu()
	except KeyError:
		resultFile.write(result.text)
		print('\nFINISH!\n'+
			'Откройте файл result.txt с содержанием ответа Shodan.\n'+
			'Open the file result.txt the contents of the reply Shodan.')
		resultFile.write('\nResult '+str(resultNum)+':\n'+ 
			'\nPort: '+str(resultText['matches'][resultNum]['port'])+
			'\nIP: '+ str(resultText['matches'][resultNum]['ip_str'])+
			'\nDomains: '+ str(resultText['matches'][resultNum]['domains'])+
			'\nOrganization: '+ str(resultText['matches'][resultNum]['org'])+
			'\nTransport protocol: '+ str(resultText['matches'][resultNum]['transport'])+
			'\nLocation: '+ 
			'\n ├Latitude(Широта): ' + str(resultText['matches'][resultNum]['location']['latitude'])+
			'\n ├Longitude(Долгота): ' + str(resultText['matches'][resultNum]['location']['longitude'])+
			'\n └Country: ' + str(resultText['matches'][resultNum]['location']['country_name'])+'('+str(resultText['matches'][resultNum]['location']['city'])+')'+
			'\n-----------------------\n')
		resultFile.close()
		resultNum = 0
		restartMenu()

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
		baseScript()
	elif selectMode == '2':
		print('Exit...')
	else:
		print('Введено не верное значение!\n'+
			'Permission is not the correct value')
def shodanVulnScan():
	try:
		HostToIpReq = requests.post('https://codebeautify.org/iptools/hostNameToIP',
	headers={'User-Agent': firefoxUserAgent}, 
	data={'domain':url})
		print(HostToIpReq.text)
		HostToIPJson = json.loads(HostToIpReq.text)
		ip = HostToIPJson[0]['ip']
		shodanResult = api.host(ip,history=True)
		os.system('clear')
		print('\nVulns: '+ format(str(shodanResult["vulns"])))	
		print(green+'''\nShow information about the vulnerability?'''+defaultColor)
		selectVuln = input(green+'Enter y/n: '+defaultColor)
		if selectVuln == 'y' or selectVuln =='Y' or selectVuln =='д' or selectVuln =='Д':
			cvenum = 0
			while True:
				print('\n-----------------'+	
				green +'\nCVE: ' + format(str(shodanResult["vulns"][cvenum]))+
				cyan+'\nLink: https://www.exploit-db.com/search?cve=' + format(str(shodanResult["vulns"][cvenum]))+
				'\nLink: https://www.cvedetails.com/cve/'+format(str(shodanResult["vulns"][cvenum]))+
				'\nLink: https://cve.mitre.org/cgi-bin/cvename.cgi?name='+format(str(shodanResult["vulns"][cvenum]))+
				'\nLink: https://nvd.nist.gov/vuln/detail/'+format(str(shodanResult["vulns"][cvenum]))+defaultColor)
				cvenum += 1
			pass
		else:
			baseScript()
	except KeyError:
		print('Not Found!')
	except IndexError:
		print('\nFINISH!')
		restartMenu()

def shodanDNSScan():
	try:
		os.system('clear')
		shodanDNSReq = requests.get('https://api.shodan.io/dns/domain/' + url + '?key='+shodanKey,
			headers={'User-Agent': firefoxUserAgent})
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
		HostToIpReq = requests.post('https://codebeautify.org/iptools/hostNameToIP',
	headers={'User-Agent': firefoxUserAgent}, 
	data={'domain':url})
		HostToIPJson = json.loads(HostToIpReq.text)
		ip = HostToIPJson[0]['ip']
		shodanResult = api.host(ip)
		portNum = 1
		while 9999 > portNum:
			print('\n---------------: '+
					'\nService: ' + format(str(shodanResult["data"][portNum]["_shodan"]['module']))+
					'\nPtr: ' + format(str(shodanResult["data"][portNum]["_shodan"]['ptr'])))
			portNum += 1
	except IndexError:
		print('\nOpen Ports: ' + format(str(shodanResult['ports'])))
		print('\nFINISH!')
		restartMenu()
	except UnboundLocalError:
		shodanResult = api.host(url)
		portNum = 1
		while 9999 > portNum:
			print('\n---------------: '+
					'\nService: ' + format(str(shodanResult["data"][portNum]["_shodan"]['module']))+
					'\nPtr: ' + format(str(shodanResult["data"][portNum]["_shodan"]['ptr'])))
			portNum += 1
	except shodan.APIError as e:
		if format(e) == 'Invalid IP':
			print('\nRussian version:\nОшибка!\nВведите IP а не URL/Hostname!\n'+
				'\nEnglish version:\nError!\nEnter the IP instead of the URL or Hostname')
			restartMenu()
def shodanFunc(): # функция с поиском инфы по Shodan
	try:
		os.system('clear')
		HostToIpReq = requests.post('https://codebeautify.org/iptools/hostNameToIP',
	headers={'User-Agent': firefoxUserAgent}, 
	data={'domain':url})
		HostToIPJson = json.loads(HostToIpReq.text)
		#print(HostToIpReq.text)
		ip = HostToIPJson[0]['ip']
		shodanResult = api.host(ip,history=True) # сам запрос
		info = api.host(ip, history=True)
		#print(shodanResult)
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
		shodanSelect = input(green+'''Menu:
1)'''+defaultColor+'''Информация про порты (Information about ports)'''
+green+'\n2)'+defaultColor +'''Информация про уязвимости (Information about the vulnerability)'''
+green+'\n3)'+defaultColor+'''Выйти в меню (To exit the menu)'''
+green+'\n4)'+defaultColor+ '''Выйти (Exit)'''
+'''\nВыберите нужный вариант (Select an option): ''')
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
		shodanResult = api.host(url,history=True) # сам запрос
		info = api.host(url, history=True)
		#print(shodanResult)
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
		shodanSelect = input(green+'''Menu:
1)'''+defaultColor+'''Информация про порты (Information about ports)'''
+green+'\n2)'+defaultColor +'''Информация про уязвимости (Information about the vulnerability)'''
+green+'\n3)'+defaultColor+'''Выйти в меню (To exit the menu)'''
+green+'\n4)'+defaultColor+ '''Выйти (Exit)'''
+'''\nВыберите нужный вариант (Select an option): ''')
	try:
		if shodanSelect == '1':
			portNum = 1
			os.system('clear')
			while 9999 > portNum:
				print('\n---------------: '+
					'\nService: ' + format(str(shodanResult["data"][portNum]["_shodan"]['module']))+
					'\nPtr: ' + format(str(shodanResult["data"][portNum]["_shodan"]['ptr'])))
				portNum += 1
	except KeyError:
		print('\nFINISH!')
		restartMenu()
	try:
		if shodanSelect == '2':
			cvenum = 0
			while True:
				print('\n-----------------'+
				green +'\nCVE: ' + format(str(shodanResult["vulns"][cvenum]))+
				cyan+'\nLink: https://www.exploit-db.com/search?cve=' + format(str(shodanResult["vulns"][cvenum]))+
				'\nLink: https://www.cvedetails.com/cve/'+format(str(shodanResult["vulns"][cvenum]))+
				'\nLink: https://cve.mitre.org/cgi-bin/cvename.cgi?name='+format(str(shodanResult["vulns"][cvenum]))+
				'\nLink: https://nvd.nist.gov/vuln/detail/'+format(str(shodanResult["vulns"][cvenum]))+defaultColor)
				cvenum += 1
	except IndexError:
		print('\nFINISH!')
		restartMenu()
		if shodanSelect == '3':
			baseScript()
		if shodanSelect == '4':
			print('Exit...')
	except shodan.APIError as e:
		if format(e) == 'Invalid IP':
			print('\nRussian version:\nОшибка!\nВведите IP а не URL/Hostname!\n'+
				'\nEnglish version:\nError!\nEnter the IP instead of the URL or Hostname')
			restartMenu()
		if format(e) == 'Request rate limit reached (1 request/ second). Please wait a second before trying again and slow down your API calls.':
			print('\nRussian version:\nОшибка!\nСлишком много запросов. Попробуйте позже :)'+
				'\nEnglish version:\nError!\nMany requests. Try later :)')

def MXLookup():
	try:
		os.system('clear')
		MXLookupReq = requests.post('https://codebeautify.org/iptools/mxLookup', # запрос на MXlookup
		headers={'User-Agent': firefoxUserAgent}, 
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
	try:
		os.system('clear')
		HostToIpReq = requests.post('https://codebeautify.org/iptools/hostNameToIP',
		headers={'User-Agent': firefoxUserAgent}, 
		data={'domain':url})
		HostToIPJson = json.loads(HostToIpReq.text)
		print('\nHost: ' + url + 
			'\nIP: ' + HostToIPJson[0]['ip'] + 
			'\nClass: ' + HostToIPJson[0]['class'] +
			'\nTTL: ' + str(HostToIPJson[0]['ttl']) + 
			'\nType: ' + HostToIPJson[0]['type'])
		restartMenu()
	except IndexError:
		print('Invelid hostname!')
		restartMenu()

def IpToHost():
	os.system('clear')
	ipToHostReq = requests.post('https://codebeautify.org/iptools/ipToHostname',
	headers={'User-Agent': firefoxUserAgent}, 
	data={'domain':url})
	ipToHostJson = json.loads(ipToHostReq.text)
	print('\nIP: ' + url + 
		'\nHost: ' + ipToHostJson[0]['hostname'])
	restartMenu()

def headReq():
	os.system('clear')
	ipInfoReq = requests.get('https://www.4it.me/api/getavaiblestatus?query=' + url,
	headers={'User-Agent': firefoxUserAgent}, 
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

def whoisFunc():
	whoisReq = requests.post('https://check-host.net/ip-info/whois',headers={'User-Agent': firefoxUserAgent}, data={'host':str(url)})
		# whoisReq делает запрос на получение базовой информации о домене.
	print('\nДанные №1: \n' +str(whoisReq.text))

def infoScan():
	try:
		HostToIpReq = requests.post('https://codebeautify.org/iptools/hostNameToIP',
	headers={'User-Agent': firefoxUserAgent}, 
	data={'domain':url})
		#print(HostToIpReq.text)
		HostToIPJson = json.loads(HostToIpReq.text)
		ip = HostToIPJson[0]['ip']
		baseReq = requests.get('https://api.ipdata.co/'+ip+'?api-key=test')
 			# baseReq делает запрос на получение информации о IP
		jsonGet = json.loads(baseReq.text)
		print('Данные №2: ' + 
'\nIP: ' + jsonGet['ip']+
'\nCity: ' + str(jsonGet['city'])+
'\nCountry: ' + jsonGet['country_name']+ '('+jsonGet['country_code'] +')'+
'\nASN: ' + jsonGet['asn']['asn']+
'\nProvider: ' + jsonGet['asn']['name']+
'\nDomain: ' + jsonGet['asn']['domain']+
'\nType: ' + jsonGet['asn']['type']+
'\nLocation: ' +
'\n ├Latitude(Широта): ' + str(jsonGet['latitude'])+
'\n ├Longitude(Долгота): ' + str(jsonGet['longitude'])+
'\n └Map: '+'https://cache.ip-api.com/'+str(jsonGet['longitude']) + ',' + str(jsonGet['latitude']) +',10'+
'\nIS: ' +
'\n ├  Tor:' + str(jsonGet['threat']['is_tor'])+
'\n ├  Proxy:' + str(jsonGet['threat']['is_proxy'])+
'\n ├  Anonymous:' + str(jsonGet['threat']['is_anonymous'])+
'\n ├  Know Attacker:' + str(jsonGet['threat']['is_known_attacker'])+
'\n ├  Know Abuser:' + str(jsonGet['threat']['is_known_abuser'])+
'\n ├  Threat:' + str(jsonGet['threat']['is_threat'])+
'\n └  Bogon:' + str(jsonGet['threat']['is_bogon'])
)
	except IndexError as e:
		if format(e) == 'list index out of range':
			baseReq = requests.get('https://api.ipdata.co/'+url+'?api-key=test')
 				# baseReq делает запрос на получение информации о IP
			jsonGet = json.loads(baseReq.text)
			print('Данные №2: ' + 
'\nIP: ' + jsonGet['ip']+
'\nCity: ' + str(jsonGet['city'])+
'\nCountry: ' + jsonGet['country_name']+ '('+jsonGet['country_code'] +')'+
'\nASN: ' + jsonGet['asn']['asn']+
'\nProvider: ' + jsonGet['asn']['name']+
'\nDomain: ' + jsonGet['asn']['domain']+
'\nType: ' + jsonGet['asn']['type']+
'\nLocation: ' +
'\n ├Latitude(Широта): ' + str(jsonGet['latitude'])+
'\n ├Longitude(Долгота): ' + str(jsonGet['longitude'])+
'\n └Map: '+'https://cache.ip-api.com/'+str(jsonGet['longitude']) + ',' + str(jsonGet['latitude']) +',10'+
'\nIS: ' +
'\n ├  Tor:' + str(jsonGet['threat']['is_tor'])+
'\n ├  Proxy:' + str(jsonGet['threat']['is_proxy'])+
'\n ├  Anonymous:' + str(jsonGet['threat']['is_anonymous'])+
'\n ├  Know Attacker:' + str(jsonGet['threat']['is_known_attacker'])+
'\n ├  Know Abuser:' + str(jsonGet['threat']['is_known_abuser'])+
'\n ├  Threat:' + str(jsonGet['threat']['is_threat'])+
'\n └  Bogon:' + str(jsonGet['threat']['is_bogon'])
)
		else:
			print('\nНеверные данные! Проверьте IP/Domain!'+
				'\nIncorrect data! Check IP/Domain')
	except KeyError:
		print('\nНеверные данные! Проверьте IP/Domain\n'+
				'Incorrect data! Check IP/Domain')
		restartMenu()

def portFunc():
	try:
		portReq = requests.get('https://www.4it.me/api/checkports?host=' + url + 
			'&ports=20%2C22%2C21%20%2C23%20%2C25%20%2C53%20%2C80%20%2C110%20%2C139%20%2C8000%20%2C8080%20%2C3128%20%2C3389%20%2C6588%2C1080%2C5900%2C8888',
			headers={'User-Agent': firefoxUserAgent}, 
			data={'host' : str(url)} and
			{'ports' : '20,22,21 ,23 ,25 ,53 ,80 ,110 ,139 ,8000 ,8080 ,3128 ,3389 ,6588,1080,5900,8888'})
		time.sleep(1	)
		portReq = requests.get('https://www.4it.me/api/checkports?host=' + url + 
			'&ports=20%2C22%2C21%20%2C23%20%2C25%20%2C53%20%2C80%20%2C110%20%2C139%20%2C8000%20%2C8080%20%2C3128%20%2C3389%20%2C6588%2C1080%2C5900%2C8888',
			headers={'User-Agent': firefoxUserAgent}, 
			data={'host' : str(url)} and
			{'ports' : '20,22,21 ,23 ,25 ,53 ,80 ,110 ,139 ,8000 ,8080 ,3128 ,3389 ,6588,1080,5900,8888'})
		# portReq делает запрос на сканирование портов IP
		portJson = json.loads(portReq.text)
		print('\n\nПорты: ' + 
'\nFTP-DATA(20 PORT): ' + portJson['20'] +
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
	except KeyError as e:
		if format(e) == '20':
			print('\nНеверные данные! Проверьте IP/Domain\n'+
			'Incorrect data! Check IP/Domain')
			restartMenu()
def headersFunc():
	try:
		ipInfoReq = requests.get('https://www.4it.me/api/getavaiblestatus?query=' + url,
			headers={'User-Agent': firefoxUserAgent}, 
			data={'query' : str(url)})
			# ipInfoReq выдает инфу о сервере
		print('\nСервер: ' + str(ipInfoJson['headers']['server']) +
	'\nДата: ' + str(ipInfoJson['headers']['date']) + 
	'\nСоединение: ' + str(ipInfoJson['headers']['connection']))
	except KeyError:
		print('Ошибка Соединения!\n'+
			'connection Error!')
	except KeyError:
		print('Неверные данные!\n'+
			'Incorrect data')
def fullScan():
	os.system('clear')
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
	pingReq = requests.get('https://check-host.net/check-http'+'?host=' + url + '&max_nodes=26', 
	headers={'Accept':'application/json'},   # делает запрос на ping серверов
	data={'host': url})
	print('Подождите 5 секунд!\n'+
		'Wait 5 seconds!')
	time.sleep(5)
	pingJson = json.loads(pingReq.text)
	pingReqResult = requests.get('https://check-host.net/check-result/' + pingJson['request_id'], 
	headers={'Accept':'application/json'}) #отправляет запрос на результаты пингa
	pingJsonResult = json.loads(pingReqResult.text)
	print('\nPing result:\n'+
str(pingJson['nodes']['fi1.node.check-host.net'][1]) +'(' +str(pingJson['nodes']['fi1.node.check-host.net'][2]) + ')' + '\nCode: '+ str(pingJsonResult['fi1.node.check-host.net'][0][3])+'\n'+
'Timeout: ' + str(pingJsonResult['fi1.node.check-host.net'][0][1])+'\n'+
'Status: ' + str(pingJsonResult['fi1.node.check-host.net'][0][2])+'\n'+
'---------------\n'+
str(pingJson['nodes']['fr2.node.check-host.net'][1]) +'(' +str(pingJson['nodes']['fr2.node.check-host.net'][2]) + ')' + '\nCode: '+ str(pingJsonResult['fr2.node.check-host.net'][0][3])+'\n'+
'Timeout: ' + str(pingJsonResult['fr2.node.check-host.net'][0][1])+'\n'+
'Status: ' + str(pingJsonResult['fr2.node.check-host.net'][0][2])+'\n'+
'---------------\n'+
str(pingJson['nodes']['de2.node.check-host.net'][1]) +'(' +str(pingJson['nodes']['de2.node.check-host.net'][2]) + ')' + '\nCode: '+ str(pingJsonResult['de2.node.check-host.net'][0][3])+'\n'+
'Timeout: ' + str(pingJsonResult['de2.node.check-host.net'][0][1])+'\n'+
'Status: ' + str(pingJsonResult['de2.node.check-host.net'][0][2])+'\n'+
'---------------\n'+
str(pingJson['nodes']['ir1.node.check-host.net'][1]) +'(' +str(pingJson['nodes']['ir1.node.check-host.net'][2]) + ')' + '\nCode: '+ str(pingJsonResult['ir1.node.check-host.net'][0][3])+'\n'+
'Timeout: ' + str(pingJsonResult['ir1.node.check-host.net'][0][1])+'\n'+
'Status: ' + str(pingJsonResult['ir1.node.check-host.net'][0][2])+'\n'+
'---------------\n'+
str(pingJson['nodes']['it1.node.check-host.net'][1]) +'(' +str(pingJson['nodes']['it1.node.check-host.net'][2]) + ')' + '\nCode: '+ str(pingJsonResult['it1.node.check-host.net'][0][3])+'\n'+
'Timeout: ' + str(pingJsonResult['it1.node.check-host.net'][0][1])+'\n'+
'Status: ' + str(pingJsonResult['it1.node.check-host.net'][0][2])+'\n'+
'---------------\n'+
str(pingJson['nodes']['kz1.node.check-host.net'][1]) +'(' +str(pingJson['nodes']['kz1.node.check-host.net'][2]) + ')' + '\nCode: '+ str(pingJsonResult['kz1.node.check-host.net'][0][3])+'\n'+
'Timeout: ' + str(pingJsonResult['kz1.node.check-host.net'][0][1])+'\n'+
'Status: ' + str(pingJsonResult['kz1.node.check-host.net'][0][2])+'\n'+
'---------------\n'+
str(pingJson['nodes']['lt1.node.check-host.net'][1]) +'(' +str(pingJson['nodes']['lt1.node.check-host.net'][2]) + ')' + '\nCode: '+ str(pingJsonResult['lt1.node.check-host.net'][0][3])+'\n'+
'Timeout: ' + str(pingJsonResult['lt1.node.check-host.net'][0][1])+'\n'+
'Status: ' + str(pingJsonResult['lt1.node.check-host.net'][0][2])+'\n'+
'---------------\n'+
str(pingJson['nodes']['ua2.node.check-host.net'][1]) +'(' +str(pingJson['nodes']['ua2.node.check-host.net'][2]) + ')' + '\nCode: '+ str(pingJsonResult['ua2.node.check-host.net'][0][3])+'\n'
'Timeout: ' + str(pingJsonResult['ua2.node.check-host.net'][0][1])+'\n'+
'Status: ' + str(pingJsonResult['ua2.node.check-host.net'][0][2])+'\n'+
'---------------\n')
	restartMenu()

baseScript()
