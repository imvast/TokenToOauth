#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: github.com/imvast
@Date: 3/25/2023
"""

from httpx         import Client
from tls_client    import Session
from os            import system


class Oauth:
    def __init__(self) -> None:
        self.client  = Session(client_identifier="firefox_111",ja3_string="771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-13-43-45-51-21,29-23-30-25-24,0-1-2",h2_settings={"HEADER_TABLE_SIZE": 65536,"MAX_CONCURRENT_STREAMS": 1000,"INITIAL_WINDOW_SIZE": 6291456,"MAX_HEADER_LIST_SIZE": 262144},h2_settings_order=["HEADER_TABLE_SIZE","MAX_CONCURRENT_STREAMS","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"],supported_signature_algorithms=["ECDSAWithP256AndSHA256","PSSWithSHA256","PKCS1WithSHA256","ECDSAWithP384AndSHA384","PSSWithSHA384","PKCS1WithSHA384","PSSWithSHA512","PKCS1WithSHA512",],supported_versions=["GREASE", "1.3", "1.2"],key_share_curves=["GREASE", "X25519"],cert_compression_algo="brotli",pseudo_header_order=[":method",":authority",":scheme",":path"],connection_flow=15663105,header_order=["accept","user-agent","accept-encoding","accept-language"])        
        self.session = Client()

    def main(self, uri, token):
        # hd = self.session.get(uri)
        oauth_reqstr = uri # hd.headers.get("location")
        refer_oauth = self.session.get(oauth_reqstr).text.split("<a href=\"")[1].split("\">")[0] # https://discord.com/oauth2/authorize?response_type=code&amp;redirect_uri=https%3A%2F%2Fgiveawaysdrops.com%2Fcallback&amp;scope=identify%20guilds.join&amp;client_id=715370284055789585
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
            'Referer': refer_oauth,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers',
        }
        res = self.client.post(oauth_reqstr, headers=headers, json=payload)#, cookies=cookies)
        if res.status_code == 401:
            return print(f"(!) Invalid Token [{token[:25]}...]")
        try:
            if "location" in res.text:
                locauri = res.json().get("location")
                headers2 = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.5",
                    "connection": "keep-alive",
                    "host": "giveaways.party",
                    "referer": "https://discord.com/",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "cross-site",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"
                }
                res2 = self.session.get(locauri, headers=headers2)
                
                if res2.status_code == 302:
                    return print("(+) Token Added To OAuth")
                else:
                    return print(f"(-) Failed to add token to oauth | {res2.text}")
            elif "You need to verify your account" in res.text:
                return print(f"(!) Invalid Token [{token[:25]}...]")
            else:
                return print(f"(!) Error | {res.text}")
        except Exception as e:
            return print(f"(!) Error | {e}")
        
        
        
if __name__ == "__main__":
    # url example : https://discord.com/oauth2/authorize?client_id=1083384723713314847&redirect_uri=https://restorecord.com/api/callback&response_type=code&scope=identify+guilds.join&state=1061672845593288724
    system("cls")
    print("""
     ╔═╗┌─┐┬ ┬┌┬┐┬ ┬╔╦╗┌─┐┬┌─┌─┐┌┐┌
     ║ ║├─┤│ │ │ ├─┤ ║ │ │├┴┐├┤ │││
     ╚═╝┴ ┴└─┘ ┴ ┴ ┴ ╩ └─┘┴ ┴└─┘┘└┘
          { discord.gg/vast }
    """)
    url = input("(?) Auth URL > ")
    with open('tokens.txt', 'r+') as f: 
        tokens = f.read().splitlines()
    for token in tokens:
        Oauth().main(uri=url, token=token)
