
#  Common Api call endpoint   https://whalewisdom.com/shell/command
        #Shared access key: FRh6eFbHHpNfGCeV8uVI
        #Secret Access Key: dKotOOMwaqXVc6gDVxmFCdIjOnBhAFsdFcmwlrGM

#       limited to 20 requests per minute



 #      Format for requests:  https://whalewisdom.com/shell/command?args=[args]&api_shared_key=[api_shared_key]&api_sig=[api_sig]&timestamp=[timestamp]
                        #args: json formatted object that contains command and other stuff
                        #timestamp: marks the day and time the request was sent, they expire after some time so malicious users cant 
                        #   capture request and resubmit them later.
                        #   This parameter is only used when authenticating via digital signitures. 
                        #api_shared_key: above
                        #api_sig: a signiture of the args parameter created using your secret access key. Uses HMAC-SHA1
                        #   to digest args parameter, and then encode in base64. 



# How to make an API call: 
    #each API call is a HTML GET Request. Constructed as follows: 
    #https://whalewisdom.com/shell/command[.output_type]?args=[args]&api_shared_key=[api_shared_key]&api_sig=[api_sig]
    
    #Parameters:
        #args: actual arguments to execute. - reread for more practice
    #Optional Parameters:
        #.output_type: default, command results are in HTML Format. If the command supports it, it can be outputted 
        #       as JSON or CSV. Specify by adding .json and .csv 
        #   ex: https://whalewisdom.com/shell/command.json?args=%7B%22command%22:%22stock_lookup%22,%20%22name%22:%22apple%20comp%22%7D


import requests
from datetime import datetime
utc = datetime.utcnow()

from datetime import datetime,timezone
now_utc = datetime.now(timezone.utc)


r =requests.get('https://whalewisdom.com/shell/command?args=[args]&api_shared_key=[FRh6eFbHHpNfGCeV8uVI]&api_sig=[api_sig]&timestamp=[utc]')

print(r.status_code)

r.headers







