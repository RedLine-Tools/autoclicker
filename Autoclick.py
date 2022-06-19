import webbrowser
import os, time
from colorama import Fore
import socket
import platform
from datetime import datetime
import threading
from pynput.mouse import Button, Controller
  
# pynput.keyboard is used to watch events of 
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, KeyCode

os.system('Generator Nitro | By Dievid#0408')
os.system('cls')

comenzando = input(f'{Fore.RED}Redline@Clave => ')

hostname = socket.gethostname()



if comenzando == "DievidOnTop":
        os.system('title AutoClicker By Dievid#0408')
        os.system('cls')

        date = datetime.now()

        banner = f'''{Fore.RED}
        ______         _ _ _          _____           _     
        | ___ \       | | (_)        |_   _|         | |    
        | |_/ /___  __| | |_ _ __   ___| | ___   ___ | |___ 
        |    // _ \/ _` | | | '_ \ / _ \ |/ _ \ / _ \| / __|
        | |\ \  __/ (_| | | | | | |  __/ | (_) | (_) | \__ \\
        \_| \_\___|\__,_|_|_|_| |_|\___\_/\___/ \___/|_|___/
        '''
        print(banner)
        my_system = platform.uname()
        print(f"Desktop : {hostname}")
        print(f"Sistema: {my_system.system}")
        print(f"Nombre del nodo: {my_system.node}")
        print(f"Lansamiento: {my_system.release}")
        print(f"Version: {my_system.version}")
        print(f"Maquina: {my_system.machine}")
        print(f"Procesador: {my_system.processor}")
        print(f"Dia y hora de ejecucion :{date}")

        time.sleep(1.5)

        os.system('cls')

        bns = """
         _____                           _               _   _ _ _             
        |  __ \                         | |             | \ | (_) |            
        | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __  |  \| |_| |_ _ __ ___  
        | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| | . ` | | __| '__/ _ \ 
        | |_\ \  __/ | | |  __/ | | (_| | || (_) | |    | |\  | | |_| | | (_) | 
         \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|    \_| \_/_|\__|_|  \___/ 

        [1] Nitro
        [2] Checker
        [3] Discord
        [4] Credits
        """

        print(bns)

        asd = input('Redline@Generator (1 , 2 , 3 , 4) => ')

        if(asd == "1"):
            os.system('cls')
            print('Proximamente . . .')
            os.system('pause')
        
        if(asd == "2"):
            os.system('cls')
            print('Proximamente . . .')
            os.system('pause')

        if(asd == "3"):
            os.system('cls')
            print('Proximamente . . .')
            os.system('pause')

        if(asd == "1"):
            os.system('cls')
            print('Proximamente . . .')
            os.system('pause')

        if(asd == "101"):
            contra = input(str(f'{Fore.RED}\nRedLine@Password => '))
            if contra == "RedlineOnTop" :
                os.system('cls')
                banner = f'''{Fore.RED}
                 /$$$$$$               /$$                /$$$$$$  /$$ /$$           /$$                          
                 /$$__  $$            | $$               /$$__  $$| $$|__/          | $$                          
                | $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$ | $$  \__/| $$ /$$  /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
                | $$$$$$$$| $$  | $$|_  $$_/   /$$__  $$| $$      | $$| $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
                | $$__  $$| $$  | $$  | $$    | $$  \ $$| $$      | $$| $$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
                | $$  | $$| $$  | $$  | $$ /$$| $$  | $$| $$    $$| $$| $$| $$      | $$_  $$ | $$_____/| $$      
                | $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/|  $$$$$$/| $$| $$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
                |__/  |__/ \______/    \___/   \______/  \______/ |__/|__/ \_______/|__/  \__/ \_______/|__/      

                [1] Autoclick
                [2] Creditos
                [3] Discord
                '''
                print(banner)

                option = input('Redline@Autoclick (1 , 2 , 3) => ')
                if option == '1' :
                    mode = input('Redline@Autoclick//Mode (Blatant) => ')
                    if mode == 'Blatant' :
                        def cps(cantidad):
                                delay = cantidad
                                button = Button.left
                                start_stop_key = KeyCode(char='6')
                                stop_key = KeyCode(char='7')
                                
                                # threading.Thread is used 
                                # to control clicks
                                class ClickMouse(threading.Thread):
                                    
                                # delay and button is passed in class 
                                # to check execution of auto-clicker
                                    def __init__(self, delay, button):
                                        super(ClickMouse, self).__init__()
                                        self.delay = delay
                                        self.button = button
                                        self.running = False
                                        self.program_running = True
                                
                                    def start_clicking(self):
                                        self.running = True
                                
                                    def stop_clicking(self):
                                        self.running = False
                                
                                    def exit(self):
                                        self.stop_clicking()
                                        self.program_running = False
                                
                                    # method to check and run loop until 
                                    # it is true another loop will check 
                                    # if it is set to true or not, 
                                    # for mouse click it set to button 
                                    # and delay.
                                    def run(self):
                                        while self.program_running:
                                            while self.running:
                                                mouse.click(self.button)
                                                time.sleep(self.delay)
                                            time.sleep(0.1)
                                
                                
                                # instance of mouse controller is created
                                mouse = Controller()
                                click_thread = ClickMouse(delay, button)
                                click_thread.start()
                                
                                
                                # on_press method takes 
                                # key as argument
                                def on_press(key):
                                    
                                # start_stop_key will stop clicking 
                                # if running flag is set to true
                                    if key == start_stop_key:
                                        if click_thread.running:
                                            click_thread.stop_clicking()
                                        else:
                                            click_thread.start_clicking()
                                            
                                    # here exit method is called and when 
                                    # key is pressed it terminates auto clicker
                                    elif key == stop_key:
                                        click_thread.exit()
                                        listener.stop()
                                
                                
                                with Listener(on_press=on_press) as listener:
                                    listener.join()
                        
                        cantidad = input('Redline@Autoclick//Modo//Cantidad (1 - 20) => ')

                        if cantidad == '1':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(1)

                        if cantidad == '2':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.5)

                        if cantidad == '3':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.32)

                        if cantidad == '4':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.25)

                        if cantidad == '5':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.2)

                        if cantidad == '6':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.15)
                        
                        if cantidad == '7':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.135)

                        if cantidad == '8':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.12)

                        if cantidad == '9':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.1)
                        
                        if cantidad == '10':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.08)

                        if cantidad == '11':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.079)

                        if cantidad == '12':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.075)

                        if cantidad == '13':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.0625)

                        if cantidad == '14':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.063)

                        if cantidad == '15':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.06)

                        if cantidad == '16':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.05)

                        if cantidad == '17':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.0471)
                        
                        if cantidad == '18':
                            print(f"Cantidad de cps {cantidad}")
                            cps(0.047)

                        if cantidad == '19':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.04621)

                        if cantidad == '20':
                            print(f"Cantidad de cps : {cantidad}")
                            cps(0.045)

                if option == "2":
                    XD = """
                    App Developer : Dievid#0408 | AleCruZzZ#2137
                    Bot Developer : Dievid#0408 | AleCruZzZ#2137
                    Web Developer : Dievid#0408
                    """
                    print(XD)

        else :
            print('Hubo un error al introducir la clave')
            webbrowser.open("discord.gg/UsF8NG3XyA")
            os.system('pause')
                
else :
    print('Hubo un error al introducir la clave')
    webbrowser.open("discord.gg/UsF8NG3XyA")
    os.system('pause')
#Creditos : https://www.geeksforgeeks.org/how-to-make-a-python-auto-clicker/
