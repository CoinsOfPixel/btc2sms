from twilio.rest import Client
from urllib.request import urlopen
import json
import threading
 
print('Type a price to activate the trigger: ')                              trigger = input()
 
def sendSMS():
    account_sid = "YOUR SID"
    auth_token = "YOUR TOKEN"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to = "YOUR PHONE",
        from_= "YOUR TWILIO PHONE",
        body = "BTC price " + str(trigger))
    print(message.sid)
 
def timer():
    threading.Timer(5.0, timer).start()
    url = urlopen('https://www.bitstamp.net/api/ticker/').read()
    btcPrice = float(url[29:36])
    print('Price now @ Bitstamp = ' + str(btcPrice))
    triggerP = float(trigger)
    if btcPrice == triggerP:
        sendSMS()
 
timer()
