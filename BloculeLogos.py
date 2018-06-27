class BloculeLogos():
    def __init__(self, BloculeUtils_):
        self.BloculeUtils_ = BloculeUtils_
        self.disp = self.BloculeUtils_.screen[0]
        self.draw = self.BloculeUtils_.screen[1]
        self.image = self.BloculeUtils_.screen[2]
        
    def TronLogo(self):
        self.BloculeUtils_.clr_scrn(self.disp, self.draw)
        self.draw.polygon([(2, 2), (9,8), (9,19)], outline=0, fill=255)  
        self.draw.polygon([(2, 2), (9,8), (18,3)], outline=0, fill=255)  
        self.draw.polygon([(21, 7), (9,8), (18,3)], outline=0, fill=255) 
        self.draw.polygon([(21, 7), (9,8), (9,19)], outline=0, fill=255) 
        self.draw.line([(0, 20), (128,20)], fill=255)  
        self.disp.display()        
        self.BloculeUtils_.write_text(self.disp, self.draw, self.image, " Tron",19,0,255, self.BloculeUtils_.font_logo)

    def BloculeLogo(self):
        self.BloculeUtils_.clr_scrn(self.disp, self.draw)
        self.disp.display()        
        self.BloculeUtils_.write_text(self.disp, self.draw, self.image, " BLOCULE",0,25,255, self.BloculeUtils_.blocule_logo)
        
