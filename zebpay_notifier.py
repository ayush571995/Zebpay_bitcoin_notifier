from time import sleep
import requests,json,notify2

URL = 'https://www.zebapi.com/api/v1/market/ticker/btc/inr'
r = requests.get(URL)
d={'buy':0,'sell':0}
notify2.init('Test')
prices = json.loads(r.text)
d['buy'] = prices['buy']
d['sell'] = prices['sell']
n = notify2.Notification('Price-Alert','Buy rate :' + str(d['buy']) + '\nSell rate :' + str(d['sell']))
n.show()
sleep(15)

while True:
    new_price = json.loads(requests.get(URL).text)
    if new_price['buy']>d['buy']:
        notify2.Notification('Buy rate Up by ' + str(new_price['buy'] - d['buy']),
                                 'Buy rate :' + str(new_price['buy']) + '\nSell rate :' + str(new_price['sell'])).show()

    elif new_price['sell']>d['sell']:
        notify2.Notification('Sell rate Up by ' + str(new_price['sell'] - d['sell']),
                                 'Buy rate :' + str(new_price['buy']) + '\nSell rate :' + str(new_price['sell'])).show()
    elif new_price['buy']<d['buy']:
        notify2.Notification('Buy rate Down-By ' + str(d['buy']-new_price['buy']),
                                 'Buy rate :' + str(new_price['buy']) + '\nSell rate :' + str(new_price['sell'])).show()
    elif new_price['sell']<d['sell']:
        notify2.Notification('Sell rate Down-By ' + str(d['sell'] - new_price['sell']),
                                 'Buy rate :' + str(new_price['buy']) + '\nSell rate :' + str(new_price['sell'])).show()
    elif new_price['buy']>d['buy'] and new_price['sell']>d['sell']:
        notify2.Notification('Buy and Sell rate Up ' ,
                                 'Buy rate :' +str(d['buy'])+'------>'+ str(new_price['buy']) + '\nSell rate :' +str(d['sell'])+'------>'+ str(new_price['sell'])).show()
    elif new_price['buy']<d['buy'] and new_price['sell']<d['sell']:
        notify2.Notification('Buy and Sell rate down' ,
                                 'Buy rate :' +str(d['buy'])+'------>'+ str(new_price['buy']) + '\nSell rate :' +str(d['sell'])+'------>'+ str(new_price['sell'])).show()
    d=new_price
    sleep(60)




