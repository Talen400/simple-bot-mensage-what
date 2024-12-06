import pywhatkit
import time
import pyautogui

mensagens = [""" Meow"""]

contacts = ["+55XXXXXXXXXXX"]

for contact in contacts:
    for mensagem in mensagens:
        try:
            
            pywhatkit.sendwhatmsg_instantly(
                contact,
                mensagem,
                10,       
                False,    
                7,       
            )
            
            time.sleep(4)
            
            pyautogui.hotkey('ctrl', 'w')
            
            time.sleep(2)
            
        except Exception as e:
            print(f" Error Contact:  {contact}: {e}")