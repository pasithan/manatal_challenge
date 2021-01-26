# Exercise 4: Scraping Test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException


def getFollowers(url: str) -> str:
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(url) 

    try:
        wait = WebDriverWait(driver, 3)
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div//div[@class="css-1dbjc4n r-13awgt0 r-18u37iz r-1w6e6rj"]/div[2]//span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"]')))
    except TimeoutException:
        print("Loading took too much time")
        return TimeoutException

    number_follower = element.text
    driver.close()

    return number_follower
    

print(getFollowers('https://twitter.com/KMbappe'))

# total time used: 5 hours 47 mins
