import json
import urllib.request as req
import urllib

class tron_trnx():
    def __init__(self):
        self.url='http://localhost:8088'
        # This is temporary
        self.Address = "" # Enter wallet Address
        self.ToAddress = "" # Enter to Address
        self.Password = "" # Account Password


    def getBalance(self):
        payload = {"address": self.Address, "password": self.Password }
        headers = {'Content-type':'application/json',
                        'Accept':'application/json'}
        payload = json.dumps(payload).encode('utf8')
        ret = req.Request(self.url+'/bal/',data=payload, headers=headers)
        resp = req.urlopen(ret)
        data = json.loads(resp.read().decode('utf8'))
        return(data['balance'])
        
    def sendCoin(self, amount):
        payload = {"amount": amount, "password": self.Password, "toaddress": self.ToAddress}
        headers = {'Content-type':'application/json',
                        'Accept':'application/json'}
        payload = json.dumps(payload).encode('utf8')
        ret = req.Request(self.url+'/sendcoin/',data=payload, headers=headers)
        resp = req.urlopen(ret)
        data = json.loads(resp.read().decode('utf8'))
        return(data['req'])
        
