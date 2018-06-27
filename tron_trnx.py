import json
import urllib.request as req
import urllib

class tron_trnx():
    def __init__(self):
        self.url='https://api.tronscan.org/api'
        self.Address = "27TX3L8SKbL2QQwPVsQMsJy9xmVYToRRDW1"
        self.ToAddress = "27YzKnFvyuVu1K6vTig4s2urQRuCSdKu83G"
        self.Password = "p4m8K7EAJKNbP2ewrYbqzYmduLJaaTc4"

    def getBalance(self):
        print(self.url+'/account/'+self.Address)
        exit
        with urllib.request.urlopen(self.url+'/account/'+self.Address) as response:
               ret = response.read()
        data = json.loads(ret.decode('utf8'))
        return(data['balance'])
    
    ## TODO        
    # def sendCoin(self, amount):
    #     payload = {"amount": amount, "password": self.Password, "toaddress": self.ToAddress}
    #     headers = {'Content-type':'application/json',
    #                     'Accept':'application/json'}
    #     payload = json.dumps(payload).encode('utf8')
    #     ret = req.Request(self.url+'/sendcoin/',data=payload, headers=headers)
    #     resp = req.urlopen(ret)
    #     data = json.loads(resp.read().decode('utf8'))
    #     return(data['req'])
        
