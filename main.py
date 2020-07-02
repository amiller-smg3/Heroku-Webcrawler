from WebCrawler import *
from PostgresHandler import *

if __name__ == "__main__":
    print("started running")

    # set up the variables
    driver = getWebDriver()
    listOfNames = []
    continueLooping = True
    listOfNewNames = []

    # navigate to the desired website
    driver = navigateCountriesForListing(driver)

    # loop through all the pages
    while continueLooping:

        listOfNames.extend(getAllLinks(driver))

        print(listOfNames)

        try:
            clickNext(driver)
        except:
            continueLooping = False

    # if the country doesn't already exist in the database, add it
    existingCountries = queryCountries()


    for countryName in listOfNames:
        if countryName not in existingCountries:
            print(countryName)
            listOfNewNames.append(countryName)

    if len(listOfNewNames) > 0:
        insertNewCountryRecord(listOfNewNames)

    print("finished running")