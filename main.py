from bs4 import BeautifulSoup
import pyautogui
import requests
import time
import cv2

#before using this code you have ot install 3 things requests, bs4, pyautgui
#pip install requests, pip install pyautogui, pip install beautifulsoup 4

#using .get_text to not get only the text and not get random symbols


#url of the item you want to snipe
url = 'https://web.roblox.com/catalog/63239668/Bat-Tie'
snipe_amount = int(input('enter the amount you want to buy the item for : '))
time.sleep(5)

#variables
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

name = soup.find('h2').get_text()
price = soup.find('span', {'class' : 'text-robux-lg wait-for-i18n-format-render'}).get_text()

#functions
def price_loop():
    time.sleep(1)
    print(name, 'is currenly selling for: $', price)

#exec
while True:
    price_loop()
    if int(price.replace(',', '')) <= snipe_amount:
        button_pos = pyautogui.locateOnScreen('buyButton.PNG', confidence=0.7)
        pyautogui.moveTo(button_pos)
        pyautogui.click()

        print('purchased the item')