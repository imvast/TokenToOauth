#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: github.com/imvast
@Date: 5/24/2023
"""

from httpx         import Client
from tls_client    import Session
from os            import system
from threading     import Thread
from colorama      import Fore
from terminut      import printf as print, inputf as input, init; init(colMain=Fore.MAGENTA)


class Oauth:
    def __init__(self, uri) -> None:
        self.client  = Session(client_identifier="firefox_111", random_tls_extension_order=True)        
        self.session = Client()
        self.uri     = uri

    def getUris(self):
        if "https://restorecord.com/verify" in self.uri:
            return print("RestoreCord Links Not Available Yet. Use the link it sends you to after pressing verify.")
            uri = "https://discord.com" + monk.split('href="https://discord.com')[1].split('"')[0]
            self.oauth_reqstr = uri.split("/oauth2")[0] + "/api/v9/oauth2" + self.uri.split("/oauth2")[1]
            self.refer_oauth = uri
        elif "oauth2/authorize" in self.uri and not "api/v9" in self.uri:
            self.oauth_reqstr = self.uri.split("/oauth2")[0] + "/api/v9/oauth2" + self.uri.split("/oauth2")[1]
            self.refer_oauth = self.uri
        elif "api/v9" in self.uri:
            self.oauth_reqstr = self.uri
            self.refer_oauth = self.uri.replace("api/v9", "")
        else:
            hd = self.session.get(self.uri)
            self.oauth_reqstr = hd.headers.get("location") # api.v9
            self.refer_oauth = self.session.get(self.oauth_reqstr).text.split("<a href=\"")[1].split("\">")[0] # https://discord.com/oauth2/authorize?response_type=code&amp;redirect_uri=https%3A%2F%2Fgiveawaysdrops.com%2Fcallback&amp;scope=identify%20guilds.join&amp;client_id=715370284055789585
    
    def submitOauth(self, res):
        if "location" in res.text:
            locauri = res.json().get("location")
            hosturi = locauri.replace("https://", "").replace("http://", "").split("/")[0]
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.5","connection": "keep-alive",
                "host": hosturi,
                "referer": "https://discord.com/","sec-fetch-dest": "document","sec-fetch-mode": "navigate","sec-fetch-site": "cross-site","sec-fetch-user": "?1", "upgrade-insecure-requests": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"
            }
            res2 = self.session.get(locauri, headers=headers)
            
            if res2.status_code in (302, 307):
                return print("(+) Token Added To OAuth")
            else:
                return print(f"(-) Failed to add token to oauth | {res2.text}, {res2.status_code}")
        elif "You need to verify your account" in res.text:
            return print(f"(!) Invalid Token [{token[:25]}...]")
        else:
            return print(f"(!) Submit Error | {res.text}")
            
    def main(self, token):
        self.getUris()
        payload = {
            "permissions": "0",
            "authorize": True
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Authorization': token,
            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwOS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzExMS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTExLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTg3NTk5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'X-Discord-Locale': 'en-US',
            'X-Debug-Options': 'bugReporterEnabled',
            'Origin': 'https://discord.com',
            'Connection': 'keep-alive',
            'Referer': self.refer_oauth,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers',
        }
        res = self.client.post(self.oauth_reqstr, headers=headers, json=payload)
        if res.status_code == 401:
            return print(f"(!) Invalid Token [{token[:25]}...]")
        if res.status_code == 200:
            try:
                return self.submitOauth(res)
            except Exception as e:
                return print(f"(!) Error | {e}")
        else:
            return print(f"(!) Error | {res.text}")
        
        
if __name__ == "__main__":
    # url example : http://giveaways.party/login/auth
    system("cls")
    x1 = Fore.MAGENTA
    x2 = Fore.LIGHTMAGENTA_EX
    print("""
     %s╔═╗%s┌─┐┬ ┬┌┬┐┬ ┬%s╔╦╗%s┌─┐┬┌─┌─┐┌┐┌
     %s║ ║%s├─┤│ │ │ ├─┤%s ║ %s│ │├┴┐├┤ │││
     %s╚═╝%s┴ ┴└─┘ ┴ ┴ ┴%s ╩ %s└─┘┴ ┴└─┘┘└┘
          { %sdiscord.gg/vast%s }
    %s""" % (x2, x1, x2, x1, x2, x1, x2, x1, x2, x1, x2, x1, x2, x1, Fore.RESET), showTimestamp=False)
    
    url = input("(?) Auth URL > ")
    auth = Oauth(uri=url)
    
    with open('tokens.txt', 'r+') as f: 
        tokens = f.read().splitlines()
    for token in tokens:
        Thread(target=auth.main, args=(token,)).start()
