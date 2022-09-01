#!/usr/local/bin/python3

import requests
import os
import time
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
greetUrl = os.getenv('GREET_URL','http://www.bing.com')
greetRPS = int(os.getenv('GREET_RPS','1'))

if (greetRPS>1000 or greetRPS < 1): 
    logging.error("GREET_RPS value must be in range [1...1000]")
    os._exit(255)

greetSleep = float( 1 / greetRPS)
logging.info("greeter starting with url="+greetUrl+" rps="+str(greetRPS))

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
