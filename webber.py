from bs4 import BeautifulSoup
import requests
import string

class webber:
    def __init__(self, cookie:string) -> None:
        self.cookie = cookie

    def getSoup(self, url:string):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        return soup

    def getPrice(self, soup):
        price = soup.find('span', {'class' : 'text-robux-lg wait-for-i18n-format-render'}).get_text()

        return price

    def buyItem(self, item_id):
        req = requests.Session()
        req.cookies['.ROBLOXSECURITY'] = self.cookie

        try:
            username = req.get('https://www.roblox.com/mobileapi/userinfo').json()['UserName']
            print('Logged in as : ', username)
        except:
            input('error : Invalid Cookie')
            exit()

        try:
            r = req.post(f'https://economy.roblox.com/v1/purchases/products/{item_id}')
            
            if 'X-CSRF-TOKEN' in r.headers:
                req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
                req.post(f'https://economy.roblox.com/v1/purchases/products/{item_id}')

        except:
            quit()
