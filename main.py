import pywhatkit
import time
import pyautogui
import pandas as pd

csv_file = "path"

df = pd.read_csv(csv_file)

df["telefone"] = df.telefone.astype(str)

df['telefone'] = df['telefone'].apply(lambda x: f"+{x}")

contacts = df.telefone.tolist()

mensagens = [""" Meow """]

for contact in contacts:
    for mensagem in mensagens:
        try:
            
            pywhatkit.sendwhatmsg_instantly(
                contact,
                mensagem,
                15,       
                False,    
                5,
            )
            
            time.sleep(4)
            
            pyautogui.hotkey('ctrl', 'w')
            
            time.sleep(2)
            
        except Exception as e:
            print(f" Error Contact:  {contact}: {e}")