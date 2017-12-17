from time import sleep
import requests,re,notify2

regex=re.compile('\d+.\d+')
URL = 'https://www.zebapi.com/api/v1/market/ticker/btc/inr'
r = requests.get(URL)
d={'buy':0,'sell':0}
up = 1000    #Rate by which if value changes you willbe notified
notify2.init('Test')
while True:
    prices = list(map(float,regex.findall(r.text)))[1:3]
    if abs(d['buy']-prices[0])>=1000 and prices[0]>d['buy']:
        n = notify2.Notification('Up-By '+str(prices[0]-d['buy']),'Buy rate :'+str(prices[0])+'\nSell rate :'+str(prices[1]),'/pathto/green.ico')
        n.show()
    elif abs(d['buy']-prices[0])>=1000 and prices[0]<d['buy']:
        n = notify2.Notification('Down-By ' + str(d['buy']-prices[0]), 'Buy rate :'+str(prices[0]) + '\nSell rate :' + str(prices[1]), '/pathto/red.ico')
        n.show()
    d['buy']=prices[0]
    d['sell']=prices[1]
    sleep(60)
    r = requests.get(URL)


