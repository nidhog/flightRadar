# -*- coding: utf-8 -*-
"""
Flight Utilities

Created on Mon Jan 19 10:23:57 2015

@author: ielouafiq
"""

# Log File location
LOG_FILE 	 = config.LOG_FILE
# default values for url, lat, lon, bound
default_url = config.default_url
default_latitude = config.default_latitude
default_longitude = config.default_longitude
default_bound = config.default_bound

def distance(lat1, lat2):
    """Return distance in miles between two lats
    """
    return 69*abs(lat1-lat2)
    
def compute_bounds(lat, lon, R):
    """Compute bounds given lat, lon and radius
    """
    lat1, lon1 = lat+R, lon-R
    lat2, lon2 = lat-R, lon+R
    return lat1, lat2, lon1, lon2