try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description':'Flight Radar',
	'author':'Ismail Elouafiq',
	'url':'https://github.com/nidhog/flightradar',
	'download_url':'https://github.com/nidhog/flightradar/archive/flightradar.zip',
	'author_email':'i.elouafiq@gmail.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['flightRadar'],
	'scripts':[],
	'name':'Flight Radar'
}

setup(**config)