import requests
from requests.exceptions import HTTPError
import os
import json
import time
import json
import shodan
from telegraph import Telegraph


telegraph = Telegraph()
telegraph.create_account(short_name='Hacker228')

# ---------------------------
#61TvA2dNwxNxmWziZxKzR5aO9tFD00Nj

#pHHlgpFt8Ka3Stb5UlTxcaEwciOeF2QM

#fW9K4luEx65RscfUiPDakiqp15jiK5f6

#17xz7MYEBoXLPoi8RdqbgkPwTV2T2H0y >>>>>> Shodan  api keys

#Jvt0B5uZIDPJ5pbCqMo12CqD7pdnMSEd

#n7voYT0TVVzZGVSLaQNRnnkkWgVqxA3b
# ---------------------------

shodanKey = 'PSKINdQe1GyxGgecYz2191H2JoS9qvgD'
api = shodan.Shodan(shodanKey)

defaultColor = '\033[0m'
green = '\033[32m'
red = '\033[31m'	 # это окраска текста с помощью ANSI
cyan = '\033[36m'

firefoxUserAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0'
chromeUserAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F'
operaUserAgent = 'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01'

def startScript():
	global url, pingType
	os.system('clear')
	print(cyan + '''
╔══╦═══╦════╗────╔╗
╚╣╠╣╔═╗║╔╗╔╗║────║║
─║║║╚═╝╠╝║║╠╩═╦══╣║╔══╗
─║║║╔══╝─║║║╔╗║╔╗║║║══╣
╔╣╠╣║────║║║╚╝║╚╝║╚╬══║
╚══╩╝────╚╝╚══╩══╩═╩══╝
My Project: t.me/www_ptoject
Author: t.me/os_people
''' + green +'''Menu:
''' + green +'1)'+ defaultColor + ' Full scan - Full scan site'
 + green +'\n2)'+ defaultColor + ' Base scan - Scan server and delivery of open ports'
 + green +'\n3)'+ defaultColor + ' Port scanner - Output ports open and closed'
 + green +'\n4)'+ defaultColor + ' Ping - Сhecking integrity and quality of the compound'
 + green +'\n5)'+ defaultColor + ' Domain search - Registered Domain Names Search'
 + green +'\n6)'+ defaultColor + ' HTTP Headers - Shows the http response header'
 + green +'\n7)'+ defaultColor + ' IP to Hostname - Shows the domains linked to the ip'
 + green +'\n8)'+ defaultColor + ' Hostname to IP - shows the IP bound to a domain'
 + green +'\n9)'+ defaultColor + ' MX Lookup - check MX record of domain'
 + green +'\n10)'+ defaultColor + ' Subdomain finder - find subdomains'
 + green +'\n11)'+ defaultColor + ' Traceroute - it makes tracing and displays the results'
 + green +'\n12)'+ defaultColor + ' Subnet Lookup - calculates subnet boundaries'
 + green +'\n13)'+ defaultColor + ' ExtractLink - download all links from site'
 + green +'\n14)'+ defaultColor + ' TeleScan - scan and create Telegraph page with info '
 + green +'\n15)'+ defaultColor + ' Proxy Finder - find proxy server')
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
		checkPingType()
	elif selectMode == '5':
		url = input('Введите домен(Enter the domain): ')
		regDomainSearch()
	elif selectMode == '6':
		url = input('Введите домен(Enter the domain): ')
		headReq()
	elif selectMode == '7':
		url = input('Введите IP: (Enter the IP)')
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
		url = input('Введи IP или домен сайта(Enter the IP or domain of the website): ')
		teleMode()
	elif selectMode == '15':
		proxyFinder()
	elif selectMode == 'debug':
		proxyOne()
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
		startScript()

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

