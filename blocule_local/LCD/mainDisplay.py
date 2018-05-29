from BloculeUtils import *
from BloculeLogos import *
from optparse import OptionParser
from tron_trnx import *
import time

class mainDisplay():
    def __init__(self, args):        
        print("Args: "+str(args.test)+"\n")
        self.TronTrnx = tron_trnx()
        self.BloculeUtils_ = BloculeUtils()
        self.BloculeLogos_ = BloculeLogos(self.BloculeUtils_)
        while(True):
            self.login_scrn(self.BloculeUtils_.screen[0], self.BloculeUtils_.screen[1], self.BloculeUtils_.screen[2])

    def login_scrn(self, disp, draw, image):
        self.BloculeLogos_.BloculeLogo()
        time.sleep(5)
        self.BloculeUtils_.clr_scrn(disp, draw)
        self.BloculeUtils_.write_text(disp, draw, image, "Enter PIN:",35,20)
        user_text = self.BloculeUtils_.enter_text(disp, draw, image,32, 32,1,0) # set mask = 1 for password    
        if("".join(user_text) == "ad"):
            options_mainDisplay = ["1. Check balance", "2. Send Coin", "Exit "]
            options_pos_mainDisplay = [(15,22), (15,32), (100,50)]

            options_chkCoin = ["Back ", "Exit "]
            options_pos_chkCoin = [(10,50), (100,50)]

            options_sendCoin = ["Back ", "Send ", "Exit "]
            options_pos_sendCoin = [(10,50), (55,50), (100,50)]

            
            sel_op_mainDisplay = 0
            sel_op_chkCoin = 0
            sel_op_sendCoin = 0
            chk_bal_flag = 0
            balance = 0
            while(sel_op_mainDisplay!=2):
                self.BloculeLogos_.TronLogo()
                sel_op_mainDisplay = self.BloculeUtils_.options_menu(disp, draw, image, options_mainDisplay, options_pos_mainDisplay,1) # For diplaying logo set no_clr to 1, before calling logo function

                #If check balance is selected
                if(sel_op_mainDisplay == 0):
                    while(True):
                        if(chk_bal_flag == 0):
                            balance = self.TronTrnx.getBalance()
                            chk_bal_flag = 1
                        self.BloculeLogos_.TronLogo()
                        self.BloculeUtils_.write_text(disp, draw, image, " TRX Balance: ",15,22)
                        self.BloculeUtils_.write_text(disp, draw, image, " "+str(balance)+" ",15,32)
                        sel_op_chkCoin = self.BloculeUtils_.options_menu(disp, draw, image, options_chkCoin, options_pos_chkCoin,1) # For diplaying logo set no_clr to 1, before calling logo function
                        print("sel_op_mainDisplay: "+str(sel_op_mainDisplay)+" sel_op_chkCoin: "+str(sel_op_chkCoin))
                        if((sel_op_chkCoin == 0) or (sel_op_chkCoin == 1)):
                            chk_bal_flag = 0
                            break

                #If sendCoin is selected
                if(sel_op_mainDisplay == 1):
                    while(True):
                        self.BloculeLogos_.TronLogo()
                        self.BloculeUtils_.write_text(disp, draw, image, " Enter Amount: ",15,22)
                        user_amount = self.BloculeUtils_.enter_text(disp, draw, image,32, 32,0,1) # set mask = 1 for password
                        print("Amount: "+"".join(user_amount))
                        sel_op_sendCoin = self.BloculeUtils_.options_menu(disp, draw, image, options_sendCoin, options_pos_sendCoin,1) # For diplaying logo set no_clr to 1, before calling logo function
                        print("sel_op_mainDisplay: "+str(sel_op_mainDisplay)+" sel_op_chkCoin: "+str(sel_op_sendCoin))
                        if(sel_op_sendCoin == 1):
                            status = self.TronTrnx.sendCoin(int("".join(user_amount)))
                            print("Status - "+str(status)+"\n")
                            while(True):
                                self.BloculeLogos_.TronLogo()
                                if(status == "OK"):
                                    self.BloculeUtils_.write_text(disp, draw, image, " Amount Sent! ",15,22)
                                else:
                                    self.BloculeUtils_.write_text(disp, draw, image, " Failed ! ",15,22)
                                sel_op = self.BloculeUtils_.options_menu(disp, draw, image, options_chkCoin, options_pos_chkCoin,1)
                                if(sel_op == 0):
                                    sel_op_sendCoin = 0
                                if(sel_op == 1):
                                    sel_op_sendCoin = 2                                        
                                break;
                                
                        if((sel_op_sendCoin == 0) or (sel_op_sendCoin == 2)):
                            break
                        
                #Reset sendCoin
                if(sel_op_sendCoin == 2):
                    sel_op_mainDisplay = 2
                else:
                    sel_op_sendCoin = 0 #reset this to prevent deadlock

                #Reset chkCoin                        
                if(sel_op_chkCoin == 1):
                    sel_op_mainDisplay = 2
                else:
                    sel_op_chkCoin = 0 #reset this to prevent deadlock

                print("sel_op_mainDisplay: "+str(sel_op_mainDisplay)+" sel_op_chkCoin: "+str(sel_op_chkCoin))
                
            #self.BloculeUtils_.exit_scrn(disp, draw, image)
            self.BloculeUtils_.clr_scrn(disp, draw)
            
        else:
            self.BloculeUtils_.wrong_pin_scrn(disp, draw, image)
            time.sleep(5)
            self.BloculeUtils_.clr_scrn(disp, draw)
    

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--test", dest="test",
                       help="testing...", metavar="VAR")

    (option, args) = parser.parse_args()
    mainDisplay(option)




