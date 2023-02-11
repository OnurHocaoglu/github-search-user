from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Selenium==4.8.0

search_keys = input("Search User : ")

driver = webdriver.Chrome() # Chrome !! Chrome:	https://chromedriver.chromium.org/downloads

url = "http://www.github.com"

driver.get(url)

sleep(1)

searchInput = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]")

searchInput.send_keys(search_keys)

searchInput.send_keys(Keys.ENTER)

sleep(1)

search_users = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div/div[2]/nav[1]/a[10]").click()

sleep(1)

users_list = driver.find_elements(By.CSS_SELECTOR,".hx_hit-user a")

with open("print.txt", "w", encoding='utf-8') as user_print:
    for user in users_list:
        user_print.writelines(user.get_attribute("href"))
        user_print.writelines("\n")
        user_print.writelines(user.text.replace("Follow",""))
        user_print.writelines("\n")
        user_print.writelines("*" * 30)
        user_print.writelines("\n")

driver.close()


