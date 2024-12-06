import pywhatkit
import time
import pyautogui

mensagens =  [""" Meow """]

contacts = ["+5516997511615"]

for contact in contacts:
    for mensagem in mensagens:
        pywhatkit.sendwhatmsg_instantly(contact, mensagem, 15, False, 5)
        time.sleep(4)
        pyautogui.click(x=1850, y=9581)
        time.sleep(2)