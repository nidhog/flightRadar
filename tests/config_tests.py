from nose.tools import *
from flightRadar.config import default_url

def used_url_is_fr24():
	assert_equal(default_url, "http://arn.data.fr24.com/zones/fcgi/feed.js?")