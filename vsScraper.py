import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

headers = {"User-Agent":"Mozilla/5.0"}
url = 'https://economictimes.indiatimes.com/commoditysummary/symbol-GOLD.cms'
res = requests.get(url,headers=headers)

soup = BeautifulSoup(res.text,'html.parser')
price = soup.find('span',{'class':'commodityPrice'}).text
print(price)

sen=''
buy_or_sell= input('buy or sell? ')
target = float(input('set target price(in decimals) '))
g = 1000

while g > 0:
    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.text,'html.parser')
    price = soup.find('span',{'class':'commodityPrice'}).text
    price = price.replace(',',"") 
    print(price)
    price = float(price)
    if buy_or_sell == 'buy':
        if target >= price :
            sen = 'kudos! you are all set to buy'
            break
        else :
            g = g - 1
            print(g)
    elif buy_or_sell == 'sell' :
        if target <= price :
            sen = 'hola! the target is ready for a sell'
            break
        else :
            g = g - 1
            print(f'tries left : {g}')

if g == 0:
    sen = 'price is not fulfilling your target, if you would like to continue then please re-run the program'
    print(soup.find('span',{'class':'commodityPrice'}).text)

print(sen)

account_sid = #enter your twilio account sid here
auth_token = #enter your twilio auth_tokenn here
client = Client(account_sid,auth_token)

call = client.calls.create(

    twiml= f'<Response><Say>{sen}</Say><Response>',
    to= #enter the number to which you wanna call(don't forget verify the number with twilio)
    from_= #enter the number from where the call has to be initiated assigned you by twilio

)

print(call.sid)