from webber import webber
import json

url = 'https://web.roblox.com/catalog/'

file = open('items.json', 'r')
jfile = json.load(file)

sniper = webber('Your cookie here')

def checkProps():
    for buy_price, item_id in jfile.items():
        soup = sniper.getSoup(f'{url}{item_id}')
        price = sniper.getPrice(soup)
        
        f_price = price.replace(',', '')

        if int(f_price) < int(buy_price):
            sniper.buyItem(item_id)
        else:
            print(f'{item_id} : {f_price} => {buy_price}')      

def main():
    while True:
        checkProps()

if __name__ == '__main__':
    main()
