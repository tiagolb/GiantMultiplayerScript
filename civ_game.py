from pyvirtualdisplay import Display  
from selenium import webdriver
import time
import pynotify

COUNTRY = "YOUR COUNTRY HERE (First letter is uppercase)"
URL = 'YOUR GAME URL'

def send_message(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

def get_hostname():
    display = Display(visible=0, size=(800, 600))  
    display.start()
    browser = webdriver.Firefox()  
    browser.get(URL)
    time.sleep(3)  

    div_element  = browser.find_element_by_class_name("game-host")
    img_element  = div_element.find_element_by_class_name("tooltip")
    host_country = img_element.get_attribute('oldtitle')
    browser.quit()  
    display.stop()
    return host_country

def main():
    host = get_hostname()
    if COUNTRY == host:
        message = "It's you!!"
        #print message
        send_message("CIV 5", message)
    else:
        message = "It's not you, it's " + host
        #print message
        send_message("CIV 5", message)

if __name__ == "__main__":
    main()
