<<<<<<< HEAD
# Program to send bulk messages through WhatsApp web from an excel sheet without saving contact numbers
# Author @inforkgodara

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from time import sleep
import pandas

Contact = ["+55112234253"]

count = 0

service = webdriver.ChromeService()
driver = webdriver.Chrome(service=service)

driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visiable.")


for column in Contact:
    try:
        url = 'https://web.whatsapp.com/send?phone={}&text={}'.format(Contact[count], "Ababa")
        sent = False
        # It tries 3 times to send a message in case if there any error occurred
        driver.get(url)
        try:
            click_btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@role="textbox"][@data-tab="10"]')))
            
            click_btn.send_keys(Keys.ENTER)

        except Exception as e:
            print("Sorry message could not sent to " + str(Contact[count]))
        else:
            sleep(2)
            click_btn.click()
            sent = True
            sleep(5)
            print('Message sent to: ' + str(Contact[count]))
        count = count + 1
    except Exception as e:
        print('Failed to send message to ' + str(Contact[count]) + str(e))
driver.quit()
print("The script executed successfully.")
=======
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
>>>>>>> 0cb41b9a8286845cd73fa0bc1a9b5a139a83b527
