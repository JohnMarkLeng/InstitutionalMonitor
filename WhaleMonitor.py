import pandas as pd
import numpy as np
import yahoo_fin.stock_info as si
from urllib.request import Request, urlopen  # Python 3


                        # elif fund == "":         #placeholder
                        #         pass
                        #print("The item you are looking for may not exist, or check your spelling.")
                                #print("The item you are looking for could not be found")
def getFundCSV(fund):

    fund = fund.strip().lower()

    if fund == "blackrock":
        csvLink = '/Users/JohnLeng/Desktop/Institutional_Monitor/CSV/BlackrockQ3_2021.csv'

    elif fund == "vanguard":
        csvLink = '/Users/JohnLeng/Desktop/Institutional_Monitor/CSV/Vanguard_groupQ3_2021.csv'

    else:
        return "error!"

    return csvLink



def findStocksByPrice(fundLink, lowerPrice, upperPrice):                #Price

    with open('stockPrice.txt', 'w+') as stockPriceFile:
        if fundLink == "error!":
            stockPriceFile.write("Error: Please check the fund name")
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
            QtrFirstOwnedFile.write("Error: Please check the fund name")
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








##### DONE

def findBySharePercentageChange(fundLink, lowerPrice, upperPrice, Increase_Decrease, percentChange):            #direction, percentChange in format 15.34 for 15%

    Increase_Decrease = Increase_Decrease.strip().lower()
    percentChange = float(percentChange)

        
    with open('share_%_Change.txt', 'w+') as percentChangeFile:

        if fundLink == "error!":
            percentChangeFile.write("Error: Please check the fund name")
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

                    if(Increase_Decrease == "reduction" and increaseOrDecrease == "reduction" and stockPercentChange <= ( -1 * percentChange) and tickerPrice >= lowerPrice and tickerPrice <= upperPrice):              #logic to retrieve data
                        textLine = ("Ticker: " + csv_df.loc[index,'Symbol'] + "   Holding Value: $" + str("{:,}".format(round(marketValue,2))) +
                            "   Ownership %: " + csv_df.loc[index, "% Ownership"] + "   Quarter first owned: " + csv_df.loc[index, "Qtr first owned"] + 
                            "   Percent Change in Shares this Q: " + str(stockPercentChange) + "   Source Date: " + csv_df.loc[index, "source_date"] + "\n")
                        percentChangeFile.write(textLine)
        
            except: 
                pass
        return percentChangeFile




# def findByFirstQtrAndSharePercentageChange(fund, lowerPrice, upperPrice, Increase_Decrease, percentChange, ):            #direction, percentChange in format 15.34 for 15%
#     pass                    #idk if this is desired. Quarter first bought and latest % stock ownership change 




def findByCompanyOwnership(fundLink, lowerPrice, upperPrice, desiredOwnership):                #Price, Ownership in format 15 = 15%

    with open('Ownership.txt', 'w+') as ownershipFile:

        if fundLink == "error!":
            ownershipFile.write("Error: Please check the fund name")
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
    #print("Completed Operation")




#findStocksByPrice("Vanguard", 0, 5)

#findByQtrFirstOwned("Vanguard", 0, 1000000, "q3 2021", "q2 2021 ")

#findBySharePercentageChange("Vanguard", 0, 1000000, "addition", 40)

#findByCompanyOwnership("blackrock", 0, 1000000, 30)



            


        
    

# csv_urls = [

    #         #'/Users/JohnLeng/Desktop/Institutional_Monitor/CSV/Vanguard_groupQ3_2021.csv',
    #         #'/Users/JohnLeng/Desktop/Institutional_Monitor/CSV/BlackrockQ3_2021.csv',

    #     ]

# for url in csv_urls:

#     df = pd.read_csv(url)

#       header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36'}



#     response = requests.get(url, headers=header)
#     print(response.status_code)
#     if response.status_code == 200:
#         file_path = os.path.join(pdf_storage_dir, os.path.basename(url)) #gets the pdf file name 
#         with open(file_path, 'wb') as f: 
#             f.write(response.content)
#             print("added")

# print(os.path)






# response = urllib.request.urlopen(url)
# file = open("")


# tables = camelot.read_pdf(url, headers=header)

# tables
