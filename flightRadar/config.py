# -*- coding: utf-8 -*-
"""
Flight Configuration Properties

Configuration properties parsing is done from a file present in the location given by the config_file_location String

Created on Mon Jan 19 10:23:57 2015

@author: ielouafiq
"""
from ConfigParser import ConfigParser

# config file location
config_file_location = "config.ini"
# config parser
config_parser = ConfigParser()
# parse properties from the  config file
try:
	config_parser.read()
except Exception, e:
	pass

# Log File location
LOG_FILE 	 = "temp/.log_file.log"
# default values for url, lat, lon, bound
default_url = "http://arn.data.fr24.com/zones/fcgi/feed.js?"
default_latitude = 43
default_longitude = 7
default_bound = 1

