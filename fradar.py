# -*- coding: utf-8 -*-
"""
Flight Radar
Monitor flights using flightradar24

Created on Fri Jan 16 10:13:32 2015

@author: ielouafiq
"""
import requests
import futilities as FLUT
default_url = FLUT.default_url

# logging settings
import logging
import datetime
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=FLUT.LOG_FILE,
                    filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
logging.getLogger('').addHandler(console)
logging.debug("\n\n   =====  ===== STARTED :"+__file__+" ON :"+
    str((datetime.datetime.now().time()).isoformat()) + "   =====  =====")
    

        
if __name__=="__main__":
    try:
        latitude, longitude, bound = [long(entry) for entry in 
        raw_input("Enter Latitude, Longitude and Bound seperated by a space:\n").strip().split()]
    except Exception, e:
        logging.error(e)
        logging.warning("Used default (lat, lon, bound)")
        latitude, longitude, bound = FLUT.default_latitude, FLUT.default_longitude, FLUT.default_bound
        
    bounds = FLUT.compute_bounds(latitude, longitude, bound)
    req_url = default_url+"bounds="+",".join([str(elt) for elt in bounds])
    
    req=requests.get(req_url)
    logging.info(req.json())
