import pandas as pd
import numpy as np
import yahoo_fin.stock_info as si
from urllib.request import Request, urlopen  # Python 3


def getFundCSV(fund):

    fund = fund.strip().lower()

    if fund == "blackrock":
        csvLink = '/Users/JohnLeng/Desktop/Institutional_Monitor/TRIAL CSV/BlackrockQ2_2021.csv'
    else:
        return "error!"

    return csvLink



def findStocksByPrice(fundLink, lowerPrice, upperPrice):                #Price

    with open('stockPrice.txt', 'w+') as stockPriceFile:
        if fundLink == "error!":
            stockPriceFile.write("This feature is only available for subscribers")
            return stockPriceFile
        csv_df = pd.read_csv(fundLink, keep_default_na=False) #creates a dataframe from csv

        for index, row in csv_df.iterrows():  #gets index and row information

            try: 
                shares = int(csv_df.loc[index, 'Shares Held'])
                marketValue = float(csv_df.loc[index, 'Market Value'])
                tickerName = csv_df.loc[index,'Symbol']
                tickerPrice = marketValue/shares


                if(tickerName != "" and shares != "" and marketValue != "" and shares!= 0 and marketValue != 0):
                    
                    if(tickerPrice <= upperPrice and tickerPrice >= lowerPrice):
                        textLine = ("Ticker: " + csv_df.loc[index,'Symbol'] + "   Holding Value: $" + str("{:,}".format(round(marketValue,2))) +
                            "   Ownership %: " + csv_df.loc[index, "% Ownership"] + "   Quarter first owned: " + csv_df.loc[index, "Qtr first owned"] + 
                            "   Source Date: " + csv_df.loc[index, "source_date"] + "\n")
                        stockPriceFile.write(textLine)

            except: 
                pass   
    return stockPriceFile




def findByQtrFirstOwned(fundLink, lowerPrice, upperPrice, *qtrAndYear):            #Price, QtrAndYear

    with open('QtrFirstOwned.txt', 'w+') as QtrFirstOwnedFile:
        if fundLink == "error!":
            QtrFirstOwnedFile.write("This feature is only available for subscribers")
            return QtrFirstOwnedFile

        csv_df = pd.read_csv(fundLink, keep_default_na=False) #creates a dataframe from csv

        for Qtr in qtrAndYear:
            Qtr = str(Qtr).strip().upper()
            Qtr = Qtr.replace("_", " ")

            for index, row in csv_df.iterrows():  #gets index and row information

                try: 
                    shares = int(csv_df.loc[index, 'Shares Held'])
                    marketValue = float(csv_df.loc[index, 'Market Value'])
                    tickerName = csv_df.loc[index,'Symbol']

                    tickerPrice = marketValue/shares
                    QtrFirstOwned = str(csv_df.loc[index, 'Qtr first owned'])
                    

                    if(tickerName != "" and shares != "" and marketValue != "" and shares != 0 and marketValue != 0):

                            
                        if(Qtr == QtrFirstOwned and tickerPrice >= lowerPrice and tickerPrice <= upperPrice):              #logic to retrieve data
                            textLine = ("Ticker: " + csv_df.loc[index,'Symbol'] + "   Holding Value: $" + str("{:,}".format(round(marketValue,2))) +
                                "   Ownership %: " + csv_df.loc[index, "% Ownership"] + "   Quarter first owned: " + csv_df.loc[index, "Qtr first owned"] + 
                                "   Source Date: " + csv_df.loc[index, "source_date"] + "\n")
                            QtrFirstOwnedFile.write(textLine)
        
                except: 
                        pass
    return QtrFirstOwnedFile




