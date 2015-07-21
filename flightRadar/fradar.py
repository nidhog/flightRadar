# -*- coding: utf-8 -*-
"""
Flight Radar
Monitor flights using requests to flightradar24 and Google Geocoding API

Created on Fri Jan 16 10:13:32 2015

@author: ielouafiq
"""

import time
import requests
import futilities as FLUT
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

default_url = FLUT.default_url

# logging settings
import logging
import datetime
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=FLUT.LOG_FILE,
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
logging.getLogger('').addHandler(console)
logging.debug("\n\n   =====  ===== STARTED :"+__file__+" ON :"+
    str((datetime.datetime.now().time()).isoformat()) + "   =====  =====")
    
def monitor_flights(lat, lon, bound):
    bounds = FLUT.compute_bounds(lat, lon, bound)
    str_bounds = ",".join([str(elt) for elt in bounds])
    req_url = default_url+"bounds="+str_bounds
    
    req=requests.get(req_url)    
    flights = req.json()
    print '-'*50
    print ' Bounds: '+str_bounds+' Full count: '+str(flights["full_count"])
    print '-'*50
    for hash_value, data in flights.items():
        if isinstance(data, list) and len(data)>=13:
            depAirport, arrAirport = data[11], data[12]
            flightNumber, acType = data[13], data[8]
            print "- "+flightNumber+" | "+depAirport+"-->"+arrAirport+" | Aircraft: "+acType
            print "  _ Great-Circle Distance from location:      "+str(great_circle( (lat, lon), (data[1], data[2]) ))
    print '-'*50
    
        
if __name__=="__main__":
    geolocator = Nominatim()
    try:
        location = geolocator.geocode(raw_input("Enter location here: "))
        latitude, longitude,  = location.latitude, location.longitude
        print "\nChosen location is in: ( latitude:", latitude, ", longitude:", longitude," )"
        bound = int(raw_input("\nEnter max lat/lon difference from boundaries: "))
        if bound<0:
            bound = FLUT.default_bound
    except Exception, e:
        logging.error(e)
        logging.warning("Used default (lat, lon, bound)")
        latitude, longitude, bound = FLUT.default_latitude, FLUT.default_longitude, FLUT.default_bound
    # Stop iterations
    it = 0
    while True:
        monitor_flights(latitude, longitude, bound)
        time.sleep(3)
        if it == 3:
            q = raw_input("quit? (y/n) ")
            if q == 'y':
                break
            it = 0
        it+=1