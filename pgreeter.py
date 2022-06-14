#!/usr/bin/python

import requests
import os
import time
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
greetUrl = os.getenv('GREET_URL','http://www.bing.com')
greetSleep = int(os.getenv('GREET_SLEEP','5'))
logging.info("greeter starting with url="+greetUrl+" sleep="+str(greetSleep))

while ( 1 == 1 ): 
    logging.info("greeter is awake")
    try:
        res = requests.get(greetUrl)
        logging.info("greeting "+greetUrl+" result code "+str(res.status_code))
    except:
        logging.error("unable to greet "+greetUrl)
    finally:
        logging.info("greeting to sleep for "+str(greetSleep)+" seconds")
        time.sleep(greetSleep)
