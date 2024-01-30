from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                          options=options)


#driver = webdriver.Chrome()
driver.get("https://neuralnine.com")
driver.maximize_window()
#print(driver.title)

links = driver.find_elements('xpath','//a[@href]') # // = in whole page, find all anchor tags that has attribute href
for link in links:
    if  "Books" in link.get_attribute("innerHTML"):
        link.click()
        break
    print(link.get_attribute("innerHTML"))


#driver.close()

'''1) you do not need to download the web driver anymore. Just use 
        
2) if you open a page and it closes immediately, add the following (assuming you are using Chrome as well):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options= options)'''