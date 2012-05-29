
import re
import simplejson
from color import message
import json


try:
	import requests
	from requests import async
except ImportError: 
	message ("Check dependences: python-requests required", "-" , "ERROR")
	sys.exit(1) 


REG_GET_NAME_MODULE    = r'<h2 class="title"><a href="\/project\/(\w+)"'
REG_GET_VERSION = r"(\w)(\.x)(.*)"
REG_GET_VERSION_D7 = r"(7)(\.x)(.*)"
REG_GET_VERSION_D6 = r"(6)(\.x)(.*)"


DRUPAL_MODULES = "http://drupal.org/project/modules"
DRUPAL_THEMES  = "http://drupal.org/project/themes"
D6_URL_ARGS = {"page":0,"filters":"drupal_core:87 bs_project_sandbox:0","solrsort":"sis_project_release_usage desc"}
D7_URL_ARGS = {"page":0,"filters":"drupal_core:103 bs_project_sandbox:0","solrsort":"sis_project_release_usage desc"}
D8_URL_ARGS = {"page":0,"filters":"drupal_core:7234 bs_project_sandbox:0","solrsort":"sis_project_release_usage desc"}


M_VERSION = " Version "
M_FILE    = " File    "
M_PROJECT = " Project "
M_USER    = " User    "
M_PATH    = " Path    "
M_UPDATE  = " Update  "


#Get the source a direction
#@param url URL direction, as an String
#@param options Options for requests configuration, as an Dictionary
#return source html

def get_source(url, options={}):
	
	params_get = tor = {}
	
	if 'args' in options:
		params_get = args=options['args']
	
	# TODO: Echar andar TOR =p
	"""	
	if "tor" in options:
		try:
			import socks
			import socket
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, "127.0.0.1", 9050, True)
			socket.socket = socks.socksocket
		except ImportError:
			message ("Check dependes: python-SocksiPy required for TOR", "ERROR")
	"""
	
	args = dict()
	args.update({'User-Agent': 'DruScan'})
	
	return requests.get(url, params=params_get, headers=args)

#
# Catch ctrl-c
#	
def signal_handler(signal, frame):
	message ('Exit', "WARNING")
	sys.exit(0)

#
# Update modules list
#	@param project modules | themes update, as an String default String
# @param limit Limit pages on drupal.org, as an Integer
#

def update(project="modules", limit=3):
	
	name_modules6 = []
	name_modules7 = []
	name_modules8 = []
	
	for i in range(limit):
		
		D6_URL_ARGS['page'] = i
		D7_URL_ARGS['page'] = i
		D8_URL_ARGS['page'] = i
		
		html6 = get_source( (DRUPAL_THEMES, DRUPAL_MODULES) [ project == "modules"] , {"args":D6_URL_ARGS} )
		html7 = get_source( (DRUPAL_THEMES, DRUPAL_MODULES) [ project == "modules"] , {"args":D7_URL_ARGS} )
		html8 = get_source( (DRUPAL_THEMES, DRUPAL_MODULES) [ project == "modules"] , {"args":D8_URL_ARGS} )
	
		match6 = re.findall(REG_GET_NAME_MODULE,html6.content)
		name_modules6 += match6
	
		match7 = re.findall(REG_GET_NAME_MODULE,html7.content)
		name_modules7 += match7
	
		match8 = re.findall(REG_GET_NAME_MODULE,html8.content)
		name_modules8 += match8

	if project == "modules":
		save6 = open("data/d6_modules", "w")
		save7 = open("data/d7_modules", "w")
		save8 = open("data/d8_modules", "w")
	else:
		save6 = open("data/d6_themes", "w")
		save7 = open("data/d7_themes", "w")
		save8 = open("data/d8_themes", "w")
	
	simplejson.dump(name_modules6, save6)
	simplejson.dump(name_modules7, save7)
	simplejson.dump(name_modules8, save8)
	
	save6.close();
	save7.close();
	save8.close();

#
#
#	@return An list value

def read_modules(version = "7"):
	read = open("data/d" + str(version) +"_modules","r")
	return json.loads(read.readline());

#
#
#	@return An list value

def read_themes(version = "7"):
	read = open("data/d" + str(version) +"_themes","r")
	return json.loads(read.readline());

#
# Search modules
#	@param url URL site for scanning, as an String
#

def search ( url, project , version ):
	
	ban_f = ban_c = 0		#flags
	modules = (read_themes( version ), read_modules( version )) [ project == "modules"];
	
	for i in modules:
		
		request_url_fail = url + "/" + ("themes", "modules") [ project == "modules"] + "/" + str(i) + "/CHANGELOG.txt"
		request_url_corr = url + "/sites/all/" + ("themes", "modules") [ project == "modules"] + "/" + str(i) + "/CHANGELOG.txt"
		
		if ban_f == 0: # search in /modules or /themes
			html = get_source(request_url_fail);
			
			if html.status_code == 200:
				ban_c = 1
				message(" - " + request_url_fail , M_FILE ,  "OK") #found project
				search = re.findall(REG_GET_VERSION ,html.content) # find version
				if search:
					message("\t" + str(search[0][0] )+ str(search[0][1] ) + str(search[0][2] ), M_VERSION , "WARNING" )
				
		if ban_c == 0: # search in /sites/all/
			html = get_source(request_url_corr);
			
			if html.status_code == 200:
				ban_f = 1
				message(request_url_corr ,M_FILE , "OK") # found project
				search = re.findall(REG_GET_VERSION ,html.content) # find version
				if search:
					message("\t" + str(search[0][0] )+ str(search[0][1] ) + str(search[0][2] ), M_VERSION , "WARNING" )

#	
#	Search user name
#	@param url Drupal Site, as an String
#	@param limit Limit the user id, as an Integer
#

def search_users(url, limit = 20):
	
	for i in range(limit):
		html = get_source( url + "/user/" + str(i))
		red  = re.findall(r"((users)\/(\w+))", html.url)
	
		if red:
			message (red[0][2],M_USER ,"OK")

#
# Return version of core
#	@param url Drupal Site, as an String

def detect_version( url ):
	
	chng   = get_source( url + "/CHANGELOG.txt")
	update = get_source( url + "/update.php"   )
	auth   = get_source( url + "/authorize.php")
	
	search7 = re.findall( REG_GET_VERSION_D7 , chng.content   )
	search6 = re.findall( REG_GET_VERSION_D6 , chng.content   )
	classe  = re.search (r"db-offline"       , update.content )
	
	if classe or search7 or auth.status_code == 403:
		return 7
	
	if search6 or auth.status_code == 404:
		return 6

# Search Paths
# @param url Drupal Site, as an String

def search_urls( url ):
	paths = [
		"/user",
		"/node/add",
	]
	for i in paths:
		html = get_source (url + str(i))
		if html.status_code == 200:
			message(url + str(i), M_PATH ,"OK")