def teleMode():
	try:
		baseReq = requests.get('http://ip-api.com/json/' + url + '?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query',headers={'User-Agent': firefoxUserAgent},
			data = {'fields': 'status,message,continent,continentCode,country,'+
 				'countryCode,region,regionName,city,district,zip,lat,lon,'+
 				'timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query'})
		jsonGet = json.loads(baseReq.text)
		subdomainReq = requests.get('https://api.hackertarget.com/hostsearch/?q='+url)
		subdomainText = subdomainReq.text
		subdomainText2 = subdomainText.replace('''
''','</p>')
		ip = jsonGet['query']
		shodanResult = api.host(ip,history=True) # сам запрос
		response = telegraph.create_page(
    str(url),
    html_content=
    '<p>'+'<b>IP</b>: ' + format(str(shodanResult['ip_str']))+'</p>'+
    '<p>'+'<b>ASN: </b>' + format(str(shodanResult['asn']))+'</p>'+
    '<p>'+'<b>ISP: </b>' + format(str(shodanResult['isp']))+'</p>'+
    '<p>'+'<b>Country: </b>' + format(str(shodanResult['country_name']))+'</p>'+
    '<p>'+'<b>City: </b>' + format(str(shodanResult['city']))+'</p>'
    '<p>'+'<b>Organization: </b>' + format(str(shodanResult['org']))+'</p>'
    '<p>'+'<b>Open Ports: </b>' + format(str(shodanResult['ports']))+'</p>'
    '<p>'+'<b>Domains: </b>' + format(str(shodanResult["data"][0]["domains"]))+'</p>'
    '<p>'+'<b>OS: </b>' + format(str(shodanResult["data"][0]["os"]))+'</p>'
    '<p>'+'<b>Vulns: </b>' + format(str(shodanResult["vulns"]))+'</p>'
    '<p>'+'<b>Coordinates:</b>'+'</p>'
    '<p>'+'<b>├ Latitude(Широта):</b> ' + str(jsonGet['lat'])+'</p>'
    '<p>'+'<b>└ Longitude(Долгота):</b>' + str(jsonGet['lon'])+'</p>'
    '<p>'+'<b>Timezone: </b>' +  jsonGet['timezone']+'</p>'
    '<p>'+'<b>Provaider: </b>' +  jsonGet['isp']+'</p>'
    '<p>'+'<b>AS: </b>' +  jsonGet['as']+'</p>'
    '<p>'+'<b>Mobile: </b>' +  str(jsonGet['mobile'])+'</p>'
    '<p>'+'<b>Proxy: </b>' +  str(jsonGet['proxy'])+'</p>'
    '<p>'+'<b>Hosting: </b>' +  str(jsonGet['hosting'])+'</p>'
    '<p>'+'<b>Map: </b>' + '<a href=https://cache.ip-api.com/'+str(jsonGet['lon']) + ',' + str(jsonGet['lat']) +',10' +'>LINK</a></p>'
)
		print('\nLink:\nhttps://telegra.ph/{}'.format(response['path']))
		restartMenu()
	except KeyError:
		baseReq = requests.get('http://ip-api.com/json/' + url + '?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query',headers={'User-Agent': firefoxUserAgent},
			data = {'fields': 'status,message,continent,continentCode,country,'+
 				'countryCode,region,regionName,city,district,zip,lat,lon,'+
 				'timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query'})
		jsonGet = json.loads(baseReq.text)
		ip = jsonGet['query']
		shodanResult = api.host(ip,history=True) # сам запрос
		response = telegraph.create_page(
    str(url),
    html_content=
    '<p>'+'<b>IP</b>: ' + format(str(shodanResult['ip_str']))+'</p>'+
    '<p>'+'<b>ASN: </b>' + format(str(shodanResult['asn']))+'</p>'+
    '<p>'+'<b>ISP: </b>' + format(str(shodanResult['isp']))+'</p>'+
    '<p>'+'<b>Country: </b>' + format(str(shodanResult['country_name']))+'</p>'+
    '<p>'+'<b>City: </b>' + format(str(shodanResult['city']))+'</p>'
    '<p>'+'<b>Organization: </b>' + format(str(shodanResult['org']))+'</p>'
    '<p>'+'<b>Open Ports: </b>' + format(str(shodanResult['ports']))+'</p>'
    '<p>'+'<b>Domains: </b>' + format(str(shodanResult["data"][0]["domains"]))+'</p>'
    '<p>'+'<b>OS: </b>' + format(str(shodanResult["data"][0]["os"]))+'</p>'
    '<p>'+'<b>Vulns:</b> Not Found' +'</p>'
    '<p>'+'<b>Coordinates:</b>'+'</p>'
    '<p>'+'<b>├ Latitude(Широта):</b> ' + str(jsonGet['lat'])+'</p>'
    '<p>'+'<b>└ Longitude(Долгота):</b>' + str(jsonGet['lon'])+'</p>'
    '<p>'+'<b>Timezone: </b>' +  jsonGet['timezone']+'</p>'
    '<p>'+'<b>Provaider: </b>' +  jsonGet['isp']+'</p>'
    '<p>'+'<b>AS: </b>' +  jsonGet['as']+'</p>'
    '<p>'+'<b>Mobile: </b>' +  str(jsonGet['mobile'])+'</p>'
    '<p>'+'<b>Proxy: </b>' +  str(jsonGet['proxy'])+'</p>'
    '<p>'+'<b>Hosting: </b>' +  str(jsonGet['hosting'])+'</p>'
    '<p>'+'<b>Map: </b>' + '<a href=https://cache.ip-api.com/'+str(jsonGet['lon']) + ',' + str(jsonGet['lat']) +',10' +'>LINK</a></p>'
)
		print('\nLink:\nhttps://telegra.ph/{}'.format(response['path']))
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
		startScript()
	elif selectMode == '2':
		print('Exit...')
	else:
		print('Введено не верное значение!\n'+
			'Permission is not the correct value')
