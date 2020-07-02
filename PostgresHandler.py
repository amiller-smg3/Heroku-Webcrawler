import os
import psycopg2
from sqlalchemy import create_engine

# get either the remote database or the local one
def getDatabaseURL():
    if os.getenv("DATABASE_URL") is None:
        return "<YOUR DATABASE URI>"
    else:
        return os.getenv("DATABASE_URL")

# query for all existing countries so we don't duplicate data
def queryCountries():
    returningList = []
    engine = create_engine(getDatabaseURL())
    with engine.connect() as connection:
        result = connection.execute("SELECT Name from salesforceccgblog.country__c")
        for row in result:
            returningList.append(str(row[0]).strip())
        connection.close()
    return returningList

# create new entry for all in the list at once, using only one connection
def insertNewCountryRecord(countryList):

    stringNames = ''
    for item in countryList:
        stringNames += "(%s),"
    stringNames = stringNames[:-1]

    engine = create_engine(getDatabaseURL())
    with engine.connect() as connection:
        sql = "INSERT INTO salesforceccgblog.country__c " + "( name ) VALUES " + stringNames
        connection.execute(sql, countryList)
        connection.close()