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