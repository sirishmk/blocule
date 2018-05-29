import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class BloculeUtils():
    def __init__(self):
        # Input pins:
        self.L_pin = 27
        self.R_pin = 23
        self.C_pin = 4
        self.U_pin = 17
        self.D_pin = 22
        self.A_pin = 5
        self.B_pin = 6

        #Font settings
        self.font = ImageFont.load_default()
        self.font_logo = ImageFont.truetype('./ttf_fonts/PIXEARG_.TTF', 14)    
        self.blocule_logo = ImageFont.truetype('./ttf_fonts/babyblocks.ttf', 15)    
        
        self.screen = self.initialize_display()
        #self.login_scrn(self.screen[0], self.screen[1], self.screen[2])
        #self.button_test(self.screen[0], self.screen[1], self.screen[2])


    def initialize_display(self):
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.A_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
        GPIO.setup(self.B_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
        GPIO.setup(self.L_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
        GPIO.setup(self.R_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
        GPIO.setup(self.U_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
        GPIO.setup(self.D_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
        GPIO.setup(self.C_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
        
        # Raspberry Pi pin configuration:
        RST = None
        
        # 128x64 display with hardware I2C:
        disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
        
        # Initialize library.
        disp.begin()
        
        # Clear display.
        disp.clear()
        disp.display()
        
        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        width = disp.width
        height = disp.height
        image = Image.new('1', (width, height))
        
        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)
        
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        return((disp, draw, image))

    def clr_scrn(self, disp, draw):
        disp.clear()
        disp.display()
        width = disp.width
        height = disp.height
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)    


    def clr_region(self, draw, x,y, fontSizeX, fontSizeY, fill=0):
        # x,y are the cursor position
        # fontSizeX, fontSizeY is the rectangle region
        draw.rectangle((x,y,x+fontSizeX,y+fontSizeY), outline=0, fill=fill)

        
    def write_text(self, disp, draw, image, text, x,y, fill=255, font=None):
        if(font == None):
            maxwidth, unused = draw.textsize(text, font=self.font)
            draw.text((x, y), text, font=self.font, fill=fill)
        else:
            maxwidth, unused = draw.textsize(text, font=font)
            draw.text((x, y), text, font=font, fill=fill)
            
        disp.image(image)
        disp.display()
        time.sleep(.01) 


    def enter_text(self, disp, draw, image, ux, uy, mask=0, letters_digits=0):
        inc_flag_U = 0
        pin_x = ux
        pin_y = uy
        inc_flag_U = 0
        inc_flag_D = 0
        inc_flag_A = 0
        inc_flag_B = 0
        if(letters_digits == 1):
            letter = 48
        else:
            letter = 97
            
        user_text = []
        
        try:
            while 1:
                if GPIO.input(self.U_pin): # button is released
                    inc_flag_U = 0
                    if((mask == 1) and (inc_flag_A ==  1)):
                        self.clr_region(draw,pin_x,pin_y,8,12) # font size 4 px
                        self.write_text(disp, draw, image, '*',pin_x, pin_y)
                    else:
                        self.write_text(disp, draw, image, chr(letter),pin_x, pin_y)
                else: # button is pressed:
                    if(inc_flag_U == 0):                            
                        if(inc_flag_A ==  1):
                            user_text.append(chr(letter))
                            inc_flag_A = 0
                            pin_x = pin_x + 8
                        else:
                            # Don't clear when A is set
                            self.clr_region(draw,pin_x,pin_y,8,12) # font size 4 px
                                
                        letter = letter + 1
                        
                        if(letters_digits == 1):
                            if(letter > 57):
                                letter = 48
                        else:                            
                            if(letter > 122):
                                letter = 97
                            
                        inc_flag_U = 1

                if GPIO.input(self.D_pin): # button is released
                    inc_flag_D = 0
                    if((mask == 1) and (inc_flag_A ==  1)):
                        self.clr_region(draw,pin_x,pin_y,8,12) # font size 4 px
                        self.write_text(disp, draw, image, '*',pin_x, pin_y)
                    else:                    
                        self.write_text(disp, draw, image, chr(letter),pin_x, pin_y)
                else: # button is pressed:
                    if(inc_flag_D == 0):                            
                        if(inc_flag_A ==  1):
                            user_text.append(chr(letter))
                            inc_flag_A = 0
                            pin_x = pin_x + 8
                        else:
                            # Don't clear when A is set
                            self.clr_region(draw,pin_x,pin_y,8,12) # font size 4 px
                                
                        letter = letter - 1

                        if(letters_digits == 1):
                            if(letter < 48):
                                letter = 57
                        else:                            
                            if(letter < 97 ):
                                letter = 122

                        inc_flag_D = 1

                if not GPIO.input(self.A_pin): # button is pressed
                    self.clr_region(draw,pin_x+7,pin_y,8,12) # font size 4 px
                    inc_flag_A = 1

                if not GPIO.input(self.B_pin): # button is pressed
                    user_text.append(chr(letter))
                    return(user_text)

        except KeyboardInterrupt: 
            GPIO.cleanup()

    def highlight_menu(self, draw, fontSizeX, fontSizeY, x,y, text, fill=255):
        self.clr_region(draw, x-4,y-1, (fontSizeX)*int(len(text)-1), fontSizeY, fill)

            
    def wrong_pin_scrn(self, disp, draw, image):
        self.clr_scrn(disp, draw)
        self.write_text(disp, draw, image, "You entered a",25,20)
        self.write_text(disp, draw, image, "wrong pin!",35,28)

    def exit_scrn(self, disp, draw, image):
        self.clr_scrn(disp, draw)
        self.write_text(disp, draw, image, "Bye!",50,20)        
        
    def options_menu(self, disp, draw, image, options, options_pos, no_clr = 0):
        # Options menu sample format
        # options = ["1. Check balance", "2. Send Coin", "Exit "]
        # options_pos = [(15,20), (15,30), (100,50)]

        if(no_clr==0):
            self.clr_scrn(disp, draw)
        
        inc_flag_U = 0
        inc_flag_D = 0
        inc_flag_B = 0
        select_option = 0
        option_num = len(options)

        self.highlight_menu(draw, 8, 12, options_pos[select_option][0], options_pos[select_option][1], options[select_option], 255) # clear the field
        self.write_text(disp, draw, image, options[select_option], options_pos[select_option][0], options_pos[select_option][1], 0) 
        
        for i in range(1,option_num):
            self.write_text(disp, draw, image, options[i], options_pos[i][0], options_pos[i][1])
                
        try:
            while 1:
                if GPIO.input(self.U_pin): # button is released
                    inc_flag_U = 0
                else: # button is pressed:
                    if(inc_flag_U == 0):
                        select_option = select_option - 1
                        inc_flag_U = 1
                        if(select_option < 0):
                            select_option = option_num - 1

                        if(select_option == option_num - 1):
                            self.highlight_menu(draw, 8, 12, options_pos[0][0], options_pos[0][1], options[0], 0) # clear the field
                            self.write_text(disp, draw, image, options[0], options_pos[0][0], options_pos[0][1], 225)
                        else:
                            self.highlight_menu(draw, 8, 12, options_pos[select_option+1][0], options_pos[select_option+1][1], options[select_option+1], 0) # clear the field
                            self.write_text(disp, draw, image, options[select_option+1], options_pos[select_option+1][0], options_pos[select_option+1][1], 225)

                        self.highlight_menu(draw, 8, 12, options_pos[select_option][0], options_pos[select_option][1], options[select_option], 255) # clear the field
                        self.write_text(disp, draw, image, options[select_option], options_pos[select_option][0], options_pos[select_option][1], 0)


                if GPIO.input(self.D_pin): # button is released
                    inc_flag_D = 0
                else: # button is pressed:
                    if(inc_flag_D == 0):
                        select_option = select_option + 1
                        inc_flag_D = 1
                        if(select_option >= option_num):
                            select_option = 0

                        if(select_option == 0):
                            self.highlight_menu(draw, 8, 12, options_pos[option_num-1][0], options_pos[option_num-1][1], options[option_num-1], 0) # clear the field
                            self.write_text(disp, draw, image, options[option_num-1], options_pos[option_num-1][0], options_pos[option_num-1][1], 225)
                        else:
                            self.highlight_menu(draw, 8, 12, options_pos[select_option-1][0], options_pos[select_option-1][1], options[select_option-1], 0) # clear the field
                            self.write_text(disp, draw, image, options[select_option-1], options_pos[select_option-1][0], options_pos[select_option-1][1], 225)

                        self.highlight_menu(draw, 8, 12, options_pos[select_option][0], options_pos[select_option][1], options[select_option], 255) # clear the field
                        self.write_text(disp, draw, image, options[select_option], options_pos[select_option][0], options_pos[select_option][1], 0) 


                if GPIO.input(self.B_pin): # button is released
                    inc_flag_B = 0
                else: # button is pressed:
                    if(inc_flag_B == 0):
                        inc_flag_B = 1
                        return(select_option)
                            
        except KeyboardInterrupt: 
            GPIO.cleanup()
        
            
        
