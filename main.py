import requests, os, threading, toml, random, httpx, time; from datetime import datetime


config = toml.load('config.toml')
quth_key = config.get("discordgg").get("authKey")

token = config.get("user").get("token")
os.system('cls || clear')
guild_id = input('Guild ID?: ')

captchaKey = config.get("captcha").get("captchaKey")
captchaApi = config.get("captcha").get("captchaApi")

os.system('')
class Colwrite:
    def __init__(self):
        self.red = 10
        self.cycle = 0 
    
   
        
        
    def _write(self,datefmt, text):
        
        print(f"\033[37m[ \033[38;2;0;{self.red};255m{datetime.utcnow().strftime(datefmt)} \033[37m] \033[37m{text}")
        if not self.red == 255 and self.cycle == 0:
            self.red += 15
            
        
            
        if self.red > 255:
            self.cycle += 1
            #self.red -= 15
            
                
        if self.cycle > 0:    
            if self.red > 10:
                self.red -= 15
                       
            if self.red == 10:
                self.cycle = 0


prnt = Colwrite()

def Captcha():
    solvedCaptcha = ''
    taskId = httpx.post(f"https://api.{captchaApi}/createTask", json={"clientKey": captchaKey, "task": {"type": "HCaptchaTaskProxyless", "appId": "5C4B67D5-D8E9-485D-AF57-4F427464F0CF", "websiteURL": "https://discord.com/", "websiteKey": "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34", "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"}}, timeout=30).json()
    if taskId.get("errorId") > 0:
        prnt._write(datefmt='%H:%M:%S.%f', text=f"[-] createTask - {taskId.get('errorDescription')}!")
        return 
            
    taskId = taskId.get("taskId")
        
        
    captchaData = httpx.post(f"https://api.{captchaApi}/getTaskResult", json={"clientKey": captchaKey, "taskId": taskId}, timeout=30).json()
    if captchaData.get("status") == "ready":
        solvedCaptcha = captchaData.get("solution").get("gRecaptchaResponse")
            
    return solvedCaptcha

def get_token():
    if not 'id' in requests.Session().get("https://discord.com/api/v10/users/@me", headers={'Authorization': token}).json():
        prnt._write(datefmt='%H:%M:%S.%f', text=f"\x1b[38;5;196mInvalid Token\033[0m")
        return get_token()
            
        
    else:
        return token


token = get_token()
print(token)
def bypassHeader(bot_id, token):
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'Authorization': token,
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        'X-Discord-Locale': 'en-US',
        'X-Debug-Options': 'bugReporterEnabled',
        'Origin': 'https://discord.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': f'https://discord.com/oauth2/authorize?client_id={bot_id}&permissions=1024&scope=bot', 
        'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers',
    }

def get_bots():
    try:
        session = requests.Session()
        bots = []
        alphabet = 'a b c d e f g h i k l m n o p q r s t u v w x y z'
        headers={'Authorization': quth_key}
        qr = alphabet.split(' ')
        for s in qr:
        
            r = session.get(f'https://discord.bots.gg/api/v1/bots?limit=100&q={s}', headers=headers)
            
            for b in r.json()['bots']:
                if b not in bots:
                    bots.append(b['userId'])
                    
    except Exception as err:
        prnt._write(datefmt='%H:%M:%S.%f', text=f"Error --> {err}")
                
    return bots
    
def inviter(userId):
    try:
        session= requests.Session()
        capKey = Captcha()
        r = session.post(f'https://discord.com/api/v9/oauth2/authorize?client_id={userId}&scope=bot%20applications.commands', headers=bypassHeader(userId, token), json={'guild_id': str(guild_id), 'authorize': True, 'permissions': '1024', 'captcha_key': capKey})
        prnt._write(datefmt='%H:%M:%S.%f', text=f"{r.text}")
        if r.status_code == 429:
            time.sleep(2)
        else:
            if r.status_code == 200:
                
                prnt._write(datefmt='%H:%M:%S.%f', text=f"[ {userId} ]\t\tBot joined server --> {guild_id}")
        
    except Exception as err:
        prnt._write(datefmt='%H:%M:%S.%f', text=f"[ {userId} ]\tError --> {err}")
        
        
        
if __name__ == "__main__":
    os.system('cls || clear')
    print(f'''
    
    
    \033[38;2;0;75;255m╦  ╦┬┌─┐┬\033[0m  
    \033[38;2;0;90;255m╚╗╔╝││ ││\033[0m  
    \033[38;2;0;105;255m ╚╝ ┴└─┘┴─┘\033[0m

    
    ''')
    bots = get_bots()
    print(f'Scraped bots: {len(bots)}')
    prnt._write(datefmt='%H:%M:%S.%f', text=f"Scraped bots: {len(bots)}")
    
    delay = config.get('ratelimits').get('delay')
    for b in bots:
        time.sleep(delay)
        inviter(b)
        
