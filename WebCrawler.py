import os
import time
from selenium import webdriver

googleChromeExecutionPath = 'C:/Users/amiller/PycharmProjects/Heroku_SF_Webscrapper/chromedriver'

# open the main website
def navigateCountriesForListing(driver):
    # open the web page
    driver.get("http://example.webscraping.com/")

    # waits for the page to load
    time.sleep(5)

    return driver

# get all the links inside the table
def getAllLinks(driver):
    listOfCountries = []
    tableDiv = driver.find_element_by_id("results")
    elems = tableDiv.find_elements_by_tag_name("a")
    for elem in elems:
        # get the text of the hyperlink
        elementText = elem.text
        listOfCountries.append(elementText)
    return listOfCountries

# click next for the next table
def clickNext(driver):
    nextButton = driver.find_element_by_link_text('Next >')
    nextButton.click()
    # waits for the page to load
    time.sleep(5)
    return nextButton

# get the chrome browser without opening a window
def getWebDriver():
    chrome_options = webdriver.ChromeOptions()

    if os.environ.get("GOOGLE_CHROME_BIN") is not None:
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    # first is Heroku usage, second is local dev
    if os.environ.get("CHROMEDRIVER_PATH") is not None:
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    else:
        driver = webdriver.Chrome(executable_path=googleChromeExecutionPath, options=chrome_options)

    return driver