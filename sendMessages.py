from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import manipulate

def test(seacrhbar,contact,message):
	seacrhbar.send_keys(contact)
	time.sleep(5)
	findUser = driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact))
	findUser.click()
	sendMessage = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
	sendMessage.clear()
	sendMessage.send_keys(message)
	sendMessage.send_keys(Keys.RETURN)

manipulate.updateStatusToNotWished()
events = manipulate.checkIfEventToday()
birthdays = manipulate.checkIfBirthdayToday()

driver = webdriver.Chrome(executable_path=r'C:\Users\Mahesh\Desktop\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
input("Press anything after QR scan")
time.sleep(5)
seacrhbar = driver.find_element_by_class_name('_2S1VP.copyable-text.selectable-text')

for event in events:
    for contact in event[0]:
        test(seacrhbar,contact,event[1])
    manipulate.updateStausToWished(event[2])

for birthday in birthdays:
    test(seacrhbar,birthday[0],birthday[1])
