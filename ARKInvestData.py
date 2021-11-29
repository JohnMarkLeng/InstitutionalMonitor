import pandas as pd
import numpy as np
import yahoo_fin.stock_info as si
from urllib.request import Request, urlopen  # Python 3

csv_urls = [
    
        #PRNT
        "https://ark-funds.com/wp-content/uploads/funds-etf-csv/ARK_INNOVATION_ETF_PRNT_HOLDINGS.csv"
        ,

        #K
        'https://ark-funds.com/wp-content/uploads/funds-etf-csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv'
        ,

        #G
        'https://ark-funds.com/wp-content/uploads/funds-etf-csv/ARK_INNOVATION_ETF_ARKG_HOLDINGS.csv'
        ,

        #W
        'https://ark-funds.com/wp-content/uploads/funds-etf-csv/ARK_INNOVATION_ETF_ARKW_HOLDINGS.csv'
        , 

        #Q
        'https://ark-funds.com/wp-content/uploads/funds-etf-csv/ARK_INNOVATION_ETF_ARKQ_HOLDINGS.csv'
        ,

        #F
        'https://ark-funds.com/wp-content/uploads/funds-etf-csv/ARK_INNOVATION_ETF_ARKF_HOLDINGS.csv'
        , 

        #X
        'https://ark-funds.com/wp-content/uploads/funds-etf-csv/ARK_INNOVATION_ETF_ARKX_HOLDINGS.csv'
        , 


        #IZRL useless fund. 
        'https://ark-funds.com/wp-content/uploads/funds-etf-csv/ARK_INNOVATION_ETF_IZRL_HOLDINGS.csv'
        ,

    ]

def under(underPrice):
    
    print("This operation may take a few minutes to complete...")

    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36'}
    for url in csv_urls:
        req = Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36')
        content = urlopen(req)


        csv_df = pd.read_csv(content, keep_default_na=False) #creates a dataframe from csv


        for index, row in csv_df.iterrows():  #gets index and row information

            sharesString = csv_df.loc[index, 'shares']

            tickerName = csv_df.loc[index,'ticker']
            #investment = csv_df.loc[index, 'market value($)']
            
            #print(csv_df.loc[index,'ticker'])

            if(tickerName != "" and sharesString != ""):
                try: 
                    sharesInt = int(sharesString.replace(',', ''))
                    tickerPrice = si.get_live_price(csv_df.loc[index,'ticker'])
                    holdingValue = tickerPrice * sharesInt;

                    if(tickerPrice < underPrice):
                        print("Ticker: " + csv_df.loc[index,'ticker'] + " | Cost: " + tickerPrice  + "  |  Market Value: $" + str("{:,}".format(round(holdingValue,2))) + "  |  Fund: " + csv_df.loc[index,'fund'])
                except: 
                    pass
                    #print(csv_df.loc[index,'ticker'] + " had an error")

            
    print("Operation Completed")


under(5)

# for url in csv_urls:

#     df = pd.read_csv(url)


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
