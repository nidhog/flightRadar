# -*- coding: utf-8 -*-
"""
Flight Radar
Monitor flights using flightradar24

Created on Fri Jan 16 10:13:32 2015

@author: ielouafiq
"""
import requests
latitude = 43
longitude = 7
bound = 1
default_url = "http://arn.data.fr24.com/zones/fcgi/feed.js?"

def compute_bounds(lat, lon, R):
        lat1, lon1 = lat+R, lon-R
        lat2, lon2 = lat-R, lon+R
        return lat1, lat2, lon1, lon2
        
if __name__=="__main__":
    bounds = compute_bounds(latitude, longitude, bound)
    req_url = default_url+"bounds="+",".join([str(elt) for elt in bounds])
    
    req=requests.get(req_url)
    print req.text