def findBySharePercentageChange(fundLink, lowerPrice, upperPrice, Increase_Decrease, percentChange):            #direction, percentChange in format 15.34 for 15%

    Increase_Decrease = Increase_Decrease.strip().lower()
    percentChange = float(percentChange)

        
    with open('share_%_Change.txt', 'w+') as percentChangeFile:

        if fundLink == "error!":
            percentChangeFile.write("This feature is only available for subscribers")
            return percentChangeFile
        
        csv_df = pd.read_csv(fundLink, keep_default_na=False) #creates a dataframe from csv


        for index, row in csv_df.iterrows():  #gets index and row information

            try: 
                shares = int(csv_df.loc[index, 'Shares Held'])
                marketValue = float(csv_df.loc[index, 'Market Value'])
                tickerName = csv_df.loc[index,'Symbol']

                tickerPrice = marketValue/shares
                increaseOrDecrease = str(csv_df.loc[index, 'Change Type'])
                stockPercentChange = float(csv_df.loc[index, '% Change'])

                if(tickerName != "" and shares != "" and marketValue != "" and shares != 0 and marketValue != 0):

                    if(Increase_Decrease == "addition" and increaseOrDecrease == "addition" and stockPercentChange >= percentChange and tickerPrice >= lowerPrice and tickerPrice <= upperPrice):          #logic to retrieve data
                        textLine = ("Ticker: " + csv_df.loc[index,'Symbol'] + "   Holding Value: $" + str("{:,}".format(round(marketValue,2))) +
                            "   Ownership %: " + csv_df.loc[index, "% Ownership"] + "   Quarter first owned: " + csv_df.loc[index, "Qtr first owned"] + 
                            "   Percent Change in Shares this Q: " + str(stockPercentChange) + "   Source Date: " + csv_df.loc[index, "source_date"] + "\n")
                        percentChangeFile.write(textLine)

                    if(Increase_Decrease == "reduction" and increaseOrDecrease == "reduction" and stockPercentChange <= (-1 *percentChange) and tickerPrice >= lowerPrice and tickerPrice <= upperPrice):              #logic to retrieve data
                        textLine = ("Ticker: " + csv_df.loc[index,'Symbol'] + "   Holding Value: $" + str("{:,}".format(round(marketValue,2))) +
                            "   Ownership %: " + csv_df.loc[index, "% Ownership"] + "   Quarter first owned: " + csv_df.loc[index, "Qtr first owned"] + 
                            "   Percent Change in Shares this Q: " + str(stockPercentChange) + "   Source Date: " + csv_df.loc[index, "source_date"] + "\n")
                        percentChangeFile.write(textLine)
        
            except: 
                pass
        return percentChangeFile





def findByCompanyOwnership(fundLink, lowerPrice, upperPrice, desiredOwnership):                #Price, Ownership in format 15 = 15%

    with open('Ownership.txt', 'w+') as ownershipFile:

        if fundLink == "error!":
            ownershipFile.write("This feature is only available for subscribers")
            return ownershipFile

        csv_df = pd.read_csv(fundLink, keep_default_na=False) #creates a dataframe from csv

        for index, row in csv_df.iterrows():  #gets index and row information

            try: 
                shares = int(csv_df.loc[index, 'Shares Held'])
                marketValue = float(csv_df.loc[index, 'Market Value'])
                tickerName = csv_df.loc[index,'Symbol']
                tickerPrice = marketValue/shares
                ownership = float(csv_df.loc[index,'% Ownership'])


                if(tickerName != "" and shares != "" and marketValue != "" and shares!= 0 and marketValue != 0):
                    
                    if(tickerPrice <= upperPrice and tickerPrice >= lowerPrice and ownership >= desiredOwnership):
                        textLine = ("Ticker: " + csv_df.loc[index,'Symbol'] + "   Holding Value: $" + str("{:,}".format(round(marketValue,2))) +
                            "   Ownership %: " + csv_df.loc[index, "% Ownership"] + "   Quarter first owned: " + csv_df.loc[index, "Qtr first owned"] + 
                            "   Source Date: " + csv_df.loc[index, "source_date"] + "\n")
                        ownershipFile.write(textLine)
  
            except: 
                pass
        return ownershipFile
