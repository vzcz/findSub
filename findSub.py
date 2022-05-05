import requests
import sys
from rich.console import Console
from colored import fg
import math

file = input("Enter file :")

try:
        v = open(file, 'r').read()
except:
        print("Sorry, I couldn't find a file with the name Ali"+file)
        sys.exit()

v = v.split("\n")

urlInput = input("Enter url :")
def site(urlFilter):
        if "https://www" in urlFilter:
                site = urlFilter.replace("https://www.", "")
        elif "http://www" in urlFilter:
                site = urlFilter.replace("http://www.", "")
        elif "http://" in urlFilter:
                site = urlFilter.replace("http://", "")
        elif "https://" in urlFilter:
                site = urlFilter.replace("https://", "")
        elif "www" in urlFilter:
                site = urlFilter.replace("www.", "")
        else:
                site = urlFilter
        return site

url= site(urlInput)

#Check site
try:
        test = requests.get("https://"+url)
        if test.status_code == 404:
                sys.exit()

except:
        sys.exit()

def subchk(link, subFile):
        num = 0
        console = Console()
        for i in subFile:
                with console.status(f"[bold green][{num} / {len(subFile)} ({math.trunc(num / len(subFile) * 100)}%) ]Working to find Subdomain...."):
                        suburl = f"https://{i}.{link}"
                        try:
                                res = requests.get(suburl)
                                if res.status_code != 404:
                                        if res.status_code == 200:
                                                print(f"{fg('green')}{suburl} : {str(res.status_code)}")
                                        else:
                                                print(f"{fg('red')}{suburl} : {str(res.status_code)}")
                        except requests.exceptions.ConnectionError:
                                pass
                        except :
                                break
                        num = num + 1

subchk(url, v)