def shodanVulnScan():
	try:
		ipGetter = requests.get('http://ip-api.com/json/' + url + '?fields=query',
			headers={'User-Agent': firefoxUserAgent},
			data = {'fields': 'query'})
		jsonIPGetter = json.loads(ipGetter.text)
		ip = jsonIPGetter['query']
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
			startScript()
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
		ipGetter = requests.get('http://ip-api.com/json/' + url + '?fields=query',
			headers={'User-Agent': firefoxUserAgent},
			data = {'fields': 'query'})
		jsonIPGetter = json.loads(ipGetter.text)
		ip = jsonIPGetter['query']
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
	except shodan.APIError as e:
		if format(e) == 'Invalid IP':
			print('\nRussian version:\nОшибка!\nВведите IP а не URL/Hostname!\n'+
				'\nEnglish version:\nError!\nEnter the IP instead of the URL or Hostname')
			restartMenu()
def shodanFunc(): # функция с поиском инфы по Shodan
	try:
		os.system('clear')
		ipGetter = requests.get('http://ip-api.com/json/' + url + '?fields=query', # тут мы узнаем ip домена (если ввели ip)
			headers={'User-Agent': firefoxUserAgent},
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
		shodanSelect = input(green+'''Menu:
1)'''+defaultColor+'''Информация про порты (Information about ports)'''
+green+'\n2)'+defaultColor +'''Информация про уязвимости (Information about the vulnerability)'''
+green+'\n3)'+defaultColor+'''Выйти в меню (To exit the menu)'''
+green+'\n4)'+defaultColor+ '''Выйти (Exit)'''
+'''\nВыберите нужный вариант (Select an option): ''')
		if shodanSelect == '1':
			portNum = 1
			os.system('clear')
			while 9999 > portNum:
				print('\n---------------: '+
					'\nService: ' + format(str(shodanResult["data"][portNum]["_shodan"]['module']))+
					'\nPtr: ' + format(str(shodanResult["data"][portNum]["_shodan"]['ptr'])))
				portNum += 1
		elif shodanSelect == '2':
			cvenum = 0
			while True:
				print('\n-----------------'+
				green +'\nCVE: ' + format(str(shodanResult["vulns"][cvenum]))+
				cyan+'\nLink: https://www.exploit-db.com/search?cve=' + format(str(shodanResult["vulns"][cvenum]))+
				'\nLink: https://www.cvedetails.com/cve/'+format(str(shodanResult["vulns"][cvenum]))+
				'\nLink: https://cve.mitre.org/cgi-bin/cvename.cgi?name='+format(str(shodanResult["vulns"][cvenum]))+
				'\nLink: https://nvd.nist.gov/vuln/detail/'+format(str(shodanResult["vulns"][cvenum]))+defaultColor)
				cvenum += 1
		elif shodanSelect == '3':
			startScript()
		elif shodanSelect == '4':
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
	whoisReq = requests.post('https://check-host.net/ip-info/whois',headers={'User-Agent': firefoxUserAgent}, data={'host':str(url)})
		# whoisReq делает запрос на получение базовой информации о домене.
	print('\nДанные №1: \n' +str(whoisReq.text))

def infoScan():
	try:
		baseReq = requests.get('http://ip-api.com/json/' + url + '?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query',headers={'User-Agent': firefoxUserAgent},
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
'\n' + str(pingJson['nodes']['ru3.node.check-host.net'][1]) + ': '+ str(pingJsonResult['ru3.node.check-host.net'])+
'\n' + str(pingJson['nodes']['se2.node.check-host.net'][1]) + ': '+ str(pingJsonResult['se2.node.check-host.net'])+
'\n' + str(pingJson['nodes']['ua1.node.check-host.net'][1]) + ': '+ str(pingJsonResult['ua1.node.check-host.net'])+
'\n' + str(pingJson['nodes']['ua2.node.check-host.net'][1]) + ': '+ str(pingJsonResult['ua2.node.check-host.net'])+
'\n' + str(pingJson['nodes']['us4.node.check-host.net'][1]) + ': '+ str(pingJsonResult['us4.node.check-host.net']))
	#print(pingReq.text)
	restartMenu()

startScript()
