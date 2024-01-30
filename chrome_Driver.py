from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= options)

#driver = webdriver.Chrome()
driver.get("https://techwithtim.net")
print(driver.title)
driver.close()

'''1) you do not need to download the web driver anymore. Just use 
        
2) if you open a page and it closes immediately, add the following (assuming you are using Chrome as well):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options= options)'''